#!/usr/bin/env python3
"""
Processador de Linguagem Natural (NLP) - Implementação Aprimorada

Este módulo contém a classe NLPProcessor que integra funcionalidades
de processamento de linguagem natural, incluindo análise de sentimentos.

Autor: Gabriel Demetrios Lafis
Data: 16 de setembro de 2025
Versão: 1.1

Usage:
    from models.nlp_processor import NLPProcessor
    
    processor = NLPProcessor()
    result = processor.process_message("Olá, como posso ajudar?")
    print(result)
"""

from .sentiment import SentimentAnalyzer

class NLPProcessor:
    """
    Classe para processamento de linguagem natural.
    
    Integra análise de sentimentos e serve como base para futuras expansões
    com extração de entidades, classificação de intenções, etc.
    """
    
    def __init__(self):
        """
        Inicializa o processador NLP e o analisador de sentimentos.
        """
        self.sentiment_analyzer = SentimentAnalyzer()
    
    def process_message(self, message: str) -> str:
        """
        Processa uma mensagem de texto, incluindo análise de sentimento.
        
        Args:
            message (str): A mensagem de texto a ser processada
            
        Returns:
            str: Resultado do processamento, incluindo o sentimento analisado.
            
        Example:
            >>> processor = NLPProcessor()
            >>> result = processor.process_message("Estou muito feliz hoje!")
            >>> print(result)
            Mensagem processada: Estou muito feliz hoje! Sentimento: positivo
        """
        if message is None:
            return "Mensagem processada:  Sentimento: neutro"
        sentiment = self.sentiment_analyzer.analyze(message)
        return f"Mensagem processada: {message} Sentimento: {sentiment}"

