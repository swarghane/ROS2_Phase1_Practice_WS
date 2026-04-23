import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
import random


class SafetyClient(Node):
    def __init__(self) -> None:
        super().__init__("safety_client")

        self.client_ = self.create_client(SetBool, "check_safety")

        while not self.client_.wait_for_service(timeout_sec=0.1):
            self.get_logger().info(f'Service not available, waiting again...')

        self.timer_ = self.create_timer(2.0, self.timer_callback)
        self.get_logger().info("Safety Client node has been started.")

    def timer_callback(self):
        request = SetBool.Request()
        request.data = True

        self.get_logger().info("Sending request to Safety Server...")
        future = self.client_.call_async(request)

        # 6. Attach a callback to handle the response when it arrives
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()

            if response.success:
                self.get_logger().info(
                    f"Response received: [SAFE] -> {response.message}")

            else:
                self.get_logger().warn(
                    f"Response Received: [DANGER] -> {response.message}")

        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = SafetyClient()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
