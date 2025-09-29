pip install mlflow
mlflow ui

import mlflow
import mlflow.sklearn

mlflow.set_experiment("GelatoMagico")

with mlflow.start_run():
    mlflow.log_param("modelo", "LinearRegression")
    mlflow.log_metric("score", modelo.score(X, y))
    mlflow.sklearn.log_model(modelo, "modelo_sorvete")
