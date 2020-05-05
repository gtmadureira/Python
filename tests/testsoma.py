import unittest
from hf_src.main import soma


class TestSoma(unittest.TestCase):
    def test_retorno_soma_15_30(self):
        self.assertEqual(soma(15, 30), 45)
