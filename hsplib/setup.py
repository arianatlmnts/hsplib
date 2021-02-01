from setuptools import find_packages, setup

setup(
    name='hsplib',
    packages=find_packages(include=['hsplib']),
    version='0.1.0',
    description='HSP graph for instance-based learning',
    author='Ariana Talamantes',
    url='https://github.com/arianatlmnts/hsplib.git',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
