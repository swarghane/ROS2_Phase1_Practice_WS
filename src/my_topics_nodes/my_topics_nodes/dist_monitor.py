import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DistMonitor(Node):
    def __init__(self) -> None:
        super().__init__("dist_monitor")

        self.declare_parameter("safety_topic", "/sensor_distance")
        safety_topic = str(self.get_parameter("safety_topic").value)

        self._subs = self.create_subscription(
            Float32, safety_topic, self.monitor_callback, 10)

    def monitor_callback(self, msg):
        if msg.data >= 1:
            self.get_logger().info(
                f"Status: Green - Path Clear ---- Distance {msg.data}m")

        elif msg.data < 1 and msg.data >= 0.5:
            self.get_logger().warn(
                f"Status: Yellow - Object Approaching ---- Distance {msg.data}m")

        else:
            self.get_logger().error(
                f"Status: RED - EMERGENCY STOP! ---- Distance {msg.data}m"
            )


def main(args=None):
    rclpy.init(args=args)
    dist_monitor = DistMonitor()
    try:
        rclpy.spin(dist_monitor)
    except KeyboardInterrupt:
        pass
    finally:
        dist_monitor.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
