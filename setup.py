from setuptools import setup
from os import path
import io
import platform

# membuka file README
with open("README.md") as file_readme:
    readme = file_readme.read()

# setup nama project
setup(
    name="OpenSeries",
    version="1.0.0",
    description="library untuk membantu temen-temen SMA/SMK/Sederajat",
    long_description=str(readme),
    url="https://github.com/bellshade/OpenSeries",
    author="bellshade, wpu, kelas terbuka",
    packages=["OpenSeries"],
    python_requires=">=3.10",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    license="MIT License",
    project_urls={
        "Bug Reports": "https://github.com/bellshade/OpenSeries/issues",
        "Source": "https://github.com/bellshade/OpenSeries",
    },
)
