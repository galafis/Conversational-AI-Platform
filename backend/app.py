# Aplicação Flask principal - Conversational AI Platform
# Este arquivo será populado com o conteúdo do app.py raiz

from flask import Flask, request, jsonify
from models.nlp_processor import NLPProcessor

app = Flask(__name__)
processor = NLPProcessor()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint principal para chat conversacional"""
    message = request.json.get('message')
    response = processor.process_message(message)
    return jsonify({'response': response})

@app.route('/api/health', methods=['GET'])
def health():
    """Endpoint de verificação de saúde da aplicação"""
    return jsonify({'status': 'healthy', 'message': 'Conversational AI Platform is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
