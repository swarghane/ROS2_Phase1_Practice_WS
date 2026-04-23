import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher_node')
        self.publisher_ = self.create_publisher(Image, 'camera_frame', 10)

        # 1. Force V4L2 Backend
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

        # 2. Set MJPG format (This is critical for WSL performance)
        # MJPG compresses the stream before it hits the USB tunnel
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

        # 3. Lower resolution to reduce data load
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # 4. Shorten the internal OpenCV timeout buffer
        self.cap.set(cv2.CAP_PROP_FPS, 30)

        if not self.cap.isOpened():
            self.get_logger().error("Still can't open camera!")

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.bridge = CvBridge()

    def timer_callback(self):
        # Optional: Grab/Retrieve method is sometimes more stable than .read()
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_.publish(msg)
        else:
            # Don't log error every single frame to avoid terminal spam
            pass

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    camera_publisher = CameraPublisher()

    try:
        rclpy.spin(camera_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        camera_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
