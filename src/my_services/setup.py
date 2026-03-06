from setuptools import find_packages, setup

package_name = 'my_services'

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
            'add_two_ints_server = my_services.add_two_ints_server:main',
            'add_two_ints_client = my_services.add_two_ints_client:main',
            'dist_safety_server = my_services.dist_safety_server:main',
            'dist_safety_client = my_services.dist_safety_client:main',
            'static_broadcaster = my_services.static_broadcaster:main',
            'dynamic_tf_publisher = my_services.dynamic_tf_publisher:main',
        ],
    },
)
