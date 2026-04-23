#!/usr/bin/env python3
from __future__ import annotations

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from std_msgs.msg import Bool


class DebounceNode(Node):
    """
    Debounces a boolean signal.

    - Subscribes: /button_raw  (std_msgs/Bool)
    - Publishes:  /button_clean (std_msgs/Bool)

    The output changes only if the input stays in the new state
    for `debounce_ms` continuously.
    """

    def __init__(self) -> None:
        super().__init__("debounce_node")

        # Parameters (easy to tune without code changes)
        self.declare_parameter("debounce_ms", 200)
        self.declare_parameter("input_topic", "/button_raw")
        self.declare_parameter("output_topic", "/button_clean")
        self.declare_parameter("publish_on_start", True)

        debounce_ms = int(self.get_parameter("debounce_ms").value)
        self._debounce_duration = Duration(nanoseconds=debounce_ms * 1_000_000)

        input_topic = str(self.get_parameter("input_topic").value)
        output_topic = str(self.get_parameter("output_topic").value)

        self._pub = self.create_publisher(Bool, output_topic, 10)
        self._sub = self.create_subscription(
            Bool, input_topic, self._on_raw, 10)

        # State
        self._stable_value: bool = False            # current clean output
        self._candidate_value: bool | None = None   # pending new value
        self._candidate_since = None                # rclpy.time.Time or None

        # Timer to evaluate candidate stability
        self._timer = self.create_timer(0.02, self._on_timer)  # 50 Hz

        if bool(self.get_parameter("publish_on_start").value):
            self._publish_clean(self._stable_value)

        self.get_logger().info(
            f"Debounce running: {input_topic} -> {output_topic}, debounce={debounce_ms}ms"
        )

    def _on_raw(self, msg: Bool) -> None:
        raw = bool(msg.data)

        # If raw equals stable, cancel any candidate (we're back to stable)
        if raw == self._stable_value:
            self._candidate_value = None
            self._candidate_since = None
            return

        # If candidate is new or changed, start timing it
        if self._candidate_value is None or raw != self._candidate_value:
            self._candidate_value = raw
            self._candidate_since = self.get_clock().now()

    def _on_timer(self) -> None:
        if self._candidate_value is None or self._candidate_since is None:
            return

        now = self.get_clock().now()
        if (now - self._candidate_since) >= self._debounce_duration:
            # Candidate has been stable long enough — accept it
            self._stable_value = self._candidate_value
            self._candidate_value = None
            self._candidate_since = None
            self._publish_clean(self._stable_value)

    def _publish_clean(self, value: bool) -> None:
        out = Bool()
        out.data = value
        self._pub.publish(out)
        self.get_logger().info(f"button_clean => {value}")


def main() -> None:
    rclpy.init()
    node = DebounceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
