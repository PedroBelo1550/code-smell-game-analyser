import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.stats import spearmanr
from scipy.stats import kruskal
from scipy.stats import shapiro

df = pd.read_excel('graficos/data.xlsx', sheet_name='Export')

dependente = 'periodo'
independente = 'Game Smells'

# Calculando a mediana da complexidade por período
mediana_complexidade_por_periodo = df.groupby(independente)[dependente].median()

# Calculando a regressão
slope, intercept, r_value, p_value, std_err = linregress(df[independente], df[dependente])

print(f"Equação de regressão: {independente} = {slope} * {dependente} + {intercept}")
print("Coeficiente de correlação de Pearson (r):", r_value)

# Coeficiente de correlação de Spearmanr
r, p_value_spearman = spearmanr(df[independente], df[dependente])

print("Coeficiente de correlação de Spearmanr (r):", r)
print("Valor-p Spearman:", p_value_spearman)

# Teste de Kruskal-Wallis
periodos = []
for periodo, grupo in df.groupby(dependente):
    periodos.append(grupo[independente])

statistic, p_value_kruskal = kruskal(*periodos)

alpha = 0.05
if p_value_kruskal < alpha:
    print(f"As medianas são estatisticamente diferentes (Rejeitamos a hipótese nula) - Resultado: {p_value_kruskal}")
else:
    print(f"As medianas não são estatisticamente diferentes (Falhamos em rejeitar a hipótese nula) - Resultado: {p_value_kruskal}")


stat, p_value_shapiro = shapiro(df[dependente])
print(f'Teste de Shapiro-Wilk: Estatística={stat}, p-valor={p_value_shapiro}')

if p_value_shapiro < alpha:
    print("Os dados não seguem uma distribuição normal (Rejeitamos a hipótese nula)")
else:
    print("Os dados seguem uma distribuição normal (Falhamos em rejeitar a hipótese nula)")
