# import streamlit as st
# import pandas as pd
# import plotly.express as px

# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/Life Expectancy Data.csv")
#     return df

# df = load_data()
# st.header("Comparación: Desarrollados vs. No Desarrollados")
# if 'Status' in df.columns and 'Life expectancy ' in df.columns:
#     fig = px.box(df, x='Status', y='Life expectancy ', color='Status',
#                  title='Esperanza de Vida por Nivel de Desarrollo')
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.warning("Las columnas requeridas no están en el dataset.")




import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/Life Expectancy Data.csv")
    return df

df = carregar_dados()
st.header("Comparação: Países Desenvolvidos vs. Não Desenvolvidos")

# Checa se as colunas existem
if 'Status' in df.columns and 'Life expectancy ' in df.columns:
    fig = px.box(
        df, x='Status', y='Life expectancy ', color='Status',
        title='Distribuição da expectativa de vida por nível de desenvolvimento',
        color_discrete_map={'Developed': '#48C9B0', 'Developing': '#F1948A'}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Colunas necessárias ('Status', 'Life expectancy ') não encontradas no dataset.")