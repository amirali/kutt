from setuptools import setup

setup(
    name='kutt',
    version='1.1.3',
    py_modules=['kutt'],
    install_requires = ['click', 'requests'],
    entry_points = '''
        [console_scripts]
        kutt=kutt:cli
    '''
)
