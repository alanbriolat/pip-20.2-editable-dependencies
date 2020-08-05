from setuptools import setup, find_packages

setup(
    name="package-b",
    version="0.1",
    packages=find_packages(),
    install_requires=["package-a"],
)