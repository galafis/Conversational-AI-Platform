#!/usr/bin/env python3
"""
Script de Validação de Dados de Clientes

Este script lê o arquivo customer_sample.csv do diretório data/datasets/samples/
e valida cada linha contra o schema JSON customer_schema.json do diretório 
data/datasets/schemas/, exibindo um relatório de linhas válidas/inválidas.

Autor: Gabriel Demetrios Lafis
Data: 16 de setembro de 2025
Versão: 1.0

Uso:
    python validate_customer_data.py

Requisitos:
    - jsonschema: pip install jsonschema
    - pandas: pip install pandas
"""

import json
import csv
import os
from pathlib import Path
from typing import Dict, Any, List, Tuple
from datetime import datetime

try:
    from jsonschema import validate, ValidationError, Draft202012Validator
except ImportError:
    print("ERRO: Biblioteca jsonschema não encontrada.")
    print("Para instalar execute: pip install jsonschema")
    exit(1)

try:
    import pandas as pd
except ImportError:
    print("ERRO: Biblioteca pandas não encontrada.")
    print("Para instalar execute: pip install pandas")
    exit(1)


class CustomerDataValidator:
    """
    Classe para validação de dados de clientes contra schema JSON.
    """
    
    def __init__(self):
        self.base_path = self._get_base_path()
        self.csv_path = self.base_path / "data" / "datasets" / "samples" / "customer_sample.csv"
        self.schema_path = self.base_path / "data" / "datasets" / "schemas" / "customer_schema.json"
        self.schema = None
        self.validator = None
        
    def _get_base_path(self) -> Path:
        """
        Determina o caminho base do projeto (raiz do repositório).
        """
        current_path = Path(__file__).resolve()
        # Navegar até encontrar a raiz do projeto (onde está o README.md)
        for parent in current_path.parents:
            if (parent / "README.md").exists() and (parent / "data").exists():
                return parent
        # Se não encontrar, usar caminho relativo a partir de src/backend/utils
        return current_path.parents[3]  # utils -> backend -> src -> raiz do projeto
    
    def load_schema(self) -> bool:
        """
        Carrega o schema JSON do arquivo customer_schema.json.
        
        Returns:
            bool: True se carregado com sucesso, False caso contrário.
        """
        try:
            if not self.schema_path.exists():
                print(f"ERRO: Arquivo de schema não encontrado: {self.schema_path}")
                return False
                
            with open(self.schema_path, 'r', encoding='utf-8') as f:
                self.schema = json.load(f)
                
            # Criar validador para melhor performance em validações múltiplas
            self.validator = Draft202012Validator(self.schema)
            
            print(f"✅ Schema carregado com sucesso: {self.schema_path}")
            print(f"   Título: {self.schema.get('title', 'N/A')}")
            print(f"   Campos obrigatórios: {', '.join(self.schema.get('required', []))}")
            return True
            
        except json.JSONDecodeError as e:
            print(f"ERRO: Arquivo de schema com formato JSON inválido: {e}")
            return False
        except Exception as e:
            print(f"ERRO: Falha ao carregar schema: {e}")
            return False
    
    def load_csv_data(self) -> List[Dict[str, Any]]:
        """
        Carrega os dados do arquivo CSV.
        
        Returns:
            List[Dict]: Lista de dicionários com os dados do CSV.
        """
        try:
            if not self.csv_path.exists():
                print(f"ERRO: Arquivo CSV não encontrado: {self.csv_path}")
                return []
            
            # Usar pandas para leitura mais robusta
            df = pd.read_csv(self.csv_path)
            
            print(f"✅ CSV carregado com sucesso: {self.csv_path}")
            print(f"   Total de linhas: {len(df)}")
            print(f"   Colunas: {', '.join(df.columns)}")
            
            # Converter para lista de dicionários
            # Tratar valores NaN do pandas
            data = df.where(pd.notnull(df), None).to_dict('records')
            
            return data
            
        except pd.errors.EmptyDataError:
            print(f"ERRO: Arquivo CSV está vazio: {self.csv_path}")
            return []
        except pd.errors.ParserError as e:
            print(f"ERRO: Erro ao processar CSV: {e}")
            return []
        except Exception as e:
            print(f"ERRO: Falha ao carregar CSV: {e}")
            return []
    
    def validate_record(self, record: Dict[str, Any], row_number: int) -> Tuple[bool, List[str]]:
        """
        Valida um registro individual contra o schema.
        
        Args:
            record: Dicionário com os dados do registro
            row_number: Número da linha para relatório de erro
            
        Returns:
            Tuple[bool, List[str]]: (é_válido, lista_de_erros)
        """
        errors = []
        
        try:
            # Usar o validador para melhor performance
            validation_errors = list(self.validator.iter_errors(record))
            
            if validation_errors:
                for error in validation_errors:
                    if error.path:
                        field_path = '.'.join(str(p) for p in error.path)
                        errors.append(f"Campo '{field_path}': {error.message}")
                    else:
                        errors.append(f"Erro geral: {error.message}")
                return False, errors
            else:
                return True, []
                
        except Exception as e:
            errors.append(f"Erro de validação: {str(e)}")
            return False, errors
    
    def validate_all_data(self) -> Dict[str, Any]:
        """
        Valida todos os dados e retorna relatório completo.
        
        Returns:
            Dict: Relatório com estatísticas de validação.
        """
        print("\n" + "="*60)
        print(" INICIANDO VALIDAÇÃO DE DADOS DE CLIENTES")
        print("="*60)
        
        # Carregar schema
        if not self.load_schema():
            return {"success": False, "error": "Falha ao carregar schema"}
        
        # Carregar dados
        data = self.load_csv_data()
        if not data:
            return {"success": False, "error": "Falha ao carregar dados CSV"}
        
        print("\n📋 INICIANDO VALIDAÇÃO...")
        
        valid_count = 0
        invalid_count = 0
        validation_errors = []
        
        for i, record in enumerate(data, 1):
            is_valid, errors = self.validate_record(record, i)
            
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1
                validation_errors.append({
                    "row": i,
                    "data": record,
                    "errors": errors
                })
        
        # Preparar relatório
        total_count = len(data)
        success_rate = (valid_count / total_count * 100) if total_count > 0 else 0
        
        report = {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "csv_file": str(self.csv_path),
            "schema_file": str(self.schema_path),
            "total_records": total_count,
            "valid_records": valid_count,
            "invalid_records": invalid_count,
            "success_rate": success_rate,
            "validation_errors": validation_errors
        }
        
        return report
    
    def print_report(self, report: Dict[str, Any]):
        """
        Exibe o relatório de validação formatado.
        
        Args:
            report: Dicionário com o relatório de validação.
        """
        if not report["success"]:
            print(f"\n❌ ERRO: {report.get('error', 'Erro desconhecido')}")
            return
        
        print("\n" + "="*60)
        print(" RELATÓRIO DE VALIDAÇÃO")
        print("="*60)
        
        print(f"📊 ESTATÍSTICAS GERAIS:")
        print(f"   • Total de registros processados: {report['total_records']:,}")
        print(f"   • Registros válidos: {report['valid_records']:,}")
        print(f"   • Registros inválidos: {report['invalid_records']:,}")
        print(f"   • Taxa de sucesso: {report['success_rate']:.1f}%")
        
        print(f"\n📁 ARQUIVOS:")
        print(f"   • CSV: {report['csv_file']}")
        print(f"   • Schema: {report['schema_file']}")
        print(f"   • Data/Hora: {report['timestamp']}")
        
        if report['invalid_records'] > 0:
            print(f"\n❌ ERROS ENCONTRADOS ({report['invalid_records']} registros):")
            
            # Mostrar apenas os primeiros 10 erros para não poluir o terminal
            errors_to_show = min(10, len(report['validation_errors']))
            
            for error_info in report['validation_errors'][:errors_to_show]:
                print(f"\n   📍 Linha {error_info['row']}:")
                
                # Mostrar dados da linha (apenas campos principais)
                data = error_info['data']
                main_fields = ['id', 'name', 'email', 'category', 'score']
                data_summary = {k: data.get(k, 'N/A') for k in main_fields if k in data}
                print(f"      Dados: {data_summary}")
                
                # Mostrar erros
                for error_msg in error_info['errors']:
                    print(f"      • {error_msg}")
            
            if len(report['validation_errors']) > errors_to_show:
                remaining = len(report['validation_errors']) - errors_to_show
                print(f"\n   ... e mais {remaining} erro(s). Execute com --verbose para ver todos.")
        
        else:
            print(f"\n✅ SUCESSO: Todos os registros estão válidos!")
        
        print("\n" + "="*60)


def main():
    """
    Função principal do script.
    """
    print("🔍 VALIDADOR DE DADOS DE CLIENTES")
    print(f"Executado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}")
    
    validator = CustomerDataValidator()
    report = validator.validate_all_data()
    validator.print_report(report)
    
    # Código de saída baseado no resultado
    if not report["success"]:
        exit(1)
    elif report["invalid_records"] > 0:
        print(f"\n⚠️  ATENÇÃO: {report['invalid_records']} registro(s) inválido(s) encontrado(s).")
        exit(2)
    else:
        print(f"\n🎉 PERFEITO: Todos os dados estão válidos!")
        exit(0)


if __name__ == "__main__":
    main()
