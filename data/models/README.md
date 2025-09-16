# Data Models Directory

## 📋 Descrição

Este diretório contém todos os modelos de Machine Learning e Inteligência Artificial treinados e pré-processados da plataforma conversacional. Inclui modelos para processamento de linguagem natural, classificação de texto, análise de sentimentos e geração de respostas.

## 🤖 Tipos de Modelos

### Modelos de Linguagem
- **BERT/RoBERTa**: Modelos transformer para compreensão de contexto
- **GPT**: Modelos generativos para criação de respostas
- **T5**: Modelos text-to-text para diversas tarefas
- **LSTM/GRU**: Redes neurais recorrentes para sequências

### Modelos de Classificação
- **Intent Classification**: Classificação de intenções do usuário
- **Sentiment Analysis**: Análise de sentimentos
- **Topic Modeling**: Modelagem de tópicos
- **Spam Detection**: Detecção de spam

### Modelos de Embeddings
- **Word2Vec**: Embeddings de palavras
- **FastText**: Embeddings com informação de subpalavras
- **Sentence-BERT**: Embeddings de frases
- **Universal Sentence Encoder**: Embeddings universais

## 📁 Estrutura Esperada

```
models/
├── nlp/
│   ├── bert_intent_classifier.pkl
│   ├── sentiment_analyzer.pkl
│   ├── entity_extractor.pkl
│   └── response_generator.pkl
├── embeddings/
│   ├── word2vec_300d.bin
│   ├── fasttext_pt.bin
│   ├── sentence_bert.pkl
│   └── use_multilingual.pkl
├── classification/
│   ├── intent_svm.pkl
│   ├── sentiment_nb.pkl
│   ├── topic_lda.pkl
│   └── spam_rf.pkl
├── transformers/
│   ├── bert-base-portuguese/
│   ├── gpt2-portuguese/
│   └── t5-small-portuguese/
└── metadata/
    ├── model_registry.json
    ├── version_info.json
    └── performance_metrics.json
```

## 📊 Metadados dos Modelos

### Registro de Modelos
```json
{
  "models": {
    "intent_classifier": {
      "name": "BERT Intent Classifier",
      "version": "1.2.0",
      "type": "classification",
      "framework": "transformers",
      "accuracy": 0.94,
      "f1_score": 0.92,
      "created_at": "2025-09-15T10:30:00Z",
      "file_path": "nlp/bert_intent_classifier.pkl",
      "model_size_mb": 420,
      "tags": ["intent", "bert", "portuguese"]
    },
    "sentiment_analyzer": {
      "name": "Sentiment Analysis Model",
      "version": "2.1.0",
      "type": "classification",
      "framework": "scikit-learn",
      "accuracy": 0.89,
      "f1_score": 0.87,
      "created_at": "2025-09-10T14:15:00Z",
      "file_path": "nlp/sentiment_analyzer.pkl",
      "model_size_mb": 15,
      "tags": ["sentiment", "svm", "portuguese"]
    }
  }
}
```

### Informações de Performance
```json
{
  "metrics": {
    "intent_classifier": {
      "accuracy": 0.94,
      "precision": 0.93,
      "recall": 0.91,
      "f1_score": 0.92,
      "confusion_matrix": "base64_encoded_matrix",
      "classification_report": "...",
      "inference_time_ms": 45,
      "memory_usage_mb": 512
    }
  },
  "benchmarks": {
    "test_dataset_size": 10000,
    "evaluation_date": "2025-09-15T16:00:00Z",
    "hardware": "CPU: Intel i7, RAM: 16GB"
  }
}
```

## 💾 Formatos Suportados

### Modelos Serializados
- **Pickle (.pkl)**: Modelos scikit-learn, NLTK
- **JobLib (.joblib)**: Modelos grandes do scikit-learn
- **HDF5 (.h5)**: Modelos Keras/TensorFlow
- **PyTorch (.pth/.pt)**: Modelos PyTorch
- **ONNX (.onnx)**: Modelos otimizados para inferência

### Modelos de Linguagem
- **Transformers**: Modelos do Hugging Face
- **Tokenizers**: Tokenizadores treinados
- **Vocabularies**: Vocabulários customizados
- **Embeddings**: Vetores pré-treinados

## 🛠️ Carregamento de Modelos

### Exemplo de Carregador
```python
import pickle
import joblib
import json
from pathlib import Path
from typing import Any, Dict, Optional

class ModelLoader:
    def __init__(self, models_dir: str = "./data/models"):
        self.models_dir = Path(models_dir)
        self.registry = self._load_registry()
        self.loaded_models = {}
    
    def _load_registry(self) -> Dict:
        registry_path = self.models_dir / "metadata" / "model_registry.json"
        with open(registry_path, 'r') as f:
            return json.load(f)
    
    def load_model(self, model_name: str) -> Any:
        if model_name in self.loaded_models:
            return self.loaded_models[model_name]
        
        if model_name not in self.registry["models"]:
            raise ValueError(f"Model {model_name} not found in registry")
        
        model_info = self.registry["models"][model_name]
        file_path = self.models_dir / model_info["file_path"]
        
        # Detectar formato e carregar apropriadamente
        if file_path.suffix == '.pkl':
            model = pickle.load(open(file_path, 'rb'))
        elif file_path.suffix == '.joblib':
            model = joblib.load(file_path)
        else:
            raise ValueError(f"Unsupported model format: {file_path.suffix}")
        
        self.loaded_models[model_name] = model
        return model
    
    def get_model_info(self, model_name: str) -> Dict:
        return self.registry["models"].get(model_name, {})
    
    def list_models(self) -> list:
        return list(self.registry["models"].keys())

# Uso
loader = ModelLoader()
intent_model = loader.load_model("intent_classifier")
sentiment_model = loader.load_model("sentiment_analyzer")
```

## 📄 Versionamento

### Convenções de Nomeação
```
{model_name}_{version}_{date}.{extension}

Exemplos:
- intent_classifier_v1.2.0_20250915.pkl
- sentiment_bert_v2.1.0_20250910.h5
- word2vec_v1.0.0_20250901.bin
```

### Controle de Versão
- **Major**: Mudanças na arquitetura do modelo
- **Minor**: Retreinamento com novos dados
- **Patch**: Correções e otimizações

## 🚀 Deploy & Serving

### Otimização para Produção
- **Quantização**: Reduzir precisão para acelerar inferência
- **Pruning**: Remover neurônios desnecessários
- **Distillação**: Criar modelos menores a partir de grandes
- **Batching**: Processar múltiplas entradas simultaneamente

### Monitoramento
- **Model Drift**: Detectar degradação de performance
- **Data Drift**: Monitorar mudanças nos dados de entrada
- **A/B Testing**: Comparar versões de modelos
- **Metrics Tracking**: Acompanhar métricas em tempo real

## 🔒 Segurança

### Backup & Recovery
- **Backup automático**: Cópias regulares dos modelos
- **Versionamento**: Manter histórico de versões
- **Checksums**: Verificar integridade dos arquivos
- **Encryption**: Criptografar modelos sensíveis

### Acesso
- **Permissões**: Controle de acesso aos modelos
- **Auditoria**: Log de uso e modificações
- **Validação**: Verificar integridade antes do carregamento

---

*Desenvolvido para a Plataforma de IA Conversacional*
