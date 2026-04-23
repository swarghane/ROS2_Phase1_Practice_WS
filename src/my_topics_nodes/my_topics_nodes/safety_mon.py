import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class SensorData(Node):
    def __init__(self) -> None:
        super().__init__("sensor_data")

        self.declare_parameter("safety_topic", '/sensor_distance')
        safety_topic = str(self.get_parameter("safety_topic").value)

        self._pub = self.create_publisher(Float32, safety_topic, 10)
        self._timer = self.create_timer(0.5, self.safety_timer)

    def safety_timer(self):
        msg = Float32()
        msg.data = random.uniform(0, 2)
        self._pub.publish(msg)
        self.get_logger().info(f"Object is {msg.data} meters away")


def main(args=None):
    rclpy.init(args=args)
    sensor_data = SensorData()
    try:
        rclpy.spin(sensor_data)
    except KeyboardInterrupt:
        pass
    finally:
        sensor_data.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
