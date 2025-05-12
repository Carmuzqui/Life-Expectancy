import streamlit as st
import io

def render(create_qr_code, add_vertical_space):
    st.header("Bem-vindo a uma análise estatística dos fatores que influenciam a Expectativa de Vida")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Vídeo introdutório da OMS: expectativa de vida aumentou 5 anos desde 2000")
        video_file = open('media/expectativa-de-vida.mp4', 'rb')
        st.video(video_file.read())
        st.markdown("""
        <div style="font-size: 1.0em; color: gray; text-align: center; margin-top: 5px;">
        Fonte: <a href="https://youtu.be/wFuVJUf_cao" >AFP Português</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        add_vertical_space(2)
        st.write("Principais recursos:")
        st.write("• Processamento de dados")
        st.write("• Análise de dados")
        st.write("• Insights sobre Expectativa de Vida")
        

        url = "https://expectativa-de-vida.streamlit.app/"
        qr_img = create_qr_code(url, fill_color="black", back_color="white")
        img_byte_arr = io.BytesIO()
        qr_img.save(img_byte_arr, format='PNG')
        st.image(img_byte_arr.getvalue(), caption='Escaneie para acessar o dashboard')
