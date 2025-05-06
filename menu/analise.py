import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer

def render():
    st.markdown("## 📊 Tratamento e Análise dos Dados")

    # Carregar e padronizar colunas localmente
    df = pd.read_csv("dados/Life Expectancy Data.csv")
    df.columns = df.columns.str.strip()

    st.markdown("### 📌 Imputação de valores faltantes")
    st.write("Usamos o algoritmo KNN (K-Nearest Neighbors) para estimar e preencher os valores ausentes com base em padrões similares.")

    imputer = KNNImputer()
    for col in df.select_dtypes(include="number").columns:
        df[col] = imputer.fit_transform(df[[col]])

    st.success("Valores ausentes imputados com sucesso.")

    st.markdown("---")
    st.markdown("### 📌 Análise de outliers com o método IQR")
    
    def wisker_bounds(col):
        q1, q3 = np.percentile(col, [25, 75])
        iqr = q3 - q1
        return q1 - 1.5 * iqr, q3 + 1.5 * iqr

    numerical_cols = df.select_dtypes(include="number").columns
    outlier_percent = {
        col: round(100 * ((df[col] < wisker_bounds(df[col])[0]) | (df[col] > wisker_bounds(df[col])[1])).sum() / len(df), 2)
        for col in numerical_cols
    }

    st.dataframe(pd.DataFrame.from_dict(outlier_percent, orient='index', columns=['% de Outliers']).sort_values('% de Outliers', ascending=False))

    st.markdown("### 📌 Tratamento de outliers por IQR")
    treated_cols = [
        'Year', 'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure',
        'Hepatitis B', 'Measles', 'BMI', 'under-five deaths', 'Polio', 'Total expenditure',
        'Diphtheria', 'HIV/AIDS', 'GDP', 'Population', 'thinness  1-19 years',
        'thinness 5-9 years', 'Income composition of resources', 'Schooling'
    ]
    for col in treated_cols:
        lw, uw = wisker_bounds(df[col])
        df[col] = np.clip(df[col], lw, uw)

    st.success("Outliers tratados com substituição pelos limites IQR.")

    st.markdown("### 📌 Boxplots Após Tratamento")
    fig1, axes = plt.subplots(5, 4, figsize=(20, 15))
    axes = axes.flatten()
    for i, col in enumerate(treated_cols):
        sns.boxplot(y=df[col], ax=axes[i])
        axes[i].set_title(col, fontsize=10)
        axes[i].set_xlabel('')
    for j in range(len(treated_cols), 20):
        fig1.delaxes(axes[j])
    st.pyplot(fig1)

    st.markdown("### 📌 Distribuição das variáveis numéricas")
    fig2, axes = plt.subplots(5, 4, figsize=(20, 15))
    axes = axes.flatten()
    for i, col in enumerate(numerical_cols):
        sns.histplot(df[col], ax=axes[i], bins=30)
        axes[i].set_title(col, fontsize=10)
    for j in range(len(numerical_cols), 20):
        fig2.delaxes(axes[j])

    plt.tight_layout()
    st.pyplot(fig2)

    st.markdown("### 📌 Densidade de probabilidade (PDF)")
    fig3, axes = plt.subplots(5, 4, figsize=(20, 15))
    axes = axes.flatten()
    for i, col in enumerate(numerical_cols):
        sns.kdeplot(df[col], ax=axes[i], fill=True, color="seagreen")
        axes[i].set_title(col, fontsize=10)
    for j in range(len(numerical_cols), 20):
        fig3.delaxes(axes[j])

    plt.tight_layout()
    st.pyplot(fig3)

   

    st.markdown("### 📌 Estatísticas descritivas Pós-tratamento")
    st.dataframe(df.describe())
