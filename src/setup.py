from setuptools import setup

setup(
    name='Steam-Profile-Switcher',
    version='1.0.1',
    packages=['tkinter', 'js2py'],
    package_dir={'': 'src'},
    url='https://github.com/ZacDair/Steam-Profile-Switcher',
    license='',
    author='Zac Dair',
    author_email='zacdair@gmail.com',
    description='Steam Profile Switching application allows the user to preset profiles (Steam Name, Bio, Avatar) these profiles can then be switched to instead of requiring the manual change of each field in Steam.'
)
