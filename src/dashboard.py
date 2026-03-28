import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import time

# ==============================
# CONFIGURAÇÃO DA PÁGINA
# ==============================
st.set_page_config(page_title="Dashboard IoT", layout="wide")

# ==============================
# CONEXÃO COM O BANCO (COM RETRY)
# ==============================
for i in range(5):
    try:
        engine = create_engine("postgresql://user:password@postgres:5432/iot_db")
        connection = engine.connect()
        break
    except:
        time.sleep(3)

# ==============================
# FUNÇÃO PARA CARREGAR DADOS
# ==============================
def load_data(view_name):
    df = pd.read_sql(f"SELECT * FROM {view_name}", engine)
    df.columns = df.columns.str.strip()
    return df

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

df_kpi = df_timeline.copy()

# Converter timestamp
df_kpi["timestamp"] = pd.to_datetime(df_kpi["timestamp"], errors="coerce")

# Remover timezone se existir
if hasattr(df_kpi["timestamp"].dt, "tz") and df_kpi["timestamp"].dt.tz is not None:
    df_kpi["timestamp"] = df_kpi["timestamp"].dt.tz_convert(None)

# Separar ambientes
df_in = df_kpi[df_kpi["ambiente"] == "In"]
df_out = df_kpi[df_kpi["ambiente"] == "Out"]

# KPIs
max_in = df_in["temp"].max()
min_in = df_in["temp"].min()
max_out = df_out["temp"].max()
min_out = df_out["temp"].min()

# Exibir KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("🔵 Máx Interno", f"{max_in:.1f} °C")
col2.metric("🔵 Mín Interno", f"{min_in:.1f} °C")
col3.metric("🔴 Máx Externo", f"{max_out:.1f} °C")
col4.metric("🔴 Mín Externo", f"{min_out:.1f} °C")

# ==============================
# GRÁFICO 1 - MÉDIA SEMANAL
# ==============================
st.header("📅 Temperatura Média Semanal (In vs Out)")

df = df_timeline.copy()

# Converter data
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Agrupar por semana
df["semana"] = df["timestamp"].dt.to_period("W").apply(lambda r: r.start_time)

df_grouped = df.groupby(["semana", "ambiente"])["temp"].mean().reset_index()

# Ordenar
df_grouped = df_grouped.sort_values(by="semana")

# Gráfico
fig = px.line(
    df_grouped,
    x="semana",
    y="temp",
    color="ambiente",
    markers=False,  # 🔥 mais limpo
    title="Temperatura Média Semanal"
)

# Cores
fig.for_each_trace(lambda t: t.update(
    line=dict(width=3, color="blue") if t.name == "In"
    else dict(width=3, color="red")
))

st.plotly_chart(fig, use_container_width=True)

# ==============================
# GRÁFICO 2 - POR HORA
# ==============================
st.header("⏱️ Leituras por Hora do Dia")

# Ordenar corretamente
df_hora["hora"] = pd.to_numeric(df_hora["hora"], errors="coerce")
df_hora = df_hora.sort_values(by="hora")

fig2 = px.line(
    df_hora,
    x="hora",
    y="contagem",
    markers=False,
    labels={"hora": "Hora", "contagem": "Quantidade de Leituras"}
)

st.plotly_chart(fig2, use_container_width=True)

# ==============================
# GRÁFICO 3 - POR DIA
# ==============================
st.header("📈 Temperaturas Máximas e Mínimas por Dia")

# Converter e ordenar data
df_temp["data"] = pd.to_datetime(df_temp["data"], errors="coerce")
df_temp = df_temp.sort_values(by="data")

fig3 = px.line(
    df_temp,
    x="data",
    y=["temp_max", "temp_min"],
    markers=False,
    labels={
        "value": "Temperatura (°C)",
        "data": "Data",
        "variable": "Tipo"
    }
)

st.plotly_chart(fig3, use_container_width=True)