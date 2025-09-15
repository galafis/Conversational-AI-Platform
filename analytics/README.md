# Analytics 📊

Este diretório contém os scripts e ferramentas de análise de dados da plataforma de IA conversacional.

## Estrutura

```
analytics/
├── README.md           # Este arquivo
├── analysis.R          # Scripts principais de análise em R
└── reports/            # Relatórios gerados automaticamente
```

## Funcionalidades

### Scripts de Análise
- **analysis.R**: Script principal contendo funções para análise de sentimentos, estatísticas de conversas e visualizações
- Análise de tendências de uso da plataforma
- Processamento de métricas de performance
- Geração de gráficos e dashboards

### Relatórios Automatizados
- A pasta `reports/` contém relatórios gerados automaticamente
- Análises estatísticas em formato HTML e PDF
- Visualizações de dados exportadas
- Relatórios de performance da IA

## Como Usar

1. Execute o script principal de análise:
```r
source("analytics/analysis.R")
```

2. Os relatórios são gerados automaticamente na pasta `reports/`

3. Visualize os resultados através dos arquivos HTML gerados

## Dependências

- R 4.0+
- Pacotes: ggplot2, dplyr, tidyr, rmarkdown
- Dados da plataforma em formato CSV/JSON
