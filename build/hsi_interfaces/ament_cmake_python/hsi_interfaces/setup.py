from setuptools import find_packages
from setuptools import setup

setup(
    name='hsi_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('hsi_interfaces', 'hsi_interfaces.*')),
)
