from setuptools import find_packages, setup

package_name = 'session5_assignment'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mohamad',
    maintainer_email='mohamadnasser.engr@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_publisher = session5_assignment.Temperature_publisher:main',
            'threshold_subscriber = session5_assignment.Threshold_subscriber:main',
            'alert_publisher = session5_assignment.Alert_publisher:main'
        ],
    },
)
