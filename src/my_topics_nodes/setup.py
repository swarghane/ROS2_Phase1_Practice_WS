from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_topics_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,
         'launch'), ['launch/launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='swarghane',
    maintainer_email='swarghane@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_talker = my_topics_nodes.my_talker:main',
            'my_listener = my_topics_nodes.my_listener:main',
            'debouncer = my_topics_nodes.debouncer:main',
            'adder_gen = my_topics_nodes.adder_gen:main',
            'adder_sum = my_topics_nodes.adder_sum:main',
            'safety_mon = my_topics_nodes.safety_mon:main',
            'dist_monitor = my_topics_nodes.dist_monitor:main',
            'square_walker = my_topics_nodes.square_walker:main',
            'camera_pub = my_topics_nodes.camera_pub:main',
            'image_sub = my_topics_nodes.image_sub:main'
        ],
    },
)
