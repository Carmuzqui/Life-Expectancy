import streamlit as st
import numpy as np
import pandas as pd
import json
import qrcode
import io



def create_qr_code(url, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

def add_vertical_space(num_lines: int = 1):
    for _ in range(num_lines):
        st.markdown('<br>', unsafe_allow_html=True)

def wisker_bounds(col):
    q1, q3 = np.percentile(col, [25, 75])
    iqr = q3 - q1
    lw = q1 - 1.5 * iqr
    uw = q3 + 1.5 * iqr
    return lw, uw




def add_population_density_column(df_vida, path_densidade_csv="dados/densidade_populacao.csv", path_codigos_json="dados/codigos_paises.json"):
    """
    Adiciona a coluna 'Population density' ao DataFrame de expectativa de vida,
    cruzando por código do país (Country Code) e ano.
    """
    # Carrega o dicionário nome → código
    with open(path_codigos_json, "r", encoding="utf-8") as f:
        name_to_code = json.load(f)

    # Adiciona 'Country Code' ao df_vida
    df_vida["Country Code"] = df_vida["Country"].map(name_to_code)
    df_vida["Year"] = df_vida["Year"].astype(int)

    # Leitura do CSV bruto (sem skiprows)
    df_dens = pd.read_csv(path_densidade_csv, skiprows=4)

    # Verifica colunas de interesse
    colunas_anos = [str(ano) for ano in range(2000, 2016)]
    colunas_desejadas = ["Country Code"] + colunas_anos
    df_dens = df_dens[colunas_desejadas].copy()

    # Elimina linhas com código nulo
    df_dens = df_dens[df_dens["Country Code"].notna()]

    # Transforma em formato longo
    df_dens_long = df_dens.melt(id_vars="Country Code",
                                var_name="Year",
                                value_name="Population density")
    df_dens_long["Year"] = df_dens_long["Year"].astype(int)

    # Faz o merge usando Country Code + Year
    df_final = df_vida.merge(df_dens_long, on=["Country Code", "Year"], how="left")

    return df_final
