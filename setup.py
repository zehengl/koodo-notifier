from setuptools import setup, find_packages

from koodo_notifier import VERSION

setup(
    name="koodo-notifier",
    version=VERSION,
    packages=find_packages(),
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["boto3", "pytest", "rollbar", "selenium", "urllib3==1.24.3"],
    test_suite="tests",
    author="Zeheng Li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng Li",
    maintainer_email="imzehengl@gmail.com",
    description="A Koodo Usage Notifier",
    license="MIT",
    url="https://github.com/zehengl/koodo-notifier",
)
