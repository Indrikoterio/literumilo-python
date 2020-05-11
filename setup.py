# Setup module for literumilo.
# Cleve (Klivo) Lendon, 2020-05

import setuptools

with open("README.md", "r") as fin:
    long_description = fin.read()

setuptools.setup(
    name = "literumilo",
    version = "1.0",
    author = "Cleve (Klivo) Lendon",
    author_email = "indriko@yahoo.com",
    description = "A spell checker and morphological analyzer for Esperanto.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/Indrikoterio/literumilo",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.5',
)
