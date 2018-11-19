from setuptools import setup

setup(
    name='kutt',
    version='1.1.4',
    author='Amirali Esfandiari',
    author_email='amiralinull@gmail.com',
    url='http://github.com/univa64/kutt-cli',
    py_modules=['kutt'],
    install_requires=['click', 'requests'],
    packages=['kutt'],
    package_dir={'kutt': 'kutt'},
    entry_points = '''
        [console_scripts]
        kutt=kutt.cli:cli
    '''
)
