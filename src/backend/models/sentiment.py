#!/usr/bin/env python3
"""
Análise de Sentimentos - Implementação Básica

Este módulo contém a classe SentimentAnalyzer que realiza uma análise
de sentimentos simplificada em texto.

Autor: Gabriel Demetrios Lafis
Data: 16 de setembro de 2025
Versão: 1.1

Usage:
    from models.sentiment import SentimentAnalyzer
    
    analyzer = SentimentAnalyzer()
    result = analyzer.analyze("Estou muito feliz hoje!")
    print(result)
"""

class SentimentAnalyzer:
    """
    Classe para análise de sentimentos em texto.
    
    Realiza uma classificação básica de sentimentos (positivo, negativo, neutro)
    baseada em palavras-chave.
    """
    
    def __init__(self):
        """
        Inicializa o analisador de sentimentos.
        """
        pass
    
    def analyze(self, text: str) -> str:
        """
        Analisa o sentimento de um texto.
        
        Args:
            text (str): O texto a ser analisado
            
        Returns:
            str: O sentimento classificado (positivo, negativo, neutro)
            
        Example:
            >>> analyzer = SentimentAnalyzer()
            >>> result = analyzer.analyze("Estou muito feliz hoje!")
            >>> print(result)
            positivo
        """
        text_lower = text.lower()
        if "bom" in text_lower or "ótimo" in text_lower or "excelente" in text_lower or "feliz" in text_lower or "great" in text_lower or "good" in text_lower or "happy" in text_lower:
            return "positivo"
        elif "ruim" in text_lower or "péssimo" in text_lower or "triste" in text_lower or "chateado" in text_lower or "bad" in text_lower or "sad" in text_lower:
            return "negativo"
        else:
            return "neutro"

