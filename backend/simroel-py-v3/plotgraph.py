import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
caminho_arquivo = "/home/backu/PycharmProjects/simroelfix/simroel-py-v3/Result/new_FF_est2.csv"
df = pd.read_csv(caminho_arquivo)

# Verificar os tipos de dados das colunas
print("Tipos de dados antes da conversão:")
print(df.dtypes)

# Converter colunas para o tipo numérico
colunas_numericas = ['Resource', 'OSNR', 'Crosstalk', 'nli', 'Allocted', 'Load']
df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors='coerce')

# Verificar os tipos de dados após a conversão
print("\nTipos de dados após a conversão:")
print(df.dtypes)

# Verificar se há valores nulos após a conversão
print("\nValores nulos após a conversão:")
print(df.isnull().sum())

# Evitar divisões por zero e calcular as métricas normalizadas por "Allocated"
df['Resource_pb'] = df['Resource'] / df['Allocted']
df['OSNR_pb'] = df['OSNR'] / df['Allocted']
df['Crosstalk_pb'] = df['Crosstalk'] / df['Allocted']
df['Total_pb'] = (df['Resource'] + df['OSNR'] + df['Crosstalk']) / df['Allocted']

# Substituir zeros para evitar problemas ao usar escala logarítmica
df.replace(0, 1e-6, inplace=True)

# Transformar o DataFrame para formato longo para plotagem
df_melted = df.melt(
    id_vars=['Load'],
    value_vars=['Resource_pb', 'OSNR_pb', 'Crosstalk_pb', 'Total_pb'],
    var_name='Metric',
    value_name='pb'
)

# Plotar gráfico com seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df_melted,
    x='Load',
    y='pb',
    hue='Metric',
    marker='o',
    palette='husl',
    linewidth=2
)

# Configurações do gráfico
plt.xlabel('Load [Erlang]', fontsize=12)
plt.ylabel('pb (Métrica / Allocated)', fontsize=12)
plt.yscale('log')  # Escala logarítmica no eixo Y
plt.title('Load vs pb (Resource, OSNR, Crosstalk)', fontsize=14)
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
plt.legend(title='Métrica', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Exibir gráfico
plt.show()