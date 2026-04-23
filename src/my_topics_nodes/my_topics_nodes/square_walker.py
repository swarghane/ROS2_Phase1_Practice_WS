# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from std_msgs.msg import Int32, Float32


# class SquareWalker(Node):
#     def __init__(self) -> None:
#         super().__init__('square_walker')

#         self._pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
#         self._timer = self.create_timer(2.0, self.timer_callback)
#         self.state = "Move"

#     def timer_callback(self):
#         msg = Twist()
#         if self.state == "Move":
#             msg.linear.x = 2.0
#             msg.angular.z = 0.0
#             self.get_logger().info("Moving Straight...")
#             self.state = "TURN"  # Next time, we turn
#         else:
#             # Set rotation velocity (radians per second)
#             # 1.57 radians is roughly 90 degrees
#             msg.linear.x = 0.0
#             msg.angular.z = 1.57
#             self.get_logger().info("Turning 90 Degrees...")
#             self.state = "MOVE"  # Next time, we move straight

#         self._pub.publish(msg)


# def main(args=None):
#     rclpy.init(args=args)
#     square_walker = SquareWalker()
#     try:
#         rclpy.spin(square_walker)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         square_walker.destroy_node()
#         rclpy.shutdown()


# if __name__ == "__main__":
#     main()


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class SquareWalker(Node):
    def __init__(self) -> None:
        super().__init__('square_walker')
        # Ensure this matches 'ros2 topic list' exactly
        self._pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        # Fast timer for more responsive control
        self._timer = self.create_timer(1.0, self.timer_callback)

        self.step = 0

    def timer_callback(self):
        msg = Twist()

        # Simple logic: Steps 0, 2, 4 are straight. Steps 1, 3, 5 are turns.
        if self.step % 2 == 0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.get_logger().info("Moving...")
        else:
            msg.linear.x = 0.0
            msg.angular.z = 1.57  # 90 degrees in radians
            self.get_logger().info("Turning...")

        self._pub.publish(msg)
        self.step += 1


def main(args=None):
    rclpy.init(args=args)
    node = SquareWalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from turtlesim.msg import Pose  # You'll need to import the Pose message
# import math


# class PreciseSquare(Node):
#     def __init__(self):
#         super().__init__('precise_square')
#         self._pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

#         # Subscribe to the turtle's position and orientation
#         self._sub = self.create_subscription(
#             Pose, '/turtle1/pose', self.pose_callback, 10)

#         self.current_pose = None
#         self.target_theta = None
#         self.state = "MOVE"

#         # Timer now just triggers the state machine check
#         self._timer = self.create_timer(0.1, self.control_loop)

#     def pose_callback(self, msg):
#         self.current_pose = msg

#     def control_loop(self):
#         if self.current_pose is None:
#             return

#         msg = Twist()

#         if self.state == "MOVE":
#             # You could add logic here to move a specific distance (x, y)
#             # For now, let's just focus on the turn fix
#             msg.linear.x = 1.0
#             self._pub.publish(msg)
#             # Switch to turn after some time or distance
#             # Let's simplify and just focus on how to turn precisely

#         elif self.state == "TURN":
#             if self.target_theta is None:
#                 # Set target to current angle + 90 degrees
#                 self.target_theta = self.current_pose.theta + (math.pi / 2)

#             # Check if we reached the target (with a small margin of error)
#             error = self.target_theta - self.current_pose.theta

#             if abs(error) > 0.01:
#                 msg.angular.z = 0.5  # Slow turn for precision
#             else:
#                 msg.angular.z = 0.0
#                 self.target_theta = None
#                 self.state = "MOVE"

#             self._pub.publish(msg)


# def main(args=None):
#     rclpy.init(args=args)
#     node = PreciseSquare()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         node.destroy_node()
#         rclpy.shutdown()


# if __name__ == "__main__":
#     main()
