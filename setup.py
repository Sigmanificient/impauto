import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="impauto",
    version="1.1.0",
    description="Make your life easier with automated inputs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Edhyjox/impauto",
    author="Sigmanificient",
    author_email="Edhyjox@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["impauto"],
    include_package_data=True,
    install_requires=[]
)
