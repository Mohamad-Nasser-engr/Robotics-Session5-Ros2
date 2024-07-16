import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertPublisher(Node):

    def __init__(self):
        super().__init__('alert_publisher')
        # create subscribtion to the topic that is getting data from the threshold publisher
        self.subscription = self.create_subscription(String,'alert_trigger', self.alert_trigger_callback, 10)

        # create publisher to new topic called alert
        self.publisher_ = self.create_publisher(String, 'alert', 10)

    def alert_trigger_callback(self, msg):
        # obtain message from the alert trigger topic
        alert_message = msg.data
        self.get_logger().info(f'Received alert trigger: {alert_message}')

        # create new alert message to be published
        alert_msg = String()
        alert_msg.data = f'Alert Published: {alert_message}'
        self.publisher_.publish(alert_msg)
        self.get_logger().info(f'Published alert: {alert_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = AlertPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
