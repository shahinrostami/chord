from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="plotapi",
    version="0.0.1",
    description="Python package for creating beautiful and interactive diagrams.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahinrostami/plotapi",
    author="Dr. Shahin Rostami",
    author_email="hello@shahinrostami.com",
    license="MIT",
    packages=["plotapi"],
    zip_safe=False,
)
