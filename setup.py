from setuptools import setup

setup(
    name="termflash",
    version="1.0.0",
    py_modules=["termflash"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "termflash=termflash:main",
        ],
    },
    author="Ryan Holben",
    description="A simple terminal utility to flash the screen and grab attention.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)
