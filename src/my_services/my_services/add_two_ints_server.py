import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MinimalServer(Node):
    def __init__(self) -> None:
        super().__init__("add_two_ints_server")

        self.srv_ = self.create_service(
            AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info("Server is ready to add some integers!")

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b

        self.get_logger().info(
            f'Incoming request\na: {request.a} b: {request.b}')
        self.get_logger().info(f'Sending back response: {response.sum}')

        return response


def main():
    rclpy.init()
    node = MinimalServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
