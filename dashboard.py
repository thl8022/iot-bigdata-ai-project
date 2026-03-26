import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================
st.set_page_config(page_title="Dashboard IoT", layout="wide")

# ==============================
# CONEXÃO COM O BANCO
# ==============================
engine = create_engine("postgresql://user:password@localhost:5432/iot_db")

# ==============================
# FUNÇÃO PARA CARREGAR DADOS
# ==============================
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# ==============================
# TÍTULO
# ==============================
st.title("📊 Dashboard de Temperaturas IoT")

# ==============================
# CARREGANDO DADOS
# ==============================
df_in_out = load_data("temp_in_out")
df_timeline = load_data("temp_in_out_timeline")
df_hora = load_data("leituras_por_hora")
df_temp = load_data("temp_max_min_por_dia")

# ==============================
# KPI (INDICADORES IN vs OUT)
# ==============================
st.subheader("📌 Indicadores Gerais (Interno vs Externo)")

df_kpi = load_data("temp_in_out_timeline")

# Limpar dados
df_kpi.columns = df_kpi.columns.str.strip()
df_kpi["timestamp"] = pd.to_datetime(df_kpi["timestamp"], errors="coerce")

# Remover timezone se existir
if hasattr(df_kpi["timestamp"].dt, "tz") and df_kpi["timestamp"].dt.tz is not None:
    df_kpi["timestamp"] = df_kpi["timestamp"].dt.tz_convert(None)

# ==============================
# CÁLCULOS
# ==============================

df_in = df_kpi[df_kpi["ambiente"] == "In"]
df_out = df_kpi[df_kpi["ambiente"] == "Out"]

max_in = df_in["temp"].max()
min_in = df_in["temp"].min()

max_out = df_out["temp"].max()
min_out = df_out["temp"].min()

# ==============================
# DASHBOARD
# ==============================

col1, col2, col3, col4 = st.columns(4)

col1.metric("🔵 Máx Interno Atingida", f"{max_in:.1f} °C")
col2.metric("🔵 Mín Interno Atingida", f"{min_in:.1f} °C")
col3.metric("🔴 Máx Externo Atingida", f"{max_out:.1f} °C")
col4.metric("🔴 Mín Externo Atingida", f"{min_out:.1f} °C")


# ==============================
# GRÁFICO 1
# ==============================
st.header("📅 Temperatura Média Semanal (In vs Out)")

df = load_data("temp_in_out_timeline")

# Limpar colunas
df.columns = df.columns.str.strip()

# Converter data
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# 🔥 AGRUPAMENTO SEMANAL SIMPLES
df["semana"] = df["timestamp"].dt.to_period("W").apply(lambda r: r.start_time)

df_grouped = df.groupby(["semana", "ambiente"])["temp"].mean().reset_index()

# ==============================
# DEBUG (IMPORTANTE)
# ==============================
# st.write("Dados agrupados:", df_grouped.head())

# ==============================
# GRÁFICO
# ==============================
fig = px.line(
    df_grouped,
    x="semana",
    y="temp",
    color="ambiente",
    markers=True,
    title="Temperatura Média Semanal"
)

# Cores
fig.for_each_trace(lambda t: t.update(
    line=dict(color="blue") if t.name == "In" else dict(color="red")
))

st.plotly_chart(fig, use_container_width=True)

# ==============================
# GRÁFICO 2
# ==============================
st.header("⏱️ Leituras por Hora do Dia")

fig2 = px.line(
    df_hora,
    x="hora",
    y="contagem",
    markers=True,
    labels={"hora": "Hora", "contagem": "Quantidade de Leituras"}
)

st.plotly_chart(fig2, use_container_width=True)

# st.subheader("📋 Dados utilizados")
# st.dataframe(df_hora)

# ==============================
# GRÁFICO 3
# ==============================
st.header("📈 Temperaturas Máximas e Mínimas por Dia")

fig3 = px.line(
    df_temp,
    x="data",
    y=["temp_max", "temp_min"],
    markers=True,
    labels={
        "value": "Temperatura (°C)",
        "data": "Data",
        "variable": "Tipo"
    }
)

st.plotly_chart(fig3, use_container_width=True)

# st.subheader("📋 Dados utilizados")
# st.dataframe(df_temp)