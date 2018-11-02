from setuptools import setup

setup(
    name='kutt',
    version='1.0',
    py_modules=['kutt'],
    install_requires = ['click', 'requests'],
    entry_points = '''
        [console_scripts]
        kutt=kutt:cli
    '''
)
