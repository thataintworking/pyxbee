from distutils.core import setup

packages = [
    'xbee',
    'xbee.tests',
    'xbee.helpers',
    'xbee.helpers.dispatch',
    'xbee.helpers.dispatch.tests',
]

setup(
    name='pyxbee',
    version='0.1',
    author='Ron Smith',
    author_email='ron.smith@thataintworking.com',
    packages=packages,
    scripts=[],
    url='https://github.com/thataintworking/pyxbee',
    license='LICENSE.txt',
    description='A refactored Python library for XBee communication',
    long_description=open('README.rst').read(),
    requires=['pyserial'],
    provides=packages,
)
