import streamlit as st

# =========================
# CONFIGURACIÓN GENERAL
# =========================
st.set_page_config(
    page_title="Algebra Labs – Percepción 360",
    page_icon="✨",
    layout="wide"
)

# =========================
# ESTILOS GLOBALES
# =========================
# with open("styles.css", encoding="utf-8") as f:
#    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# IMPORTAR VISTAS
# =========================
import _1_Portada as portada
import _2_Que_es_la_percepcion as percepcion
import _3_Fundamentos as fundamentos
import _4_Tipos_de_estudios as tipos
import _5_Que_medimos as medimos
import _6_Metodologia as metodologia
import _7_Pipeline as pipeline
import _8_Demo as demo
import _9_Cierre as cierre

# =========================
# SIDEBAR (VISIBLE)
# =========================
st.sidebar.image("assets/logo_algebralabs.png", use_container_width=False)

page = st.sidebar.radio(
    "Navegación",
    [
        "📱 Portada",
        "🧠 ¿Qué es la percepción?",
        "📚 ¿Qué es un estudio de percepción?",
        "📊 Tipos de estudios",
        "🎯 Qué medimos",
        "🔬 Metodología",
        "🧬 Pipeline Algebra Labs",
        "🧪 Estudios de percepciones realizados",
        "🏁 Diagnóstico y levantamiento de necesidades"
    ]
)

# =========================
# ROUTER
# =========================


if page == "📱 Portada":
    portada.render()
elif page == "🧠 ¿Qué es la percepción?":
    percepcion.render()
elif page == "📚 ¿Qué es un estudio de percepción?":
    fundamentos.render()
elif page == "📊 Tipos de estudios":
    tipos.render()
elif page == "🎯 Qué medimos":
    medimos.render()
elif page == "🔬 Metodología":
    metodologia.render()
elif page == "🧬 Pipeline Algebra Labs":
    pipeline.render()
elif page == "🧪 Estudios de percepciones realizados":
    demo.render()
elif page == "🏁 Diagnóstico y levantamiento de necesidades":
    cierre.render()


# =========================
# CONTROL DE CAMBIO DE PÁGINA
# =========================

if "current_page" not in st.session_state:
    st.session_state.current_page = page

# Si cambió la página, limpiamos estados específicos
if st.session_state.current_page != page:
    if st.session_state.current_page == "📱 Portada":
        st.session_state.pop("portada_index", None)
    st.session_state.current_page = page
