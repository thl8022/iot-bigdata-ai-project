import random
import pandas as pd
from sklearn.linear_model import LinearRegression

# Simulação de sensores IoT
temperatura = [random.randint(20, 40) for _ in range(50)]
umidade = [random.randint(30, 90) for _ in range(50)]

data = pd.DataFrame({
    "temperatura": temperatura,
    "umidade": umidade
})

print("Dados coletados dos sensores IoT:")
print(data.head())

# Modelo simples de IA
X = data[["temperatura"]]
y = data["umidade"]

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[30]])

print("\nPrevisão de umidade para temperatura 30°C:")
print(pred)