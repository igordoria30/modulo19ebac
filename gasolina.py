
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv("gasolina.csv")

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=tabela, x="dia", y="venda")
  grafico.set(title='Preço da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021', xlabel='Dia', ylabel='Preço ($)');

grafico.legend(["Vendas"], loc='upper right', bbox_to_anchor=(1.1, 1))
