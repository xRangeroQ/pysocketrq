from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    data=f.read()

setup(
    name="testpysocketrq",
    version="0.3.0",
    author="xRangeroQ",
    description="A simple basic socket controller",
    packages=find_packages(),
    long_description=data,
    long_description_content_type="text/markdown"
)
