#!/usr/bin/env python3
"""
Conversational-AI-Platform
Conversational AI platform with multi-turn dialogue support
Built by Gabriel Demetrios Lafis
"""

from flask import Flask, jsonify, render_template
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'project': 'Conversational-AI-Platform',
        'description': 'Conversational AI platform with multi-turn dialogue support',
        'author': 'Gabriel Demetrios Lafis',
        'status': 'active',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/status')
def status():
    return jsonify({'status': 'running', 'version': '1.0.0'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
