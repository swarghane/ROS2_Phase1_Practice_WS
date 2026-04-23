import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32


class AdderSummation(Node):
    def __init__(self) -> None:
        super().__init__("adder_sum")

        self.running_total = 0
        self.declare_parameter('input_topic', '/number')
        self.declare_parameter('output_topic', '/sum')

        input_topic = str(self.get_parameter('input_topic').value)
        output_topic = str(self.get_parameter('output_topic').value)

        self.publisher_ = self.create_publisher(Int32, output_topic, 10)
        self.subscriber_ = self.create_subscription(
            Int32, input_topic, self.sum_callback, 10)

    def sum_callback(self, msg):
        self.running_total += msg.data

        sum_msg = Int32()
        sum_msg.data = self.running_total
        self.publisher_.publish(sum_msg)

        self.get_logger().info(
            f"Current Published value: {msg.data} /nSummation of published values {self.running_total} ")


def main(args=None):
    rclpy.init(args=args)
    adder_sum = AdderSummation()
    rclpy.spin(adder_sum)
    adder_sum.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
