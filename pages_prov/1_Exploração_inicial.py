# import streamlit as st
# import pandas as pd

# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/Life Expectancy Data.csv")
#     return df

# st.header("Exploración Inicial de los Datos")
# df = load_data()
# st.subheader("Primeras filas del dataset")
# st.write(df.head())

# st.subheader("Resumen de columnas")
# st.write(df.info())
# st.write(df.describe())

# st.subheader("Valores nulos por columna")
# st.write(df.isnull().sum())



import streamlit as st
import pandas as pd

# Função para carregar os dados com cache
@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/Life Expectancy Data.csv")
    return df

st.header("Exploração Inicial dos Dados")
df = carregar_dados()

# Visualizar as primeiras linhas
st.subheader("Primeiras linhas do dataset")
st.write(df.head())

# # Informações das colunas
# st.subheader("Informações gerais")
# buffer = st.empty()
# # Exibe info como texto, pois df.info() retorna None
# import io
# buffer = io.StringIO()
# df.info(buf=buffer)
# s = buffer.getvalue()
# st.text(s)

# Estatísticas descritivas
st.subheader("Estatísticas descritivas")
st.write(df.describe())

# Valores nulos
st.subheader("Valores ausentes em cada coluna")
st.write(df.isnull().sum())