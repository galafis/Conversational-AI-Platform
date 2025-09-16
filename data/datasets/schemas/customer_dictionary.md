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

---

# Boas Práticas para Documentação de Dicionários de Dados

## 1. Estrutura e Organização

### Informações Essenciais
- **Cabeçalho claro**: Nome do dataset e versão
- **Metadados básicos**: Origem, frequência, responsável
- **Data de atualização**: Para controle de versão

### Tabela de Campos
- **Colunas obrigatórias**: Campo, Tipo, Obrigatório, Descrição, Exemplo
- **Ordem lógica**: Campos chave primeiro, depois funcionais
- **Nomenclatura consistente**: Seguir padrões da organização

## 2. Descrições Efetivas

### Clareza
- Use linguagem simples e objetiva
- Evite jargões técnicos desnecessários
- Seja específico sobre o propósito do campo

### Completude
- Documente todos os campos, mesmo os óbvios
- Inclua restrições e validações
- Especifique formatos esperados

### Exemplos Representativos
- Use dados realistas (anonimizados)
- Mostre diferentes cenários quando aplicável
- Mantenha consistência nos exemplos

## 3. Regras de Negócio

### Validações
- Documente todas as regras de validação
- Especifique dependências entre campos
- Inclua regras de integridade referencial

### Constraints Técnicos
- Tamanhos máximos e mínimos
- Formatos obrigatórios (regex, padrões)
- Valores permitidos (enums, listas)

## 4. Relacionamentos e Dependências

### Mapeamento de Dependências
- Liste datasets relacionados
- Especifique chaves estrangeiras
- Documente joins comuns

### Impacto de Mudanças
- Identifique sistemas downstream
- Documente processos que dependem dos dados
- Mantenha lista de stakeholders

## 5. Versionamento e Evolução

### Controle de Versão
- Use versionamento semântico (Major.Minor.Patch)
- Documente todas as mudanças
- Mantenha histórico de versões

### Processo de Mudança
- Defina workflow de aprovação
- Comunique mudanças com antecedência
- Teste compatibilidade antes de implementar

## 6. Qualidade e Manutenção

### Revisão Regular
- Agende revisões periódicas (trimestrais)
- Valide com usuários dos dados
- Atualize exemplos conforme necessário

### Automatização
- Integre com ferramentas de catalogação
- Use templates padronizados
- Automatize validação de esquemas

## 7. Acessibilidade e Uso

### Organização
- Use índices e sumários para documentos grandes
- Mantenha estrutura consistente
- Facilite navegação e busca

### Distribuição
- Publique em local acessível à equipe
- Mantenha sincronização com documentação técnica
- Considere integração com ferramentas de discovery

## 8. Padrões de Nomenclatura

### Convenções
- Use snake_case para nomes de campos
- Prefixos consistentes por tipo (id_, dt_, fl_)
- Evite abreviações não óbvias

### Glossário
- Mantenha glossário de termos técnicos
- Defina siglas e abreviações
- Padronize terminologia de negócio
