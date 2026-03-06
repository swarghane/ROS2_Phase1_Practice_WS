import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import math


class DynamicFramePublisher(Node):
    def __init__(self):
        super().__init__('dynamic_tf_publisher')

        # 1. Initialize the Dynamic Broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

        # 2. Create a timer to update the transform at 20Hz (every 0.05s)
        self.timer = self.create_timer(0.05, self.broadcast_timer_callback)
        self.get_logger().info("Dynamic TF: turtle1 -> carrot_link is active!")

    def broadcast_timer_callback(self):
        t = TransformStamped()

        # Update the timestamp
        t.header.stamp = self.get_clock().now().to_msg()

        # Define the link: Parent is turtle1, Child is carrot_link
        t.header.frame_id = 'turtle1'
        t.child_frame_id = 'carrot_link'

        # 3. Create a circular motion (The "Carrot on a Stick")
        seconds = self.get_clock().now().to_msg().sec + \
            self.get_clock().now().to_msg().nanosec * 1e-9

        # The carrot will circle turtle1 at a 2-meter radius
        t.transform.translation.x = 2.0 * math.sin(seconds)
        t.transform.translation.y = 2.0 * math.cos(seconds)
        t.transform.translation.z = 0.0

        # No rotation for this simple example
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        # 4. Send the transform
        self.tf_broadcaster.sendTransform(t)


def main():
    rclpy.init()
    node = DynamicFramePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()


if __name__ == '__main__':
    main()
