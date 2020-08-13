import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path('Downloads/New_data_file/Unfollow_bot/twitter-unfollow_python-library/setup.py').parent

# The text of the README file
README = ("README.md")

# This call to setup() does all the work
setup(
    name="twitter unfollow",
    version="1.0.0",
    description="build an unfollow bot",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com",
    author="Emeka Boris",
    author_email="borisphilosophy@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["unfollow"],
    include_package_data=True,
    install_requires=["tweepy"],
    entry_points={
        "console_scripts": [
            "unfollow_bot=__main__:main",
        ]
    },
)