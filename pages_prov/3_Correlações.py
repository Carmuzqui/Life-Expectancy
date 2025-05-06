# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/Life Expectancy Data.csv")
#     return df

# df = load_data()
# st.header("Correlación entre variables")
# corr = df.corr(numeric_only=True)
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
# st.pyplot(fig)


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/Life Expectancy Data.csv")
    return df

df = carregar_dados()
st.header("Correlação entre variáveis numéricas")

# Calcula matriz de correlação
corr = df.corr(numeric_only=True)
# Heatmap com Seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)