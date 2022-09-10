from setuptools import setup, find_packages

base_packages = [
    "blis==0.2.4",
    "boto3==1.24.8",
    "botocore==1.27.8",
    "certifi==2022.5.18.1",
    "charset-normalizer==2.0.12",
    "cymem==2.0.6",
    "en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz",
    "idna==3.3",
    "jmespath==1.0.0",
    "jsonschema==2.6.0",
    "murmurhash==1.0.7",
    "neuralcoref==4.0",
    "numpy==1.21.6",
    "plac==0.9.6",
    "preshed==2.0.1",
    "python-dateutil==2.8.2",
    "requests==2.28.0",
    "s3transfer==0.6.0",
    "six==1.16.0",
    "spacy==2.1.0",
    "srsly==1.0.5",
    "thinc==7.0.8",
    "tqdm==4.64.0",
    "urllib3==1.26.9",
    "wasabi==0.9.1",
    ]

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
