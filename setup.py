from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="chord",
    version="0.10.0",
    description="Python package for creating beautiful interactive Chord Diagrams.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahinrostami/chord",
    author="Dr. Shahin Rostami",
    author_email="hello@shahinrostami.com",
    license="AGPLv3+",
    packages=["chord"],
    zip_safe=False,
)
