# Backend Utils Directory

## 📋 Descrição

Este diretório contém utilitários e funções auxiliares (helpers) que suportam a funcionalidade principal da plataforma conversacional. Inclui ferramentas para configuração, logs, validação, cache e outras utilidades transversais.

## 🛠️ Utilitários Principais

### Configuração
- **ConfigManager**: Gerenciamento centralizado de configurações
- **EnvironmentLoader**: Carregamento de variáveis de ambiente
- **DatabaseConfig**: Configuração de banco de dados
- **ModelConfig**: Configuração de modelos de IA

### Logs & Monitoramento
- **Logger**: Sistema de logs estruturado
- **Metrics**: Coleta de métricas de performance
- **Tracer**: Rastreamento de requisições
- **HealthChecker**: Verificação de saúde do sistema

### Validação & Formatação
- **TextProcessor**: Processamento e limpeza de texto
- **DataValidator**: Validação de dados de entrada
- **ResponseFormatter**: Formatação de respostas
- **DateTimeHelper**: Utilitários de data e hora

## 📁 Estrutura Esperada

```
utils/
├── __init__.py
├── config.py           # Gerenciamento de configuração
├── logger.py           # Sistema de logs
├── validators.py       # Validação de dados
├── formatters.py       # Formatação de dados
├── cache.py            # Gerenciamento de cache
├── database.py         # Utilitários de banco de dados
├── security.py         # Utilitários de segurança
├── metrics.py          # Coleta de métricas
└── helpers.py          # Funções auxiliares gerais
```

## 🛠️ Implementação

### Exemplo de Configuração
```python
import os
from typing import Dict, Any

class ConfigManager:
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        return {
            'DEBUG': os.getenv('DEBUG', 'False').lower() == 'true',
            'SECRET_KEY': os.getenv('SECRET_KEY', 'dev-key'),
            'DATABASE_URL': os.getenv('DATABASE_URL', 'sqlite:///app.db'),
            'REDIS_URL': os.getenv('REDIS_URL', 'redis://localhost:6379'),
            'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
            'MODEL_PATH': os.getenv('MODEL_PATH', './models'),
        }
    
    def get(self, key: str, default=None):
        return self.config.get(key, default)

# Uso
config = ConfigManager()
debug_mode = config.get('DEBUG')
```

### Exemplo de Logger
```python
import logging
import json
from datetime import datetime

class StructuredLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self._setup_logger()
    
    def _setup_logger(self):
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def log_request(self, method: str, path: str, 
                   status_code: int, duration: float):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'type': 'request',
            'method': method,
            'path': path,
            'status_code': status_code,
            'duration_ms': duration * 1000
        }
        self.logger.info(json.dumps(log_data))
```

## 🔒 Segurança

### Utilitários de Segurança
- **Hash functions**: Hashing seguro de senhas
- **Token generation**: Geração de tokens JWT
- **Input sanitization**: Sanitação de entradas
- **Rate limiting**: Controle de taxa

### Exemplo
```python
import hashlib
import secrets
from typing import str

class SecurityUtils:
    @staticmethod
    def hash_password(password: str) -> str:
        salt = secrets.token_hex(16)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', 
                                       password.encode('utf-8'), 
                                       salt.encode('utf-8'), 
                                       100000)
        return f"{salt}:{pwd_hash.hex()}"
    
    @staticmethod
    def verify_password(password: str, hash_str: str) -> bool:
        salt, pwd_hash = hash_str.split(':')
        return secrets.compare_digest(
            pwd_hash,
            hashlib.pbkdf2_hmac('sha256', 
                               password.encode('utf-8'), 
                               salt.encode('utf-8'), 
                               100000).hex()
        )
```

## 📊 Cache & Performance

### Gerenciamento de Cache
- **Redis integration**: Integração com Redis
- **Memory cache**: Cache em memória
- **Cache invalidation**: Invalidação de cache
- **Performance monitoring**: Monitoramento de performance

## 📝 Variáveis de Ambiente

### Configurações Principais
```bash
# Debug
DEBUG=False
LOG_LEVEL=INFO

# Database
DATABASE_URL=sqlite:///app.db

# Cache
REDIS_URL=redis://localhost:6379
CACHE_TTL=3600

# Security
SECRET_KEY=your-secret-key-here
JWT_EXPIRE_HOURS=24

# Models
MODEL_PATH=./models
MODEL_CACHE_SIZE=100
```

## 🚀 Melhores Práticas

### Organização
- **Single responsibility**: Uma responsabilidade por utilitário
- **Type hints**: Anotações de tipo obrigatórias
- **Documentation**: Docstrings em todas as funções
- **Testing**: Cobertura de testes > 90%

### Performance
- **Lazy loading**: Carregamento sob demanda
- **Caching**: Cache inteligente
- **Connection pooling**: Pool de conexões
- **Async support**: Suporte assíncrono quando necessário

---

*Desenvolvido para a Plataforma de IA Conversacional*
