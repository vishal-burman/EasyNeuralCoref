from setuptools import setup, find_packages

base_packages = open("requirements.txt").read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easyneuralcoref",
    packages=find_packages(exclude=["tests"]),
    version="0.0.1",
    author="Vishal Burman",
    author_email="vishal.a.burman23@gmail.com",
    description="An easy to use thin wrapper on top of neuralcoref library from Huggingface for coreference resolution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishal-burman/EasyNeuralCoref",
    keywords="nlp coreference-resolution",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=base_packages,
    python_requires="~=3.7",
)
