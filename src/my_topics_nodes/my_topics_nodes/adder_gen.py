import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32
import random


class AdderGenerator(Node):
    def __init__(self) -> None:
        super().__init__("adder_gen")

        self.declare_parameter("output_topic", "/number")
        output_topic = str(self.get_parameter("output_topic").value)
        self.publisher_ = self.create_publisher(Int32, output_topic, 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(1, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing Random Number:  {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    adder_gen = AdderGenerator()
    try:
        rclpy.spin(adder_gen)
    except KeyboardInterrupt:
        pass
    finally:
        adder_gen.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
