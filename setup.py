from setuptools import setup, find_packages
from photon_geocoder import __version__, __author__

with open('requirements.txt', encoding='utf-8') as f:
    required = f.read().splitlines()

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='photon_geocoder',
    version=__version__,
    author=__author__,
    description='A Python wrapper for the Photon geocoder',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/binoalien/photon-geocoder',
    packages=find_packages(),
    install_requires=required,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
    include_package_data=True,
    keywords='geocoding, OSM, OpenStreetMap, address, mapping',
)
