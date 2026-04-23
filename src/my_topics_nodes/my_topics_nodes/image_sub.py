import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber_node')
        # Subscribe to the same topic used by the publisher
        self.subscription = self.create_subscription(
            Image,
            'camera_frame',
            self.listener_callback,
            10)

        self.bridge = CvBridge()

    def listener_callback(self, msg):
        # 1. Convert ROS Image message back to OpenCV format
        current_frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # 2. Process the image (e.g., convert to grayscale)
        gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.flip(gray_frame, 1)

        # 3. Display the processed frame
        cv2.imshow("Processed Camera Feed", gray_frame)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()

    try:
        rclpy.spin(image_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        image_subscriber.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
