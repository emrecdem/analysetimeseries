#from setuptools import setup
import setuptools

def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(name='analysetimeseries',
      version='0.0.0.dev1',
      description='A tool to analyse time series',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/emrecdem/analysetimeseries',
      keywords='analysis, conversion',
      author='V. van Hees, B.L. de Vries',
      author_email='b.devries@esciencecenter.nl',
      classifiers=(
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
      ),
      packages=setuptools.find_packages(),
      install_requires=['numpy', 'pandas'],
      zip_safe=True)