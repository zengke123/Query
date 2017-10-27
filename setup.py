from setuptools import setup
setup(
    name='query',
    version='0.11',
    py_modules=['train', 'movie', 'weather', 'query','urllib3'],
    install_requires=['requests', 'docopt', 'prettytable', 'colorama', 'bs4',],
    entry_points={
        'console_scripts': ['query=query:query'],}
)