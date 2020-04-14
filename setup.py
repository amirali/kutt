from setuptools import setup

setup(
    name='kutt',
    version='1.2',
    author='Amirali Esfandiari',
    author_email='amiralinull@gmail.com',
    url='http://github.com/realamirali/kutt-cli',
    py_modules=['kutt'],
    install_requires=['fire', 'requests'],
    packages=['kutt'],
    package_dir={'kutt': 'kutt'},
    entry_points = '''
        [console_scripts]
        kutt=kutt.cli:main
    '''
)
