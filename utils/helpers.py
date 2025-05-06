import streamlit as st
import numpy as np
import pandas as pd
import qrcode
import io

@st.cache_data
def load_data():
    df_cross = pd.read_csv("dados/oasis_cross-sectional.csv")
    df_long = pd.read_csv("dados/oasis_longitudinal.csv")
    return df_cross, df_long

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
