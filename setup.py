from setuptools import setup

setup(
    name="systeminfo",
    version="0.1",
    description="Basic system info",
    url="",
    author="louisgh",
    author_email="louisgateshardiman@gmail.com",
    licence="GPL3",
    packages=['systeminfo'],
    entry_points={
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
  
)