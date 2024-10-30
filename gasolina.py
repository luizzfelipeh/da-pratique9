import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv')
gasolina_df.head()

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='pastel')
  grafico.set(title='Preço médio da gasolina nos 10 primeiros dias de Julho', xlabel='dia', ylabel='Preço');
  plt.savefig('gasolina.png')