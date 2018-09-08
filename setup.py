from setuptools import setup, find_packages

setup(
    name='koodo-notifier',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['boto3', 'selenium'],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'rollbar'
    ],
    test_suite='tests',
    author='Zeheng Li',
    author_email='imzehengl@gmail.com',
    maintainer='Zeheng Li',
    maintainer_email='imzehengl@gmail.com',
    description='A koodo usage notifier',
    license='MIT',
    url='https://github.com/zehengl/koodo-notifier',
)
