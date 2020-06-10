import re
from setuptools import setup

changes = open('CHANGES.txt').read()
version = re.findall("__version__ = '(.*)'", open(version_file).read())[0]
try:
    version = __import__('utile').git_version(version)
except ImportError:
    pass

setup(
    long_description=readme + '\n\n' + changes,
)
