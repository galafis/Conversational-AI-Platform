# Raw Data

Este diretório contém os datasets originais sem qualquer processamento ou transformação.

## Finalidade

- Armazenar dados brutos obtidos de fontes externas
- Manter a integridade dos dados originais como backup
- Servir como ponto de partida para o pipeline de processamento de dados

## Tipos de Arquivos Suportados

- `.csv` - Arquivos de valores separados por vírgula
- `.json` - Dados estruturados em formato JSON
- `.xlsx` - Planilhas do Microsoft Excel
- `.parquet` - Formato colunar otimizado para análise
- `.txt` - Arquivos de texto simples
- `.xml` - Dados estruturados em XML

## Exemplos de Uso

```
raw/
├── customer_data_2024.csv
├── transaction_logs.json
├── product_catalog.xlsx
├── user_feedback.txt
└── api_responses/
    ├── weather_data_jan.json
    └── stock_prices.csv
```

## Boas Práticas

1. **Nomenclatura**: Use nomes descritivos incluindo data quando relevante
2. **Documentação**: Mantenha um registro da origem e data de coleta
3. **Backup**: Nunca modifique arquivos nesta pasta diretamente
4. **Organização**: Use subpastas para organizar por fonte ou período
5. **Metadados**: Inclua informações sobre a coleta dos dados quando possível

## Fluxo de Trabalho

1. Dados brutos são colocados nesta pasta
2. Scripts de limpeza processam os dados para `/processed`
3. Dados originais permanecem inalterados como referência
