import pandas as pd
from sqlalchemy import create_engine

# conexão com postgres (nome do serviço = postgres)
engine = create_engine("postgresql://user:password@postgres:5432/iot_db")

# carregar CSV
data = pd.read_csv("IOT-temp.csv")

print("Dados carregados:")
print(data.head())

# enviar para o banco
data.to_sql("temperature_readings", engine, if_exists="replace", index=False)

print("Dados inseridos no PostgreSQL com sucesso!")