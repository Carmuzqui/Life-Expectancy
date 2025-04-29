# import streamlit as st
# import pandas as pd
# import plotly.express as px

# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/Life Expectancy Data.csv")
#     return df

# df = load_data()
# st.header("Distribuciones Univariadas")

# col = st.selectbox("Seleccione variable numérica", df.select_dtypes("number").columns)
# fig = px.histogram(df, x=col, nbins=30, title=f"Distribución de {col}")
# st.plotly_chart(fig, use_container_width=True)




import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/Life Expectancy Data.csv")
    return df

df = carregar_dados()
st.header("Distribuições Univariadas")

# Seleção de coluna numérica
coluna = st.selectbox(
    "Selecione uma variável numérica para visualizar a distribuição", 
    df.select_dtypes("number").columns
)

# Histograma com Plotly
fig = px.histogram(df, x=coluna, nbins=30, 
                   title=f"Distribuição de {coluna}",
                   color_discrete_sequence=["#2E86AB"])
st.plotly_chart(fig, use_container_width=True)