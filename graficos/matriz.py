import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crie um DataFrame com seus dados
data = pd.read_excel('./graficos/data.xlsx')

df = data[['periodo', 'Complexity', 'Code', 'Game Smells']]

# Calcule a matriz de correlação
correlation_matrix = df.corr(method='spearman')

# Configure o estilo do gráfico
sns.set(style="white")

# Crie o mapa de calor da matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlação')
plt.show()
