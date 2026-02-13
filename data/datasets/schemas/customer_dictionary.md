# Dataset: Customer

## Visão Geral

- **Origem**: Sistema CRM / API de Clientes
- **Frequência**: Diária
- **Responsável**: Equipe de Dados
- **Última atualização**: 16 de setembro de 2025
- **Versão do esquema**: 1.0

## Esquema

| Campo | Tipo | Obrigatório | Descrição | Exemplo |
|-------|------|-------------|-----------|----------|
| id | INTEGER | Sim | Identificador único do cliente | 12345 |
| name | VARCHAR(100) | Sim | Nome completo do cliente | "Maria Silva Santos" |
| email | VARCHAR(255) | Não | Endereço de e-mail válido | "maria.silva@email.com" |
| category | VARCHAR(20) | Sim | Categoria do cliente (premium, standard, basic) | "premium" |
| score | DECIMAL(5,2) | Não | Pontuação de crédito do cliente (0.00-999.99) | 785.50 |

## Regras de Negócio

- **ID**: Deve ser único e sequencial, gerado automaticamente
- **Name**: Não pode conter caracteres especiais além de espaços, hífens e apostrofes
- **Email**: Deve seguir formato RFC 5322 quando preenchido
- **Category**: Valores permitidos: "premium", "standard", "basic"
- **Score**: Quando preenchido, deve estar entre 0.00 e 999.99
- **Validação de integridade**: Clientes premium devem ter score >= 700

## Dependências

- **Relaciona com**: Dataset de transações (campo customer_id)
- **Origem dos dados**: API CRM v2.1
- **Sistemas dependentes**: 
  - Plataforma de Analytics
  - Sistema de Recomendações
  - Dashboard Executivo

## Metadados Técnicos

- **Formato de armazenamento**: JSON, Parquet
- **Encoding**: UTF-8
- **Compressão**: GZIP (JSON), Snappy (Parquet)
- **Particionamento**: Por data de criação (YYYY/MM/DD)
- **Retenção**: 7 anos

## Histórico de Versões

| Versão | Data | Alterações |
|--------|------|------------|
| 1.0 | 2025-09-16 | Criação inicial do esquema |


