import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
import random


class SafetyServer(Node):
    def __init__(self) -> None:
        super().__init__("safety_server")

        self.srv_ = self.create_service(
            SetBool, "check_safety", self.status_callback)
        self.get_logger().info("Safety Server is now active and monitoring...")

    def status_callback(self, request, response):
        obj_dist = random.uniform(0, 5)

        # Logic check
        if obj_dist > 2.5:
            response.success = True
            response.message = f"Clear! Distance: {obj_dist:.2f}m"
        else:
            response.success = False
            response.message = f"STOP! Object at: {obj_dist:.2f}m"

        self.get_logger().info(
            f"Dist: {obj_dist:.2f}m | Response: {response.success}")

        return response


def main():
    rclpy.init()
    node = SafetyServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
