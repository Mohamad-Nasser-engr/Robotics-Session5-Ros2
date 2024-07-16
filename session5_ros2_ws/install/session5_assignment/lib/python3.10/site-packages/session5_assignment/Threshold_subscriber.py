import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class ThresholdSubscriber(Node):

    def __init__(self):
        super().__init__('threshold_subscriber')
        #create subscriber for the same topic that will recieve data from the temperature publisher
        self.subscription = self.create_subscription(Float32,'temperature', self.temperature_callback, 10)

        # create publisher 
        self.publisher  = self.create_publisher(String, 'alert_trigger', 10)
        self.threshold = 30.0  #threshold

    def temperature_callback(self, msg):
        # get data from the temperature topic
        temperature = msg.data
        self.get_logger().info(f'Received temperature: {temperature:.2f} °C')

        #check threshold
        if temperature > self.threshold:
            alert_msg = String()
            alert_msg.data = f'Alert! Temperature exceeded threshold: {temperature:.2f} °C'
            self.publisher.publish(alert_msg)
            self.get_logger().info(f'Published alert: {alert_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ThresholdSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
