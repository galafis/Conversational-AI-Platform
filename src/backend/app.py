# Aplicacao Flask principal - Conversational AI Platform

from flask import Flask, request, jsonify

try:
    from models.nlp_processor import NLPProcessor
except ImportError:
    from backend.models.nlp_processor import NLPProcessor

app = Flask(__name__)
processor = NLPProcessor()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint principal para chat conversacional"""
    data = request.json
    if not data or 'message' not in data:
        return jsonify({'error': 'Campo "message" e obrigatorio'}), 400
    message = data.get('message')
    if not message or not isinstance(message, str):
        return jsonify({'error': 'Campo "message" deve ser uma string nao vazia'}), 400
    response = processor.process_message(message)
    return jsonify({'response': response})

@app.route('/api/health', methods=['GET'])
def health():
    """Endpoint de verificacao de saude da aplicacao"""
    return jsonify({'status': 'healthy', 'message': 'Conversational AI Platform is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
