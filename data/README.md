# Data Directory

Este diretório contém os dados e modelos utilizados pela plataforma de IA conversacional.

## Estrutura

### models/
Contém os modelos de machine learning treinados:
- Modelos de processamento de linguagem natural
- Modelos de classificação de intenções
- Modelos de análise de sentimentos
- Modelos de geração de respostas

### datasets/
Contém os conjuntos de dados utilizados para treinamento:
- Dados de treinamento para NLP
- Datasets de conversas
- Dados históricos de interações
- Dados de avaliação e teste

## Formato dos Dados

### Conversas
```json
{
  "conversation_id": "uuid",
  "timestamp": "2025-09-15T19:50:00Z",
  "messages": [
    {
      "sender": "user",
      "message": "Olá, como você pode me ajudar?",
      "timestamp": "2025-09-15T19:50:00Z"
    },
    {
      "sender": "bot",
      "message": "Olá! Posso ajudá-lo com informações sobre nossa plataforma de IA conversacional.",
      "timestamp": "2025-09-15T19:50:01Z",
      "confidence": 0.95
    }
  ],
  "sentiment_analysis": {
    "overall_sentiment": "positive",
    "score": 0.8
  }
}
```

### Modelos
- Formato: `.pkl`, `.joblib`, `.h5`, `.pth`
- Metadados em arquivos JSON correspondentes
- Documentação de performance e métricas

## Segurança

⚠️ **Importante**: 
- Não armazene dados sensíveis ou pessoais
- Use anonimização quando necessário
- Mantenha backups dos modelos importantes

## Uso

Para carregar modelos:
```python
from backend.models.model_loader import ModelLoader

# Carregar modelo de NLP
nlp_model = ModelLoader.load_model('models/nlp_processor.pkl')

# Carregar dataset
dataset = ModelLoader.load_dataset('datasets/training_data.json')
```
