# import streamlit as st
# from streamlit_option_menu import option_menu
# from menu import home, perguntas, dados, analise, respostas
# from utils.helpers import create_qr_code, add_vertical_space

# st.set_page_config(page_title="Expectativa de Vida (OMS)", layout="wide", page_icon="🌍")

# # Define opções do menu
# menu_options = ["Início", "Perguntas", "Dados", "Análise", "Respostas/Insights"]
# menu_icons = ["house", "question-circle", "layers", "bar-chart", "lightbulb"]

# # Gerenciar redirecionamento sem sobrescrever diretamente menu_selected
# if "redirect_to" in st.session_state:
#     redirect_option = st.session_state.redirect_to
#     default_index = menu_options.index(redirect_option)
#     del st.session_state["redirect_to"]
# else:
#     default_index = 0  # padrão: Início

# with st.sidebar:
#     st.title("Expectativa de Vida (OMS)")
#     selected = option_menu(
#         menu_title=None,
#         options=menu_options,
#         icons=menu_icons,
#         menu_icon="cast",
#         default_index=default_index,
#         orientation="vertical",
#         key="menu_selected",  # manter consistente com rerun
#         styles={
#             "container": {"padding": "0!important", "background-color": "transparent"},
#             "icon": {"color": "#FFD700", "font-size": "25px"},
#             "nav-link": {
#                 "font-size": "16px", 
#                 "text-align": "left", 
#                 "margin": "0px", 
#                 "padding": "10px",
#                 "--hover-color": "rgba(80, 80, 80, 0.7)"
#             },
#             "nav-link-selected": {"background-color": "#02ab21"},
#         }
#     )


# # Direciona conteúdo
# if selected == "Início":
#     home.render(create_qr_code, add_vertical_space)
# elif selected == "Perguntas":
#     perguntas.render()
# elif selected == "Dados":
#     # dados.render(df_cross, df_long)
#     dados.render()
# elif selected == "Análise":
#     # analise.render(df_cross, df_long)
#     analise.render()
# elif selected == "Respostas/Insights":
#     # respostas.render(df_cross, df_long)
#     respostas.render()






# import streamlit as st
# from streamlit_option_menu import option_menu
# from menu import home, perguntas, dados, analise, respostas
# from utils.helpers import create_qr_code, add_vertical_space

# st.set_page_config(page_title="Expectativa de Vida (OMS)", layout="wide", page_icon="🌍")

# # Define opções do menu
# menu_options = ["Início", "Perguntas", "Dados", "Análise", "Respostas/Insights"]
# menu_icons = ["house", "question-circle", "layers", "bar-chart", "lightbulb"]

# # Clave para el widget option_menu en session_state
# MENU_KEY = "menu_selected_option"

# # --- Gestión de la Selección del Menú y Redirección ---
# # 1. Inicializar la selección del menú si aún no existe en session_state
# if MENU_KEY not in st.session_state:
#     st.session_state[MENU_KEY] = menu_options[0]  # Por defecto "Início"

# # 2. Procesar la solicitud de redirección desde otras páginas (ej. perguntas.py)
# if "redirect_to" in st.session_state:
#     redirect_target_page_name = st.session_state.pop("redirect_to") # Leer y eliminar
#     if redirect_target_page_name in menu_options:
#         # Actualizar directamente el estado que option_menu usa (debido a su 'key')
#         st.session_state[MENU_KEY] = redirect_target_page_name
#     # Si redirect_target_page_name no es válido, se quedará con el valor actual de st.session_state[MENU_KEY]


# try:
#     current_default_index = menu_options.index(st.session_state[MENU_KEY])
# except ValueError:
#     current_default_index = 0 
#     st.session_state[MENU_KEY] = menu_options[0]

# # -------- LÍNEA DE DEPURACIÓN --------
# st.toast(f"Página activa para menú: {st.session_state[MENU_KEY]}, Índice: {current_default_index}")
# # ------------------------------------



# # --- Renderizado de la Barra Lateral y Menú ---
# with st.sidebar:
#     st.title("Expectativa de Vida (OMS)")
    
#     # option_menu guardará su selección en st.session_state[MENU_KEY]
#     # y también devolverá la opción seleccionada.
#     # Usamos current_default_index para asegurar que se muestre la opción correcta.
#     selected_page_from_menu = option_menu(
#         menu_title=None,  # "Menu Principal" o None
#         options=menu_options,
#         icons=menu_icons,
#         menu_icon="cast",
#         default_index=current_default_index,
#         orientation="vertical",
#         key=MENU_KEY,  # Muy importante: esta key conecta el widget con st.session_state[MENU_KEY]
#         styles={
#             "container": {"padding": "0!important", "background-color": "transparent"},
#             "icon": {"color": "#FFD700", "font-size": "25px"},
#             "nav-link": {
#                 "font-size": "16px",
#                 "text-align": "left",
#                 "margin": "0px",
#                 "padding": "10px",
#                 "--hover-color": "rgba(80, 80, 80, 0.7)"
#             },
#             "nav-link-selected": {"background-color": "#02ab21"},
#         }
#     )

# # 4. Usar la selección del menú (ya sea la que viene de redirect_to o la seleccionada por el usuario)
# # para decidir qué página renderizar. Es más seguro usar el valor de st.session_state[MENU_KEY]
# # ya que es la fuente de verdad para la selección del menú.
# active_page_to_render = st.session_state[MENU_KEY]


# # --- Direccionamiento del Contenido de la Página ---
# if active_page_to_render == "Início":
#     home.render(create_qr_code, add_vertical_space) # Asegúrate que home.render() puede llamarse sin argumentos si es necesario
# elif active_page_to_render == "Perguntas":
#     perguntas.render()
# elif active_page_to_render == "Dados":
#     dados.render()
# elif active_page_to_render == "Análise":
#     analise.render()
# elif active_page_to_render == "Respostas/Insights":
#     respostas.render() # Esta es la página a la que queremos redirigir



import streamlit as st
from streamlit_option_menu import option_menu
from menu import home, perguntas, dados, analise, respostas
from utils.helpers import create_qr_code, add_vertical_space # Asegúrate que esta importación es correcta




st.set_page_config(page_title="Expectativa de Vida (OMS)", layout="wide", page_icon="🌍")


# Modificar CSS para cambiar el tamaño del texto de botones y selectores
st.markdown("""
    <style>
        /* Aumentar el tamaño del texto en los encabezados */
        .larger-text {
            font-size: 22px;
        }

        h1 {
            font-size: 26px;
        }
        h2 {
            font-size: 22px;
        }
        h3 {
            font-size: 32px;
        }

        /* Aumentar el tamaño del texto en los botones */
        div.stButton > button {
            font-size: 20px;  /* Cambia el tamaño del texto en los botones */
            padding: 14px 26px;  /* Cambia el padding para ajustarlo */
        }

        /* Aumentar el tamaño del texto en los selectores (selectbox, radio) */
        div.stSelectbox > div, div.stRadio > div {
            font-size: 20px;  /* Cambia el tamaño del texto en los selectores */
        }

        /* Aumentar el tamaño de los textos generales (si se desea) */
        .stText {
            font-size: 20px;  /* Cambia el tamaño de todos los textos */
        }
    </style>
""", unsafe_allow_html=True)




menu_options = ["Início", "Perguntas", "Dados", "Análise", "Respostas/Insights"]
menu_icons = ["house", "question-circle", "layers", "bar-chart", "lightbulb"]
MENU_KEY = "menu_selected_option"

# --- Gestión de la Selección del Menú y Redirección ---

# 1. Determinar la página activa ANTES de renderizar el menú
#    La prioridad es: redirect_to > selección manual del menú > default.

if "redirect_to" in st.session_state:
    # Prioridad 1: Redirección activa
    target_page = st.session_state.pop("redirect_to") # Leer y eliminar
    if target_page in menu_options:
        st.session_state[MENU_KEY] = target_page
        active_page_to_render = target_page
    else:
        # Redirección a página inválida, usar valor actual o default
        active_page_to_render = st.session_state.get(MENU_KEY, menu_options[0])
        if active_page_to_render not in menu_options: # Doble check
             active_page_to_render = menu_options[0]
        st.session_state[MENU_KEY] = active_page_to_render

elif MENU_KEY in st.session_state and st.session_state[MENU_KEY] in menu_options:
    # Prioridad 2: Ya hay una selección válida en session_state (de un clic anterior en el menú o redirect)
    active_page_to_render = st.session_state[MENU_KEY]
else:
    # Prioridad 3: Default (primera carga o estado inválido)
    active_page_to_render = menu_options[0]
    st.session_state[MENU_KEY] = active_page_to_render

# En este punto, 'active_page_to_render' tiene la página que DEBE mostrarse.
# Y st.session_state[MENU_KEY] está sincronizado con ella.

# Calcular el default_index para option_menu basado en la página que REALMENTE se va a renderizar
try:
    current_default_index = menu_options.index(active_page_to_render)
except ValueError:
    current_default_index = 0 # Fallback, no debería ocurrir si la lógica anterior es correcta
    active_page_to_render = menu_options[0] # Sincronizar por si acaso
    st.session_state[MENU_KEY] = active_page_to_render


# st.toast(f"Renderizando: {active_page_to_render}, Índice para menú: {current_default_index}, Estado menú SS: {st.session_state.get(MENU_KEY)}")

# --- Renderizado de la Barra Lateral y Menú ---
with st.sidebar:
    st.title("Expectativa de Vida (OMS)")

    # Guardar el estado del menú ANTES de que option_menu lo pueda cambiar
    pre_option_menu_state = st.session_state.get(MENU_KEY)

    selected_page_from_menu_widget = option_menu(
        menu_title=None,
        options=menu_options,
        icons=menu_icons,
        menu_icon="cast",
        default_index=current_default_index, # Este es el índice de 'active_page_to_render'
        key=MENU_KEY, # option_menu leerá st.session_state[MENU_KEY] y lo actualizará si hay un clic
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#FFD700", "font-size": "30px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "left",
                "margin": "0px",
                "padding": "10px",
                "--hover-color": "rgba(80, 80, 80, 0.7)"
            },
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )
    
    # Diagnóstico: ¿option_menu cambió el estado que le dimos?
    post_option_menu_state = st.session_state.get(MENU_KEY)
    if pre_option_menu_state != post_option_menu_state:
        st.warning(f"¡Alerta! option_menu cambió el estado de '{pre_option_menu_state}' a '{post_option_menu_state}'. Valor devuelto por widget: '{selected_page_from_menu_widget}'")
        # Si option_menu cambió el estado, y no fue una redirección, entonces es un clic manual del usuario.
        # En ese caso, la página a renderizar DEBE ser la que el usuario acaba de seleccionar en el menú.
        active_page_to_render = post_option_menu_state # Actualizamos la página a renderizar si el usuario hizo clic en el menú


# --- Direccionamiento del Contenido de la Página ---
# Usamos 'active_page_to_render' que se decidió ANTES o se actualizó por un clic en el menú.
if active_page_to_render == "Início":
    home.render(create_qr_code, add_vertical_space)
elif active_page_to_render == "Perguntas":
    perguntas.render()
elif active_page_to_render == "Dados":
    dados.render()
elif active_page_to_render == "Análise":
    analise.render()
elif active_page_to_render == "Respostas/Insights":
    respostas.render()
else:
    st.error(f"Página desconocida: {active_page_to_render}")
    home.render(create_qr_code, add_vertical_space) # Fallback a inicio








# import streamlit as st
# from streamlit_option_menu import option_menu

# # Importaciones de las páginas del menú (ajusta según tu estructura)
# from menu import home, perguntas, dados, analise, respostas # Asegúrate que respostas esté importado
# from utils.helpers import create_qr_code, add_vertical_space

# # Configuración de la página
# st.set_page_config(page_title="Expectativa de Vida (OMS)", layout="wide", page_icon="🌍")

# # Opciones del menú y claves
# menu_options = ["Início", "Perguntas", "Dados", "Análise", "Respostas/Insights"]
# menu_icons = ["house", "question-circle", "layers", "bar-chart", "lightbulb"]
# MENU_KEY = "active_menu_option"  # La clave que usa option_menu para su estado

# # --- 1. INICIALIZACIÓN DEL ESTADO ---
# if MENU_KEY not in st.session_state:
#     st.session_state[MENU_KEY] = menu_options[0] # Por defecto "Início"

# # También inicializamos selected_question_index si no existe, para evitar errores en respostas.py
# if "selected_question_index" not in st.session_state:
#     st.session_state.selected_question_index = None # O un valor por defecto como 0 o -1

# # --- 2. MANEJO DE REDIRECCIÓN (desde perguntas.py) ---
# # Esto debe ocurrir ANTES de que se renderice el option_menu
# if "redirect_to" in st.session_state:
#     target_page = st.session_state.pop("redirect_to") # Lee y elimina la señal
#     if target_page in menu_options:
#         # Actualiza la clave que option_menu usa para su selección
#         st.session_state[MENU_KEY] = target_page
#         # No se necesita st.rerun() aquí, porque perguntas.py ya lo hizo.
#         # El script continuará y option_menu usará el MENU_KEY actualizado.
#     # selected_question_index ya fue establecido por perguntas.py

# # --- 3. BARRA LATERAL Y MENÚ ---
# with st.sidebar:
#     st.title("Expectativa de Vida (OMS)")

#     # option_menu leerá su default_index de st.session_state[MENU_KEY]
#     # y también actualizará st.session_state[MENU_KEY] si el usuario hace clic.
#     selected_by_user_click = option_menu(
#         menu_title=None,
#         options=menu_options,
#         icons=menu_icons,
#         menu_icon="cast",
#         default_index=menu_options.index(st.session_state[MENU_KEY]),
#         key=MENU_KEY,
#         orientation="vertical",
#         styles={
#             "container": {"padding": "0!important", "background-color": "transparent"},
#             "icon": {"color": "#FFD700", "font-size": "25px"},
#             "nav-link": {
#                 "font-size": "16px",
#                 "text-align": "left",
#                 "margin": "0px",
#                 "padding": "10px",
#                 "--hover-color": "rgba(80, 80, 80, 0.7)",
#             },
#             "nav-link-selected": {"background-color": "#02ab21"},
#         }
#     )
#     # A estas alturas, st.session_state[MENU_KEY] refleja la selección actual
#     # (ya sea por redirección o por clic del usuario en el menú)

# # --- 4. DEP DEBUG TOASTS ---
# # st.toast(f"Página activa en MENU_KEY: {st.session_state[MENU_KEY]}")
# # if st.session_state.get("selected_question_index") is not None:
# #     st.toast(f"Índice de pregunta seleccionado: {st.session_state.selected_question_index}")


# # --- 5. RENDERIZADO DEL CONTENIDO DE LA PÁGINA ---
# active_page_to_render = st.session_state[MENU_KEY]

# if active_page_to_render == "Início":
#     home.render(create_qr_code, add_vertical_space)
# elif active_page_to_render == "Perguntas":
#     perguntas.render() # perguntas.py se encargará de la lógica de st.session_state.redirect_to
# elif active_page_to_render == "Dados":
#     dados.render()
# elif active_page_to_render == "Análise":
#     analise.render()
# elif active_page_to_render == "Respostas/Insights":
#     respostas.render() # respostas.py deberá usar st.session_state.selected_question_index
# else:
#     st.error(f"Página desconocida: '{active_page_to_render}'. Mostrando 'Início'.")
#     st.session_state[MENU_KEY] = menu_options[0] # Resetear
#     home.render(create_qr_code, add_vertical_space)