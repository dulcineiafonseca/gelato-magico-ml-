import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('inputs/dados.txt')
X = df[['Temperatura']]
y = df['Vendas']

modelo = LinearRegression()
modelo.fit(X, y)

joblib.dump(modelo, 'model/modelo_sorvete.pkl')
