"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='visualisations_pckg',  # Required
    version='0.1',  # Required
    description='A visualisation package for bar charts and histograms',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    #url='https://github.com/pypa/sampleproject',  # Optional
    author='Jochen Ruland',  # Optional
    author_email='jochenhgruland@gmail.com',  # Optional
    keywords='visualisation', 'bar chart', 'histogram'  # Optional
    packages=['visualisation_pckg'],  # Required
    zip_safe = False
)
