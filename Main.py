# import streamlit as st
# from streamlit_option_menu import option_menu
# from menu import home, transversal, longitudinal, metricas
# from utils.helpers import load_data, create_qr_code, add_vertical_space

# st.set_page_config(page_title="Expectativa de Vida (OMS)", layout="wide", page_icon="🌍")

# def main():
#     df_cross, df_long = load_data()

#     with st.sidebar:
#         st.title("Expectativa de Vida (OMS)")
#         selected = option_menu(
#             menu_title=None,
#             options=["Início", "Dados", "Análise", "Métricas"],
#             icons=["house", "layers", "graph-up", "clipboard-data"],
#             menu_icon="cast",
#             default_index=0,
#             orientation="vertical",
#             styles={
#                 "container": {"padding": "0!important", "background-color": "transparent"},
#                 "icon": {"color": "#FFD700", "font-size": "25px"},
#                 "nav-link": {
#                     "font-size": "16px", 
#                     "text-align": "left", 
#                     "margin": "0px", 
#                     "padding": "10px",
#                     "--hover-color": "rgba(80, 80, 80, 0.7)"
#                 },
#                 "nav-link-selected": {"background-color": "#02ab21"},
#             }
#         )

#     if selected == "Início":
#         home.render(df_cross, create_qr_code, add_vertical_space)
#     elif selected == "Transversal":
#         transversal.render(df_cross)
#     elif selected == "Longitudinal":
#         longitudinal.render(df_long)
#     elif selected == "Métricas":
#         metricas.render(df_cross, df_long)

# if __name__ == "__main__":
#     main()








# import streamlit as st
# from streamlit_option_menu import option_menu
# from menu import home, perguntas, dados, analise, respostas
# from utils.helpers import load_data, create_qr_code, add_vertical_space

# st.set_page_config(page_title="Expectativa de Vida (OMS)", layout="wide", page_icon="🌍")

# def main():
#     df_cross, df_long = load_data()

#     with st.sidebar:
#         st.title("Expectativa de Vida (OMS)")
#         selected = option_menu(
#             menu_title=None,
#             options=["Início", "Perguntas", "Dados", "Análise", "Respostas/Insights"],
#             icons=["house", "question-circle", "layers", "graph-up", "lightbulb"],
#             menu_icon="cast",
#             default_index=0,
#             orientation="vertical",
#             styles={
#                 "container": {"padding": "0!important", "background-color": "transparent"},
#                 "icon": {"color": "#FFD700", "font-size": "25px"},
#                 "nav-link": {
#                     "font-size": "16px", 
#                     "text-align": "left", 
#                     "margin": "0px", 
#                     "padding": "10px",
#                     "--hover-color": "rgba(80, 80, 80, 0.7)"
#                 },
#                 "nav-link-selected": {"background-color": "#02ab21"},
#             }
#         )

#     if selected == "Início":
#         home.render(df_cross, create_qr_code, add_vertical_space)
#     elif selected == "Perguntas":
#         perguntas.render()
#     elif selected == "Dados":
#         dados.render(df_cross, df_long)
#     elif selected == "Análise":
#         analise.render(df_cross, df_long)
#     elif selected == "Respostas/Insights":
#         respostas.render(df_cross, df_long)

# if __name__ == "__main__":
#     main()





import streamlit as st
from streamlit_option_menu import option_menu
from menu import home, perguntas, dados, analise, respostas
from utils.helpers import load_data, create_qr_code, add_vertical_space

st.set_page_config(page_title="Expectativa de Vida (OMS)", layout="wide", page_icon="🌍")

# Define opções do menu
menu_options = ["Início", "Perguntas", "Dados", "Análise", "Respostas/Insights"]
menu_icons = ["house", "question-circle", "layers", "bar-chart", "lightbulb"]

# Gerenciar redirecionamento sem sobrescrever diretamente menu_selected
if "redirect_to" in st.session_state:
    redirect_option = st.session_state.redirect_to
    default_index = menu_options.index(redirect_option)
    del st.session_state["redirect_to"]
else:
    default_index = 0  # padrão: Início

with st.sidebar:
    st.title("Expectativa de Vida (OMS)")
    selected = option_menu(
        menu_title=None,
        options=menu_options,
        icons=menu_icons,
        menu_icon="cast",
        default_index=default_index,
        orientation="vertical",
        key="menu_selected",  # manter consistente com rerun
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#FFD700", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "0px", 
                "padding": "10px",
                "--hover-color": "rgba(80, 80, 80, 0.7)"
            },
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Carrega dados
df_cross, df_long = load_data()

# Direciona conteúdo
if selected == "Início":
    home.render(df_cross, create_qr_code, add_vertical_space)
elif selected == "Perguntas":
    perguntas.render()
elif selected == "Dados":
    # dados.render(df_cross, df_long)
    dados.render()
elif selected == "Análise":
    # analise.render(df_cross, df_long)
    analise.render()
elif selected == "Respostas/Insights":
    # respostas.render(df_cross, df_long)
    respostas.render()
