import spacy
import neuralcoref

class EasyNeuralCoref:
    def __init__(self,):
        self.nlp = spacy.load("en_core_web_sm")
        neuralcoref.add_to_pipe(self.nlp)

    def _coref_text_resolve(text: str) -> str:
        doc = self.nlp(text)
        return doc._.coref_resolved

    def __call__(self, text: str) -> str:
        if not text:
            raise ValueError(f"Not a valid text")
        return _coref_text_resolve(text)
