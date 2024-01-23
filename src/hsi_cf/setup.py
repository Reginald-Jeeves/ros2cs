from setuptools import find_packages, setup

package_name = 'hsi_cf'

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
    maintainer='adm.sof44944',
    maintainer_email='adm.sof44944@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cf_node = hsi_cf.cf_node:main',
            'cf_trial = hsi_cf.cf_trial:main',
            'cf_fly_test = hsi_cf.cf_fly_test:main',
            'emergency_landing = hsi_cf.emergency_landing:main',
            'cf_takeoff = hsi_cf.cf_phy_node:main',
            'cf_par_node = hsi_cf.cf_par_node:main'
        ],
    },
)
