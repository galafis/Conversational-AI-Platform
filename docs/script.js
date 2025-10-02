// Frontend JavaScript - Conversational AI Platform
// Lógica principal da interface web

// Configurações globais
const CONFIG = {
    API_BASE_URL: '/api',
    CHAT_ENDPOINT: '/api/chat',
    HEALTH_ENDPOINT: '/api/health'
};

// Estado da aplicação
const appState = {
    isLoading: false,
    conversationHistory: [],
    currentMessage: ''
};

// Funções de utilidade
const utils = {
    // Formata data/hora
    formatTimestamp: (date = new Date()) => {
        return date.toLocaleTimeString('pt-BR', {
            hour: '2-digit',
            minute: '2-digit'
        });
    },

    // Escape HTML
    escapeHtml: (text) => {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    },

    // Debounce function
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};

// API Functions
const api = {
    // Enviar mensagem para chat
    sendMessage: async (message) => {
        const response = await fetch(CONFIG.CHAT_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message })
        });
        
        if (!response.ok) {
            throw new Error('Erro na comunicação com a API');
        }
        
        return await response.json();
    },

    // Verificar saúde da API
    checkHealth: async () => {
        const response = await fetch(CONFIG.HEALTH_ENDPOINT);
        return await response.json();
    }
};

// Gerenciamento da interface
const ui = {
    elements: {},
    
    init: () => {
        ui.elements = {
            chatContainer: document.getElementById('chat-container'),
            messageInput: document.getElementById('message-input'),
            sendButton: document.getElementById('send-button'),
            loadingIndicator: document.getElementById('loading')
        };
        
        ui.bindEvents();
        ui.checkApiHealth();
    },
    
    bindEvents: () => {
        // Enviar mensagem ao pressionar Enter
        ui.elements.messageInput?.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                ui.sendMessage();
            }
        });
        
        // Enviar mensagem ao clicar no botão
        ui.elements.sendButton?.addEventListener('click', ui.sendMessage);
        
        // Auto-resize do textarea
        ui.elements.messageInput?.addEventListener('input', ui.autoResize);
    },
    
    autoResize: () => {
        const textarea = ui.elements.messageInput;
        if (textarea) {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        }
    },
    
    sendMessage: async () => {
        const message = ui.elements.messageInput?.value.trim();
        if (!message || appState.isLoading) return;
        
        try {
            ui.setLoading(true);
            ui.addMessage(message, 'user');
            ui.elements.messageInput.value = '';
            
            const response = await api.sendMessage(message);
            ui.addMessage(response.response, 'bot');
            
        } catch (error) {
            console.error('Erro ao enviar mensagem:', error);
            ui.addMessage('Desculpe, ocorreu um erro. Tente novamente.', 'bot', true);
        } finally {
            ui.setLoading(false);
        }
    },
    
    addMessage: (message, sender, isError = false) => {
        const messageEl = document.createElement('div');
        messageEl.className = `message message--${sender} ${isError ? 'message--error' : ''}`;
        
        const timestamp = utils.formatTimestamp();
        messageEl.innerHTML = `
            <div class="message__content">${utils.escapeHtml(message)}</div>
            <div class="message__time">${timestamp}</div>
        `;
        
        ui.elements.chatContainer?.appendChild(messageEl);
        ui.scrollToBottom();
        
        // Adicionar ao histórico
        appState.conversationHistory.push({
            message,
            sender,
            timestamp: new Date(),
            isError
        });
    },
    
    setLoading: (loading) => {
        appState.isLoading = loading;
        ui.elements.loadingIndicator?.classList.toggle('hidden', !loading);
        ui.elements.sendButton?.classList.toggle('disabled', loading);
    },
    
    scrollToBottom: () => {
        const container = ui.elements.chatContainer;
        if (container) {
            container.scrollTop = container.scrollHeight;
        }
    },
    
    checkApiHealth: async () => {
        try {
            const health = await api.checkHealth();
            console.log('API Status:', health);
        } catch (error) {
            console.warn('API health check failed:', error);
        }
    }
};

// Inicializar aplicação quando DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    ui.init();
    console.log('Conversational AI Platform initialized');
});

// Exportar para uso global (se necessário)
window.ConversationalAI = {
    ui,
    api,
    utils,
    appState
};

