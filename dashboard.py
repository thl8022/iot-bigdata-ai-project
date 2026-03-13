import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Dashboard IoT + Inteligência Artificial")

# Simulação de sensores IoT
temperatura = [random.randint(20, 40) for _ in range(50)]
umidade = [random.randint(30, 90) for _ in range(50)]

data = pd.DataFrame({
    "temperatura": temperatura,
    "umidade": umidade
})

st.subheader("Dados coletados dos sensores IoT")
st.write(data)

# Gráfico
st.subheader("Gráfico de Temperatura vs Umidade")

fig, ax = plt.subplots()
ax.scatter(data["temperatura"], data["umidade"])
ax.set_xlabel("Temperatura")
ax.set_ylabel("Umidade")

st.pyplot(fig)

# Modelo de IA
X = data[["temperatura"]]
y = data["umidade"]

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[30]])

st.subheader("Previsão de IA")

st.write(f"Umidade prevista para temperatura de 30°C: {pred[0]:.2f}")