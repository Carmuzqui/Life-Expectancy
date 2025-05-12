# import streamlit as st

# def render():
#     st.markdown("## ❓ O conjunto de dados visa responder às seguintes perguntas:")

#     perguntas = [
#         "Os vários fatores preditivos inicialmente escolhidos realmente afetam a expectativa de vida?",
#         "Quais são as variáveis ​​preditivas que realmente afetam a expectativa de vida?",
#         "Um país com uma expectativa de vida menor (<65 anos) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?",
#         "Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?",
#         "Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?",
#         "A expectativa de vida tem relação positiva ou negativa com o consumo de álcool?",
#         "Países densamente povoados tendem a ter menor expectativa de vida?",
#         "Qual é o impacto da cobertura vacinal na expectativa de vida?"
#     ]

#     st.markdown("---")

#     for i, pergunta in enumerate(perguntas, 1):
#         if st.button(f"{i} ) {pergunta}", key=f"q{i}"):
#             st.session_state.redirect_to = "Respostas/Insights"
#             st.rerun()

#     st.markdown("---")

#     st.markdown("""
#     <div style='text-align: center; color: gray;'>
#         As respostas serão disponibilizadas na seção 
#         <a href='#' id='respostas-link'><b>Respostas/Insights</b></a>
#     </div>

#     <script>
#     const link = window.parent.document.getElementById('respostas-link');
#     if (link) {
#         link.onclick = function() {
#             window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'Respostas/Insights'}, '*');
#         }
#     }
#     </script>
#     """, unsafe_allow_html=True)

#     # Backup interno para garantir redirecionamento em back-end
#     for k, v in st.session_state.items():
#         if isinstance(v, str) and v == "Respostas/Insights":
#             st.session_state.redirect_to = "Respostas/Insights"
#             st.rerun()





# # perguntas.py

# import streamlit as st

# def render():
#     st.markdown("## ❓ O conjunto de dados visa responder às seguintes perguntas:")

#     # Esta lista de textos de perguntas debe ser consistente en orden
#     # con cómo se generan las claves en respostas.py
#     perguntas_textos = [
#         "Os vários fatores preditivos inicialmente escolhidos realmente afetam a expectativa de vida?",
#         "Quais são as variáveis ​​preditivas que realmente afetam a expectativa de vida?",
#         "Um país com uma expectativa de vida menor (<65 anos) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?",
#         "Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?",
#         "Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?",
#         "A expectativa de vida tem relação positiva ou negativa com o consumo de álcool?",
#         "Países densamente povoados tendem a ter menor expectativa de vida?",
#         "Qual é o impacto da cobertura vacinal na expectativa de vida?"
#     ]

#     st.markdown("---")

#     # Generamos los botones. Guardamos el índice de la pregunta (0-based).
#     for i, pergunta_texto in enumerate(perguntas_textos):
#         # El key del botón debe ser único
#         if st.button(f"{i + 1} ) {pergunta_texto}", key=f"btn_pergunta_{i}"):
#             st.session_state.redirect_to = "Respostas/Insights"
#             # Guardamos el índice de la pregunta que se debe seleccionar en respostas.py
#             st.session_state.selected_question_index = i
#             st.rerun()

#     st.markdown("---")

#     st.markdown("""
#     <div style='text-align: center; color: gray;'>
#         As respostas serão disponibilizadas na seção 
#         <a href='#' id='respostas-link'><b>Respostas/Insights</b></a>
#     </div>

#     <script>
#     const link = window.parent.document.getElementById('respostas-link');
#     if (link) {
#         link.onclick = function() {
#             // Este script solo puede cambiar la página, no el estado interno del selectbox
#             // Para que funcione completamente, también debería establecer selected_question_index
#             // pero es más complejo desde JS puro sin una función de callback de Streamlit.
#             // Por ahora, este script solo redirige.
#             window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'Respostas/Insights'}, '*');
#         }
#     }
#     </script>
#     """, unsafe_allow_html=True)

#     # El backup interno no es estrictamente necesario si el st.rerun() ya está en los botones.
#     # Lo comentaré por ahora, pero puedes descomentarlo si ves algún caso donde no redirige.
#     # for k, v in st.session_state.items():
#     #     if isinstance(v, str) and v == "Respostas/Insights" and "redirect_to" not in st.session_state:
#     #         st.session_state.redirect_to = "Respostas/Insights"
#     #         # No es necesario selected_question_index aquí si no vino de un botón.
#     #         st.rerun()





# perguntas.py
import streamlit as st

def render():
    st.markdown("## ❓ O conjunto de dados visa responder às seguintes perguntas:")

    perguntas_textos = [
        "Os vários fatores preditivos inicialmente escolhidos realmente afetam a expectativa de vida?",
        "Quais são as variáveis ​​preditivas que realmente afetam a expectativa de vida?",
        "Um país com uma expectativa de vida menor (<65 anos) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?",
        "Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?",
        "Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?",
        "A expectativa de vida tem relação positiva ou negativa com o consumo de álcool?",
        "Países densamente povoados tendem a ter menor expectativa de vida?",
        "Qual é o impacto da cobertura vacinal na expectativa de vida?"
    ]

    st.markdown("---")

    for i, pergunta_texto in enumerate(perguntas_textos):
        # La key del botón debe ser única para cada botón
        if st.button(f"{i + 1} ) {pergunta_texto}", key=f"btn_pergunta_{i}"):
            st.session_state.redirect_to = "Respostas/Insights"
            # ¡IMPORTANTE! Guardamos el índice de la pregunta (0-based)
            st.session_state.selected_question_index = i 
            st.rerun() # Vuelve a ejecutar la app desde main.py

    st.markdown("---")

    st.markdown("""
    <div style='text-align: center; color: gray;'>
        As respostas serão disponibilizadas na seção 
        <a href='#' id='respostas-link-js'><b>Respostas/Insights</b></a>
    </div>
    <script>
    // Script para el enlace (solo redirige la página, no selecciona pregunta)
    const link = window.parent.document.getElementById('respostas-link-js');
    if (link) {
        link.onclick = function(event) {
            event.preventDefault(); // Prevenir comportamiento por defecto del enlace
            // Esto intentará cambiar la selección del menú en main.py
            // Necesita que el componente option_menu esté escuchando este tipo de mensaje
            // o que main.py tenga una forma de manejarlo.
            // Para simplificar, nos enfocaremos en los botones de Streamlit por ahora.
            // Esta forma de cambiar la página puede ser menos fiable que el st.rerun de los botones.
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                key: 'menu_selected_option', // La key de tu option_menu en main.py
                value: 'Respostas/Insights'
            }, '*');
        }
    }
    </script>
    """, unsafe_allow_html=True)