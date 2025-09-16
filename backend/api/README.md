# Backend API Directory

## 📋 Descrição

Este diretório contém todos os endpoints da API RESTful da plataforma conversacional. Inclui rotas para chat, análise de sentimentos, gerenciamento de sessões e integrações com serviços externos.

## 🔗 Endpoints Principais

### Chat & Conversação
- **POST /api/chat**: Processar mensagens do usuário
- **GET /api/chat/history**: Histórico de conversações
- **POST /api/chat/feedback**: Feedback do usuário
- **DELETE /api/chat/clear**: Limpar sessão

### Análise & Processamento
- **POST /api/analyze/sentiment**: Análise de sentimentos
- **POST /api/analyze/intent**: Classificação de intenções
- **POST /api/analyze/entities**: Extração de entidades
- **GET /api/analyze/stats**: Estatísticas de uso

### Gerenciamento
- **GET /api/health**: Status da aplicação
- **GET /api/models**: Modelos disponíveis
- **POST /api/admin/reload**: Recarregar modelos

## 📁 Estrutura Esperada

```
api/
├── __init__.py
├── chat.py             # Endpoints de chat
├── analysis.py         # Endpoints de análise
├── admin.py            # Endpoints administrativos
├── auth.py             # Autenticação e autorização
├── middleware.py       # Middleware personalizado
├── validators.py       # Validação de dados
└── responses.py        # Formatação de respostas
```

## 🛠️ Implementação

### Exemplo de Endpoint
```python
from flask import Blueprint, request, jsonify
from models.nlp_processor import NLPProcessor

chat_bp = Blueprint('chat', __name__)
processor = NLPProcessor()

@chat_bp.route('/api/chat', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get('message')
    
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    
    try:
        response = processor.process_message(message)
        return jsonify({
            'response': response,
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

## 🔒 Autenticação

### Métodos Suportados
- **API Keys**: Para integrações externas
- **JWT Tokens**: Para sessões de usuário
- **Rate Limiting**: Controle de taxa de requisições

### Headers Obrigatórios
```http
Content-Type: application/json
Authorization: Bearer <token>
X-API-Key: <api-key>
```

## 📋 Documentação da API

### Swagger/OpenAPI
- **GET /api/docs**: Documentação interativa
- **GET /api/swagger.json**: Especificação OpenAPI
- **GET /api/redoc**: Documentação alternativa

### Formatos de Resposta
```json
{
  "data": {},
  "status": "success|error",
  "message": "Descrição opcional",
  "timestamp": "2025-09-16T10:04:00Z",
  "request_id": "uuid-unique-id"
}
```

## 📊 Monitoramento

- **Logs estruturados**: JSON logging
- **Métricas**: Prometheus/Grafana
- **Tracing**: OpenTelemetry
- **Health checks**: Endpoints de saúde

## 🚀 Deploy

### Variáveis de Ambiente
```bash
FLASK_ENV=production
API_SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
REDIS_URL=redis://localhost:6379
LOG_LEVEL=INFO
```

---

*Desenvolvido para a Plataforma de IA Conversacional*
