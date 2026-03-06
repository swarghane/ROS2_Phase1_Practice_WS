import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped


class StaticFramePublisher(Node):
    def __init__(self):
        super().__init__('static_tf_publisher')

        # 1. Initialize the Static Broadcaster
        self.tf_static_broadcaster = StaticTransformBroadcaster(self)

        # 2. Create the transform message
        t = TransformStamped()

        # Timestamp and Frame IDs
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'  # Parent
        t.child_frame_id = 'lidar_link'  # Child

        # 3. Translation (Position in meters)
        t.transform.translation.x = 0.1
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.5

        # 4. Rotation (Quaternion - 0 rotation here)
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        # 5. Send the transform
        self.tf_static_broadcaster.sendTransform(t)
        self.get_logger().info("Static TF: base_link -> lidar_link published!")


def main():
    rclpy.init()
    node = StaticFramePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()


if __name__ == '__main__':
    main()
