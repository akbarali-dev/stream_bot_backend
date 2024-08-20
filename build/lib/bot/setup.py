from setuptools import setup, find_packages

setup(
    name='signals',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django>=3.2',
    ],
    include_package_data=True,
    description='A Django package for custom signals',
    author='Your Name',
    author_email='your.email@example.com',
)
