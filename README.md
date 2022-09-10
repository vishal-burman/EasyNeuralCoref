# EasyNeuralCoref
A thin wrapper on top of neuralcoref library from Huggingface for coreference resolution

## Reason
HuggingFace's neuralcoref is an excellent library, but I had to jump through a lot of hoops to get the dependency conflicts resolved. I have consolidated the requirements and made a thin wrapper on top of it.

## Instructions to install
1. Install miniconda from here: https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links
2. Create a new conda environment with python=3.7
   ```bash
   conda create --name coref python=3.7
   ```
3. Activate the newly created conda environment
   ```bash
   conda activate coref
   ```
4. Install the package EasyNeuralCoref
   ```bash
   pip install git+https://github.com/vishal-burman/EasyNeuralCoref.git
   ```

## Usage
```python
from easyneuralcoref import EasyNeuralCoref
nc = EasyNeuralCoref()
nc('Angela lives in Boston. She is quite happy in that city.')
# 'Angela lives in Boston. Angela is quite happy in Boston.'
```
