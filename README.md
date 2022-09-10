# EasyNeuralCoref
A thin wrapper on top of neuralcoref library from Huggingface for coreference resolution

## Reason
HuggingFace's neuralcoref is an excellent library, but I had to jump through a lot of hoops to get the dependency conflicts resolved. I have consolidated the requirements and made a thin wrapper on top of it.

```python
from easyneuralcoref import EasyNeuralCoref
nc = EasyNeuralCoref()
nc('Angela lives in Boston. She is quite happy in that city.')
'Angela lives in Boston. Angela is quite happy in Boston.'
```
