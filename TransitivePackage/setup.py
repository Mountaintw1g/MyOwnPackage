from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/Mountaintw1g/MyOwnPackage',
    author='Johan Bergqvist',
    author_email='scjbergqvist@gmail.com',

    py_modules=['my_pip_package'],
)