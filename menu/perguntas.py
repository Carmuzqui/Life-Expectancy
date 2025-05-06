# import streamlit as st

# def render():
#     st.markdown("## 🔍 O conjunto de dados visa responder às seguintes perguntas:")

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
#         if st.button(f"❓ {pergunta}", key=f"q{i}"):
#             st.switch_page("main.py")  # redireciona para Respostas/Insights (simulação temporária)
#             # No futuro: st.experimental_set_query_params(pergunta=i) ou usar navegação por hash/ancla

#     st.markdown("---")
#     st.markdown("<div style='text-align: center; color: gray;'>As respostas serão disponibilizadas na seção <b>Respostas/Insights</b></div>", unsafe_allow_html=True)







# import streamlit as st

# def render():
#     st.markdown("## 🔍 O conjunto de dados visa responder às seguintes perguntas:")

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
#         if st.button(f"❓ {pergunta}", key=f"q{i}"):
#             st.session_state["menu_option"] = "Respostas/Insights"
#             st.experimental_rerun()

#     st.markdown("---")
#     st.markdown("""
#     <div style='text-align: center; color: gray;'>
#         As respostas serão disponibilizadas na seção 
#         <a href='#' onclick="window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'Respostas/Insights'}, '*');">
#         <b>Respostas/Insights</b></a>
#     </div>
#     """, unsafe_allow_html=True)





import streamlit as st

def render():
    st.markdown("## ❓ O conjunto de dados visa responder às seguintes perguntas:")

    perguntas = [
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

    for i, pergunta in enumerate(perguntas, 1):
        if st.button(f"{i} ) {pergunta}", key=f"q{i}"):
            st.session_state.redirect_to = "Respostas/Insights"
            st.rerun()

    st.markdown("---")

    st.markdown("""
    <div style='text-align: center; color: gray;'>
        As respostas serão disponibilizadas na seção 
        <a href='#' id='respostas-link'><b>Respostas/Insights</b></a>
    </div>

    <script>
    const link = window.parent.document.getElementById('respostas-link');
    if (link) {
        link.onclick = function() {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'Respostas/Insights'}, '*');
        }
    }
    </script>
    """, unsafe_allow_html=True)

    # Backup interno para garantir redirecionamento em back-end
    for k, v in st.session_state.items():
        if isinstance(v, str) and v == "Respostas/Insights":
            st.session_state.redirect_to = "Respostas/Insights"
            st.rerun()
