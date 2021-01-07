import os
import pathlib

from setuptools import find_packages, setup

# project root path
here = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

with open(str(here / 'README.md'), 'r') as f:
    readme = f.read()

setup(
    # Basic project description. Not really needed for a local-only project though.
    name='my_dummy_project',
    description='Dummy project',
    long_description=readme,
    author='Benjamin Rabier',
    # Everything in src/ will be installed
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_dirs=["src"],
    # Requirements
    python_requires='>=3.6,<4',  # Supported Python versions
    install_requires=[
        # Dependencies that will be installed when installing this project
        # Example:
        # tabulate>=0.8,<0.9
    ],
    license='MIT',
    zip_safe=False  # Pretty much always needed, don't remember exactly why though. :D
)
