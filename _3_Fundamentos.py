import streamlit as st

def render():
    # =========================
    # TÍTULO
    # =========================
    st.markdown("## 🧠 ¿Qué es un estudio de percepción?")

    st.write(
        "Un **estudio de percepción** es una metodología que permite medir cómo piensa, "
        "siente o interpreta una población sobre un tema, institución, servicio, situación "
        "o grupo social.\n\n"
        "No busca hechos objetivos, sino **representaciones subjetivas**, tales como:"
    )

    st.markdown(
        """
        - Creencias  
        - Sensaciones  
        - Miedos  
        - Confianza  
        - Satisfacción  
        - Valoraciones  
        - Expectativas  
        """
    )

    with st.container(border=True):
        st.info(
            "📌 **Un estudio de percepción se utiliza para entender cómo la gente interpreta "
            "la realidad, no necesariamente cómo la realidad es.**"
        )

    # =========================
    # USOS
    # =========================
    st.markdown("## 🎯 ¿Para qué sirve o en qué se utiliza?")

    # =========================
    # TARJETAS / BLOQUES
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 🔍 Gestión pública")
            st.markdown(
                """
                - Medir satisfacción con servicios públicos (salud, educación, justicia).  
                - Evaluar niveles de confianza institucional.  
                - Diagnosticar percepción de seguridad o convivencia.  
                - Monitorear la reputación de programas públicos (vivienda, subsidios, búsqueda de personas desaparecidas).  
                """
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 🎭 Programas sociales")
            st.markdown(
                """
                - Entender emociones, expectativas y niveles de confianza hacia las instituciones.  
                - Evaluar percepción de acompañamiento, respeto y trato digno.  
                - Identificar barreras simbólicas que afectan la participación.  
                - Medir impacto emocional de proyectos de memoria, reparación o atención psicosocial.  
                """
            )

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.markdown("### 📚 Empresas y entornos privados")
            st.markdown(
                """
                - Identificar fortalezas y debilidades desde la mirada del cliente o del colaborador.  
                - Analizar la percepción de marca, servicio y experiencia.  
                - Evaluar niveles de satisfacción y recomendación.  
                - Detectar riesgos reputacionales.  
                """
            )

    with col4:
        with st.container(border=True):
            st.markdown("### 🌐 Psicología y rehabilitación")
            st.markdown(
                """
                - Evaluar déficits o alteraciones en la percepción sensorial.  
                - Diseñar programas de rehabilitación para mejorar funciones perceptivas y cognitivas.  
                - Analizar patrones y tendencias del comportamiento humano.  
                """
            )
