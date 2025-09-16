# Sample Data

Este diretório contém amostras pequenas dos datasets para testes rápidos, desenvolvimento e demonstração.

## Finalidade

- Acelerar o desenvolvimento com subconjuntos pequenos dos dados
- Permitir testes rápidos de código e algoritmos
- Facilitar demonstrações e prototipagem
- Reduzir tempo de processamento durante desenvolvimento
- Servir como dados de exemplo para documentação

## Características dos Samples

- **Tamanho reduzido**: Tipicamente 100-10,000 registros
- **Representatividade**: Mantém características dos dados originais
- **Diversidade**: Inclui variação suficiente para testes
- **Anonimização**: Dados sensíveis devem ser mascarados ou sintéticos

## Tipos de Amostras

### 1. Amostras Aleatórias
- Seleção random dos dados originais
- Mantém distribuição estatística
- Ideal para testes gerais

### 2. Amostras Estratificadas
- Preserva proporções de grupos importantes
- Garante representação de classes minoritárias
- Essencial para classificação

### 3. Amostras Extremas
- Inclui casos edge e outliers
- Testa robustez dos algoritmos
- Identifica pontos de falha

## Formatos Comuns

- `.csv` - Para visualização e testes rápidos
- `.json` - Para dados semi-estruturados
- `.parquet` - Quando performance é importante
- `.pkl` - Para objetos Python complexos

## Exemplos de Uso

```
samples/
├── customer_sample_1k.csv          # 1,000 clientes aleatórios
├── transactions_sample_5k.json     # 5,000 transações
├── product_catalog_sample.csv      # Amostra de catálogo
├── edge_cases/
│   ├── outliers_sample.csv         # Casos extremos
│   └── missing_data_sample.csv     # Dados com valores ausentes
└── synthetic/
    ├── fake_customer_data.csv      # Dados sintéticos
    └── mock_api_responses.json     # Respostas simuladas
```

## Boas Práticas

1. **Nomenclatura**: Inclua tamanho da amostra no nome (ex: _1k, _10k)
2. **Documentação**: Registre como a amostra foi criada
3. **Atualização**: Mantenha amostras atualizadas com os dados originais
4. **Privacidade**: Nunca inclua dados sensíveis reais
5. **Versão**: Versione as amostras junto com os dados originais
6. **Seed**: Use seeds fixas para reprodução das amostras

## Scripts de Geração

### Python - Amostra Aleatória
```python
import pandas as pd

# Carregar dados completos
df = pd.read_csv('../raw/full_dataset.csv')

# Gerar amostra de 1000 registros
sample = df.sample(n=1000, random_state=42)

# Salvar amostra
sample.to_csv('dataset_sample_1k.csv', index=False)
```

### Python - Amostra Estratificada
```python
from sklearn.model_selection import train_test_split

# Amostra estratificada por categoria
sample, _ = train_test_split(
    df, 
    test_size=0.9,  # Manter apenas 10%
    stratify=df['category'],
    random_state=42
)
```

## Considerações de Segurança

- **Anonimização**: Remova ou mascare informações pessoais
- **Dados Sintéticos**: Use ferramentas como Faker para dados falsos
- **Revisão**: Sempre revise amostras antes de compartilhar
- **Controle de Acesso**: Mesmo amostras devem ter controle adequado
