import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('inputs/dados.txt')

plt.scatter(df['Temperatura'], df['Vendas'], color='blue')
plt.title('Temperatura vs Vendas de Sorvete')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Sorvetes Vendidos')
plt.grid(True)
plt.savefig('grafico.png')
