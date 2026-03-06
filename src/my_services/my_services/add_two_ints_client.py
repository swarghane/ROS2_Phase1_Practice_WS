import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import random


class MinimalClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")

        self.client = self.create_client(AddTwoInts, "add_two_ints")

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        request = AddTwoInts.Request()
        request.a = random.randint(0, 100)
        request.b = random.randint(0, 100)

        # Call asynchronously so the node doesn't block while waiting
        self.get_logger().info(f"Requesting: {request.a} + {request.b}")
        future = self.client.call_async(request)

        # Use a callback to handle the result when it returns
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Result from server: {response.sum}')
        except Exception as e:
            self.get_logger().error(f'Service call failed %r' % (e,))


def main():
    rclpy.init()
    node = MinimalClient()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
