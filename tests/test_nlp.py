import unittest
import sys
import os

# Adicionar o diretório src ao PATH para que as importações funcionem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from backend.models.sentiment import SentimentAnalyzer
from backend.models.nlp_processor import NLPProcessor

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_positive_sentiment(self):
        self.assertEqual(self.analyzer.analyze("Estou muito feliz hoje!"), "positivo")
        self.assertEqual(self.analyzer.analyze("This is a great project."), "positivo")
        self.assertEqual(self.analyzer.analyze("Excelente trabalho!"), "positivo")

    def test_negative_sentiment(self):
        self.assertEqual(self.analyzer.analyze("Estou muito triste com isso."), "negativo")
        self.assertEqual(self.analyzer.analyze("This is a bad idea."), "negativo")
        self.assertEqual(self.analyzer.analyze("Péssimo resultado."), "negativo")

    def test_neutral_sentiment(self):
        self.assertEqual(self.analyzer.analyze("O céu é azul."), "neutro")
        self.assertEqual(self.analyzer.analyze("The cat sat on the mat."), "neutro")
        self.assertEqual(self.analyzer.analyze("Isso é uma cadeira."), "neutro")

class TestNLPProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = NLPProcessor()

    def test_process_message_positive(self):
        result = self.processor.process_message("Adorei o novo recurso, muito bom!")
        self.assertIn("Mensagem processada: Adorei o novo recurso, muito bom! Sentimento: positivo", result)

    def test_process_message_negative(self):
        result = self.processor.process_message("Não gostei, achei ruim.")
        self.assertIn("Mensagem processada: Não gostei, achei ruim. Sentimento: negativo", result)

    def test_process_message_neutral(self):
        result = self.processor.process_message("Isso é apenas um teste.")
        self.assertIn("Mensagem processada: Isso é apenas um teste. Sentimento: neutro", result)

if __name__ == '__main__':
    unittest.main()

