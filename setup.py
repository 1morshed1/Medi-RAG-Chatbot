from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Medi-RAG",
    version="1.2",
    author="Morshed",
    packages=find_packages(),
    install_requires = requirements,
)