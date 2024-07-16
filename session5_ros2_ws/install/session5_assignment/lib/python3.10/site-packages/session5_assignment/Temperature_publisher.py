import rclpy
from std_msgs.msg import Float32
from rclpy.node import Node
import random

class TemperaturePublisher(Node):

    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher = self.create_publisher(Float32, 'temperature', 10)
        timer_period = 2
        self.timer = self.create_timer(timer_period,self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(-20, 70)
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data: .2f} C')

def main(args = None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


