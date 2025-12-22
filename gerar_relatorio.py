"""
Gerador de Relatório YData Profiling
====================================
Este script gera um relatório EDA automatizado usando YData Profiling
SEM CONFIGURAÇÕES CUSTOMIZADAS - apenas os dados puros.

Autor: Jefferson Desenvolvedor
"""

import pandas as pd
from ydata_profiling import ProfileReport

# Carregar dados
print("Carregando dataset...")
df = pd.read_excel("Treinamento EDA estatistica descritiva .xls")

print(f"Dataset carregado: {df.shape[0]} registros, {df.shape[1]} variáveis")
print(f"\nColunas: {list(df.columns)}")

# Gerar relatório YData Profiling PURO (sem configurações customizadas)
print("\nGerando relatório YData Profiling...")
profile = ProfileReport(df, title="Relatório YData Profiling - EDA Automatizada")

# Salvar relatório HTML
output_file = "relatorio_ydata_profiling.html"
profile.to_file(output_file)

print(f"\n✅ Relatório gerado com sucesso: {output_file}")
print("\nAbra o arquivo HTML em um navegador para visualizar o relatório interativo.")
