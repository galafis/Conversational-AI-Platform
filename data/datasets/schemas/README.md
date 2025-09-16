# Data Schemas & Documentation

Este diretório contém a documentação detalhada dos esquemas de dados, metadados e descrições das estruturas dos datasets.

## Finalidade

- Documentar a estrutura e esquemas dos datasets
- Manter dicionários de dados e metadados
- Registrar versões e evolução dos esquemas
- Facilitar o entendimento dos dados para a equipe
- Suportar validação e qualidade dos dados
- Estabelecer contratos de dados entre sistemas

## Tipos de Documentação

### 1. Dicionários de Dados
- Descrição detalhada de cada campo
- Tipos de dados e constraints
- Valores possíveis e domínios
- Regras de negócio aplicadas

### 2. Esquemas Técnicos
- Estruturas JSON Schema
- DDLs de banco de dados
- Schemas Avro/Parquet
- Definições XML/XSD

### 3. Metadados
- Informações sobre origem dos dados
- Histórico de modificações
- Frequência de atualização
- Proprietários dos dados

## Formatos Suportados

- `.json` - JSON Schema para validação
- `.sql` - DDL de bancos de dados
- `.avsc` - Esquemas Apache Avro
- `.md` - Documentação em Markdown
- `.yaml`/`.yml` - Metadados estruturados
- `.xml`/`.xsd` - Esquemas XML
- `.proto` - Protocol Buffers

## Exemplos de Uso

```
schemas/
├── customer/
│   ├── customer_schema.json        # JSON Schema
│   ├── customer_ddl.sql            # Criação da tabela
│   ├── customer_dictionary.md      # Dicionário de dados
│   └── customer_metadata.yaml      # Metadados
├── transactions/
│   ├── transaction_schema.avsc     # Schema Avro
│   ├── transaction_dictionary.md
│   └── validation_rules.json
└── api_responses/
    ├── weather_api.json
    └── payment_gateway.proto
```

## Estrutura de Documentação

### Dicionário de Dados (Template)
```markdown
# Dataset: [Nome]

## Visão Geral
- **Origem**: [Sistema/API/Arquivo]
- **Frequência**: [Diária/Semanal/Mensal]
- **Responsável**: [Time/Pessoa]
- **Última atualização**: [Data]

## Esquema

| Campo | Tipo | Nulo | Descrição | Exemplo |
|-------|------|------|-------------|----------|
| id | INTEGER | Não | Identificador único | 12345 |
| name | VARCHAR(100) | Não | Nome completo | "João Silva" |
| email | VARCHAR(255) | Sim | E-mail de contato | "joao@email.com" |

## Regras de Negócio
- [Lista de regras e validações]

## Dependências
- [Relacionamentos com outros datasets]
```

### JSON Schema (Exemplo)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Customer",
  "type": "object",
  "required": ["id", "name", "created_at"],
  "properties": {
    "id": {
      "type": "integer",
      "minimum": 1,
      "description": "Identificador único do cliente"
    },
    "name": {
      "type": "string",
      "maxLength": 100,
      "description": "Nome completo do cliente"
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "Endereço de e-mail"
    },
    "created_at": {
      "type": "string",
      "format": "date-time",
      "description": "Data de criação do registro"
    }
  }
}
```

## Boas Práticas

1. **Versionamento**: Use controle de versão para esquemas
2. **Retrocompatibilidade**: Mantenha compatibilidade com versões anteriores
3. **Validação**: Implemente validação automática de esquemas
4. **Documentação**: Mantenha documentação atualizada
5. **Padronização**: Use convenções consistentes de nomenclatura
6. **Revisão**: Faça revisão por pares das mudanças de esquema

## Ferramentas Recomendadas

### Validação
- **JSON Schema**: Para validação de estruturas JSON
- **Great Expectations**: Para testes de qualidade de dados
- **Apache Avro**: Para serialização e evolução de esquemas
- **Pandera**: Validação de DataFrames pandas

### Documentação
- **DBT**: Para documentação de modelos de dados
- **DataHub**: Para catalogação e linhagem de dados
- **Apache Atlas**: Para governança de metadados

## Evolução de Esquemas

### Mudanças Compatíveis
- Adição de campos opcionais
- Adição de valores em enums
- Documentação de campos existentes

### Mudanças Quebrantês
- Remoção de campos obrigatórios
- Mudança de tipos de dados
- Renomeação de campos
- Mudança de constraints

### Processo de Mudança
1. **Proposta**: Documente a mudança necessária
2. **Impacto**: Analise impacto em sistemas dependentes
3. **Migração**: Planeje estratégia de migração
4. **Implementação**: Execute mudanças gradualmente
5. **Validação**: Confirme que tudo funciona corretamente
6. **Documentação**: Atualize toda documentação relevante

## Governança de Dados

- **Proprietário**: Cada esquema deve ter um proprietário definido
- **Aprovação**: Mudanças devem ser aprovadas pelo proprietário
- **Comunicação**: Notifique equipes dependentes sobre mudanças
- **Conformidade**: Garanta aderência a políticas de dados
- **Auditoria**: Mantenha histórico de todas as mudanças
