import streamlit as st

def render():
    # =========================
    # TÍTULO
    # =========================
    st.markdown("## 🎯 ¿Qué medimos en un estudio de percepción?")

    st.write(
        "Un estudio de percepción permite evaluar **dimensiones emocionales, cognitivas, "
        "actitudinales, comportamentales y simbólicas** asociadas a una organización, "
        "marca o institución."
    )

    st.divider()

    # =========================
    # DIMENSIONES PRINCIPALES
    # =========================
    st.markdown("### 🔍 Dimensiones clave que se analizan")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 💬 Opinión")
            st.write(
                "Evalúa **qué piensa** la gente sobre la organización, "
                "sus servicios, programas o actuaciones."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 💛 Emociones")
            st.write(
                "Analiza los **sentimientos asociados** a la experiencia: "
                "confianza, miedo, satisfacción, frustración, esperanza."
            )

    with col3:
        with st.container(border=True):
            st.markdown("### 🔄 Comportamiento")
            st.write(
                "Observa **cómo actúan** las personas y "
                "qué decisiones toman frente a la organización."
            )

    # =========================
    # SEGUNDA FILA
    # =========================
    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            st.markdown("### 🧠 Cognición")
            st.write(
                "Mide **qué sabe o cree** la población: nivel de información, "
                "conocimiento de programas, comprensión de procesos."
            )

    with col5:
        with st.container(border=True):
            st.markdown("### ⚖️ Actitudes")
            st.write(
                "Evalúa la **predisposición** a apoyar, rechazar, participar "
                "o colaborar con la institución."
            )

    with col6:
        with st.container(border=True):
            st.markdown("### 🤝 Confianza y legitimidad")
            st.write(
                "Analiza la **credibilidad**, transparencia percibida "
                "y legitimidad de la institución."
            )

    # =========================
    # TERCERA FILA
    # =========================
    col7, col8 = st.columns(2)

    with col7:
        with st.container(border=True):
            st.markdown("### 🎯 Expectativas")
            st.write(
                "Identifica **qué espera la gente** que ocurra: "
                "mejoras, respuestas, acompañamiento o resultados futuros."
            )

    with col8:
        with st.container(border=True):
            st.markdown("### 🌐 Valoración simbólica")
            st.write(
                "Explora **significados, narrativas, estigmas o símbolos** "
                "asociados a la organización o al tema analizado."
            )

    # =========================
    # CIERRE ANALÍTICO
    # =========================
    with st.container(border=True):
        st.info(
            "📌 **Estas dimensiones permiten construir indicadores sintéticos "
            "y modelos explicativos**, facilitando la toma de decisiones "
            "basadas en evidencia y percepción social."
        )
