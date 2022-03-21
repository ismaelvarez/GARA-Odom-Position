from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['odom_to_position'],
    package_dir={'': 'include'}
)
setup(**d)
