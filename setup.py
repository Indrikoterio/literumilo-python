# Setup module for literumilo package.
# Cleve (Klivo) Lendon, 2020-05

import setuptools

with open("README.md", "r") as fin:
    long_description = fin.read()

setuptools.setup(
    name = "literumilo",
    version = "1.0.1",
    author = "Cleve (Klivo) Lendon",
    author_email = "indriko@yahoo.com",
    description = "A spell checker and morphological analyzer for Esperanto.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/Indrikoterio/literumilo",
    packages = setuptools.find_packages(),
    package_data = {'tests': ['test.txt'], 'data': ['vortaro.tsv', 'example.txt']},
    include_package_data = True,
    py_modules = ['literumilo', 'literumilo_check_word', 'literumilo_ending', \
                             'literumilo_entry', 'literumilo_load', 'literumilo_morpheme_list', \
                             'literumilo_scan_morphemes', 'literumilo_suffix', 'literumilo_utils',  \
                             'example'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.5',
)
