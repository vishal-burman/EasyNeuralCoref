import unittest
from easyneuralcoref import EasyNeuralCoref

class EasyNeuralCorefTestCase(unittest.TestCase):
    def setUp(self,):
        self.nc = EasyNeuralCoref()

    def test_coref_resolved_text(self,):
        text = "Alice is living in Boston. She is loving that city."
        text_r = self.nc(text)
        self.assertEqual(text_r, "Alice is living in Boston. Alice is loving Boston.")

    def tearDown(self,):
        del self.nc
