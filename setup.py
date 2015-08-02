#!/usr/bin/env python3

from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(name='cotest',
          description='concurrent code testing framework',
          author="Lasse Schuirmann",
          author_email='lasse.schuirmann@gmail.com',
          maintainer='Lasse Schuirmann',
          maintainer_email='lasse.schuirmann@gmail.com',
          platforms='any',
          packages=find_packages(exclude=["build.*", ".*tests.*", ".*tests"]),
          install_requires=["setuptools"],
          license="AGPL v3",
          long_description="A simple concurrent code testing utility.",
          entry_points={"console_scripts": ["cotest = cotest:main"]})
