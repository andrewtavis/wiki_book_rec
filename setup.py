try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os

from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name="wikirec",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="0.2.2.2",
    author="Andrew Tavis McAllister",
    author_email="andrew.t.mcallister@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    description="Recommendation engine framework based on Wikipedia data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="new BSD",
    url="https://github.com/andrewtavis/wikirec",
)

on_rtd = os.environ.get("READTHEDOCS") == "True"
if on_rtd:
    install_requires = []
else:
    install_requires = [
        "pytest-cov",
        "numpy",
        "pandas",
        "nltk",
        "spacy",
        "stopwordsiso",
        "matplotlib",
        "seaborn",
        "gensim",
        "scikit-learn",
        "keras",
        "sentence-transformers",
        "tensorflow",
        "tqdm",
        "beautifulsoup4",
        "mwparserfromhell",
        "defusedxml",
    ]

if __name__ == "__main__":
    setup(**setup_args, install_requires=install_requires)
