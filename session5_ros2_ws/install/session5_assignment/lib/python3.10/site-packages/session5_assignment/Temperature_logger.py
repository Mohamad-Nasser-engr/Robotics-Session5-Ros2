import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import os

class TemperatureLogger(Node):

    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(Float32,'temperature',self.temperature_callback,10)

        # Set up log file
        log_directory = os.path.expanduser('~/Inmind/Robotics-Session5-Ros2/session5_ros2_ws')
        self.log_file_path = os.path.join(log_directory, 'temperature_log.txt')
        self.get_logger().info(f'Logging temperature data to {self.log_file_path}')
        
        # Open the file in append mode
        self.log_file = open(self.log_file_path, 'a')

    def temperature_callback(self, msg):
        temperature = msg.data
        log_entry = f'Temperature: {temperature:.2f} °C\n'
        self.log_file.write(log_entry)
        self.get_logger().info(log_entry.strip())

    # make sure to close the file before killing the node
    def destroy_node(self):
        self.log_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
