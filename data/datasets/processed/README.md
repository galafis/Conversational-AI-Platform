# Processed Data

Este diretório contém datasets que passaram por processos de limpeza, transformação e preparação para análise.

## Finalidade

- Armazenar dados limpos e preparados para análise
- Dados estruturados e padronizados após ETL (Extract, Transform, Load)
- Datasets prontos para treinamento de modelos de machine learning
- Dados com tratamento de valores ausentes e outliers

## Tipos de Transformações Comuns

- **Limpeza**: Remoção de duplicatas, tratamento de valores nulos
- **Normalização**: Padronização de formatos de data, texto, etc.
- **Feature Engineering**: Criação de novas variáveis derivadas
- **Encoding**: Conversão de variáveis categóricas para numéricas
- **Scaling**: Normalização e padronização de escalas
- **Discretização**: Agrupamento de valores contínuos em intervalos

## Formatos Recomendados

- `.parquet` - Formato otimizado para análises (recomendado)
- `.csv` - Para compatibilidade e visualização
- `.json` - Para dados semi-estruturados processados
- `.h5` / `.hdf5` - Para grandes volumes de dados numéricos
- `.pkl` / `.pickle` - Para objetos Python complexos

## Nota sobre Formatos

⚠️ **Importante**: Em projetos reais de produção, é altamente recomendado utilizar formatos binários otimizados como:

- **`.parquet`**: Formato colunar comprimido, ideal para analytics e machine learning
- **`.h5`** / **`.hdf5`**: Para datasets científicos e arrays multidimensionais
- **`.pkl`** / **`.pickle`**: Para objetos Python complexos e modelos treinados

O arquivo `processed_sample.csv` neste repositório utiliza formato CSV apenas para demonstração e compatibilidade com GitHub. Em ambiente de produção, este mesmo dataset seria armazenado como `processed_sample.parquet` para melhor performance e menor uso de espaço.

## Exemplos de Uso

```
processed/
├── train_features.parquet
├── test_features.parquet
├── validation_features.parquet
├── customer_segments_clean.csv
├── nlp_processed/
│   ├── tokenized_reviews.pkl
│   └── embeddings_matrix.h5
└── timeseries/
    ├── daily_aggregated.parquet
    └── monthly_trends.csv
```

## Boas Práticas

1. **Versionamento**: Inclua versão ou timestamp nos nomes dos arquivos
2. **Metadata**: Documente as transformações aplicadas
3. **Validação**: Inclua testes de qualidade dos dados
4. **Separacao**: Mantenha dados de treino, validação e teste separados
5. **Nomenclatura**: Use convenções claras (train_, test_, val_, etc.)
6. **Documentação**: Registre schema e estatisticas descritivas

## Pipeline de Processamento

1. **Ingestão**: Leitura dos dados brutos de `/raw`
2. **Limpeza**: Tratamento de inconsistências e valores ausentes
3. **Transformção**: Aplicação de regras de negócio e feature engineering
4. **Validação**: Verificação da qualidade e integridade dos dados
5. **Export**: Salvar dados processados em formatos otimizados
6. **Catalog**: Registrar metadata e linhagem dos dados
