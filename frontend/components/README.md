# Frontend Components Directory

## 📋 Descrição

Este diretório contém todos os componentes reutilizáveis da interface de usuário da plataforma conversacional. Inclui componentes para chat, formulários, modais, navegação e elementos de UI que seguem princípios de design modular e reutilização.

## 🧑‍💻 Componentes Principais

### Chat & Conversação
- **ChatContainer**: Container principal do chat
- **MessageBubble**: Bolhas de mensagens
- **InputBox**: Caixa de entrada de texto
- **TypingIndicator**: Indicador de digitação
- **MessageHistory**: Histórico de mensagens

### Interface & Navegação
- **Header**: Cabeçalho da aplicação
- **Sidebar**: Barra lateral
- **NavigationMenu**: Menu de navegação
- **Footer**: Rodapé da aplicação
- **LoadingSpinner**: Indicadores de carregamento

### Modais & Diálogos
- **Modal**: Modal genérico
- **ConfirmDialog**: Diálogo de confirmação
- **SettingsPanel**: Painel de configurações
- **AboutDialog**: Diálogo sobre

## 📁 Estrutura Esperada

```
components/
├── chat/
│   ├── ChatContainer.js
│   ├── MessageBubble.js
│   ├── InputBox.js
│   ├── TypingIndicator.js
│   └── MessageHistory.js
├── ui/
│   ├── Header.js
│   ├── Sidebar.js
│   ├── Modal.js
│   ├── Button.js
│   └── LoadingSpinner.js
├── forms/
│   ├── ContactForm.js
│   ├── FeedbackForm.js
│   └── SettingsForm.js
└── utils/
    ├── ComponentHelpers.js
    └── Validators.js
```

## 🛠️ Implementação

### Exemplo de Componente Chat
```javascript
// ChatContainer.js
class ChatContainer {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.messages = [];
        this.init();
    }
    
    init() {
        this.createChatInterface();
        this.bindEvents();
    }
    
    createChatInterface() {
        this.container.innerHTML = `
            <div class="chat-header">
                <h3>Assistente Virtual</h3>
                <span class="status-indicator online"></span>
            </div>
            <div class="chat-messages" id="chat-messages"></div>
            <div class="chat-input-container">
                <input type="text" id="message-input" 
                       placeholder="Digite sua mensagem..." />
                <button id="send-button">Enviar</button>
            </div>
        `;
    }
    
    addMessage(message, sender = 'user') {
        const messageElement = this.createMessageBubble(message, sender);
        const messagesContainer = document.getElementById('chat-messages');
        messagesContainer.appendChild(messageElement);
        this.scrollToBottom();
    }
    
    createMessageBubble(text, sender) {
        const bubble = document.createElement('div');
        bubble.className = `message-bubble ${sender}`;
        bubble.innerHTML = `
            <div class="message-content">${text}</div>
            <div class="message-time">${new Date().toLocaleTimeString()}</div>
        `;
        return bubble;
    }
    
    scrollToBottom() {
        const container = document.getElementById('chat-messages');
        container.scrollTop = container.scrollHeight;
    }
}
```

### Exemplo de Componente Modal
```javascript
// Modal.js
class Modal {
    constructor(options = {}) {
        this.title = options.title || '';
        this.content = options.content || '';
        this.closable = options.closable !== false;
        this.modal = null;
    }
    
    show() {
        this.create();
        document.body.appendChild(this.modal);
        
        // Animação de entrada
        setTimeout(() => {
            this.modal.classList.add('show');
        }, 10);
    }
    
    hide() {
        this.modal.classList.remove('show');
        setTimeout(() => {
            if (this.modal && this.modal.parentNode) {
                this.modal.parentNode.removeChild(this.modal);
            }
        }, 300);
    }
    
    create() {
        this.modal = document.createElement('div');
        this.modal.className = 'modal-overlay';
        this.modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h4>${this.title}</h4>
                    ${this.closable ? '<button class="modal-close">&times;</button>' : ''}
                </div>
                <div class="modal-body">
                    ${this.content}
                </div>
            </div>
        `;
        
        if (this.closable) {
            this.modal.querySelector('.modal-close').onclick = () => this.hide();
            this.modal.onclick = (e) => {
                if (e.target === this.modal) this.hide();
            };
        }
    }
}
```

## 🎨 Estilos & Design

### CSS Variáveis
```css
:root {
    /* Cores principais */
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --background-color: #f8f9fa;
    --text-color: #333333;
    
    /* Chat */
    --chat-bg: #ffffff;
    --user-message-bg: #667eea;
    --bot-message-bg: #f1f3f5;
    --message-text: #ffffff;
    
    /* Componentes */
    --border-radius: 8px;
    --shadow: 0 2px 10px rgba(0,0,0,0.1);
    --transition: all 0.3s ease;
}
```

### Exemplo de Estilo de Componente
```css
.chat-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    max-width: 800px;
    margin: 0 auto;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
    background: var(--chat-bg);
}

.message-bubble {
    max-width: 70%;
    margin: 8px;
    padding: 12px 16px;
    border-radius: var(--border-radius);
    animation: slideIn 0.3s ease;
}

.message-bubble.user {
    align-self: flex-end;
    background: var(--user-message-bg);
    color: var(--message-text);
}

.message-bubble.bot {
    align-self: flex-start;
    background: var(--bot-message-bg);
    color: var(--text-color);
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

## 📡 Eventos & Interação

### Sistema de Eventos
```javascript
// EventManager.js
class EventManager {
    constructor() {
        this.events = {};
    }
    
    on(event, callback) {
        if (!this.events[event]) {
            this.events[event] = [];
        }
        this.events[event].push(callback);
    }
    
    emit(event, data) {
        if (this.events[event]) {
            this.events[event].forEach(callback => callback(data));
        }
    }
    
    off(event, callback) {
        if (this.events[event]) {
            this.events[event] = this.events[event].filter(cb => cb !== callback);
        }
    }
}

// Uso global
const eventManager = new EventManager();

// Emitir eventos de componentes
eventManager.emit('message:sent', { text: 'Olá!', timestamp: Date.now() });
eventManager.emit('modal:opened', { modalId: 'settings' });
```

## 📦 Gerenciamento de Estado

### Estado Global Simples
```javascript
// StateManager.js
class StateManager {
    constructor() {
        this.state = {
            messages: [],
            user: null,
            settings: {
                theme: 'light',
                language: 'pt-BR'
            }
        };
        this.subscribers = [];
    }
    
    getState() {
        return { ...this.state };
    }
    
    setState(newState) {
        this.state = { ...this.state, ...newState };
        this.notifySubscribers();
    }
    
    subscribe(callback) {
        this.subscribers.push(callback);
    }
    
    notifySubscribers() {
        this.subscribers.forEach(callback => callback(this.state));
    }
}
```

## 🚀 Melhores Práticas

### Organização de Componentes
- **Modularidade**: Cada componente tem uma responsabilidade específica
- **Reutilização**: Componentes genéricos e configuráveis
- **Acessibilidade**: Suporte a ARIA e navegação por teclado
- **Performance**: Lazy loading e otimização de renderização

### Padrões de Desenvolvimento
- **ES6+**: Uso de classes, arrow functions, destructuring
- **CSS moderno**: Flexbox, Grid, CSS Variables
- **Responsive**: Design adaptável para todos os dispositivos
- **Progressive Enhancement**: Funcionalidade básica sem JavaScript

---

*Desenvolvido para a Plataforma de IA Conversacional*
