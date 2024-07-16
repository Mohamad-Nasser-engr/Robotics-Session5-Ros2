# INSTRUCTIONS:

# STEP 1: CLONING THE REPOSITORY

git clone git@github.com:Mohamad-Nasser-engr/Robotics-Session5-Ros2.git

# STEP 2: BUILDING THE ROS2 PACKAGE

cd Robotics-Session5-Ros2/session5_ros2_ws
#
colcon build

# STEP 3: RUN THE NODES INDIVIDUALLY

# First navigate to the 'src' directory
cd Robotics-Session5-Ros2/session5_ros2_ws/src

# Temperature publisher
ros2 run session5_assignment temperature_publisher

# Threshold subscriber
ros2 run session5_assignment threshold_subscriber

# Alert publisher
ros2 run session5_assignment alert_publisher

# Temperature logger
ros2 run session5_assignment temperature_logger

# STEP 4: RUN THE LAUNCH FILE

# Navigate to the 'launch' directory 
cd Robotics-Session5-Ros2/session5_ros2_ws/launch

ros2 launch Temperature_alert_launch.py

# NOTE: The 'temperature_log.txt' logger file created by the temperature logger node can be found inside the 'session5_ros2_ws' directory. 


