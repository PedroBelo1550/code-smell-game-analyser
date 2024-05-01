import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.stats import spearmanr

df = pd.read_excel('graficos/data.xlsx', sheet_name='Export')

dependente = 'Game Smells'

independente = 'periodo'

# Calculando a mediana da complexidade por período
mediana_complexidade_por_periodo = df.groupby(independente)[dependente].median()

# Calculando a regressão
slope, intercept, r_value, p_value, std_err = linregress(df[independente], df[dependente])

print("Equação de regressão: Complexity = {}*Período + {}".format(slope, intercept))
print("Coeficiente de correlação de Pearson (r):", r_value)

r, p_value = spearmanr(df[independente], df[dependente])

print("Coeficiente de correlação de Spearmanr (r):", r)
print("Valor-p:", p_value)