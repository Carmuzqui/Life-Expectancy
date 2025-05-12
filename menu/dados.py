import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns







def render():
    st.header("🔍 Exploração dos dados")

    with st.spinner("Carregando os dados..."):
        df = pd.read_csv("dados/Life Expectancy Data.csv")
        df.columns = df.columns.str.strip()  # Remove espaços nos nomes das colunas

    st.subheader("📁 Informações iniciais")
    with st.expander("👁️ Visualizar primeiras linhas"):
        st.dataframe(df.head())

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Linhas", df.shape[0])
    with col2:
        st.metric("Colunas", df.shape[1])

    with st.expander("📑 Tipos de dados e estrutura"):
        buffer = df.dtypes.astype(str)
        st.write(buffer)

    with st.expander("⚠️ Valores ausentes"):
        missing = df.isnull().sum()
        missing_percent = (missing / df.shape[0]) * 100
        st.dataframe(pd.DataFrame({
            "Ausentes": missing,
            "%": missing_percent.round(2)
        }).sort_values(by="%", ascending=False))

    with st.expander("🔁 Linhas duplicadas"):
        st.write(f"Número de linhas duplicadas: **{df.duplicated().sum()}**")

    st.subheader("📈 Análise estatística")

    with st.expander("📊 Resumo estatístico das variáveis numéricas"):
        st.dataframe(df.describe().transpose())

    with st.expander("📋 Resumo das variáveis categóricas"):
        st.dataframe(df.describe(include="object").transpose())

    st.subheader("📦 Boxplots para detecção de outliers")
    numerical_cols = df.select_dtypes(include="number").columns
    fig, axes = plt.subplots(5, 4, figsize=(20, 15))
    axes = axes.flatten()

    for i, col in enumerate(numerical_cols):
        sns.boxplot(y=df[col], ax=axes[i], color="lightblue")
        axes[i].set_title(col, fontsize=9)
        axes[i].set_xlabel("")
        axes[i].set_ylabel("")

    for j in range(len(numerical_cols), 20):
        fig.delaxes(axes[j])

    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("📊 Distribuição das variáveis numéricas")
    fig, axes = plt.subplots(5, 4, figsize=(20, 15))
    axes = axes.flatten()

    for i, col in enumerate(numerical_cols):
        sns.histplot(df[col], ax=axes[i], bins=30, color="skyblue", edgecolor="black")
        axes[i].set_title(col, fontsize=9)

    for j in range(len(numerical_cols), 20):
        fig.delaxes(axes[j])

    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("📈 Densidade de probabilidade (KDE)")
    fig, axes = plt.subplots(5, 4, figsize=(20, 15))
    axes = axes.flatten()

    for i, col in enumerate(numerical_cols):
        sns.kdeplot(df[col], ax=axes[i], fill=True, color="seagreen")
        axes[i].set_title(col, fontsize=9)

    for j in range(len(numerical_cols), 20):
        fig.delaxes(axes[j])

    plt.tight_layout()
    st.pyplot(fig)
