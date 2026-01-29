import streamlit as st

def render():
    # =========================
    # TÍTULO
    # =========================
    st.markdown("## 🔬 Metodología")
    st.caption("Cómo entendemos la percepción y la transformamos en conocimiento útil")

    st.write(
        "La **metodología** define el enfoque conceptual del estudio: "
        "es decir, **cómo pensamos y analizamos la percepción**.\n\n"
        "El *pipeline* corresponde a lo operativo; "
        "la metodología es el **marco estratégico** que guía todo el análisis."
    )

    st.divider()

    # ======================================================
    # COMPONENTES METODOLÓGICOS
    # ======================================================
    with st.container(border=True):
        st.markdown("### 🧠 1. Enfoque mixto")
        st.write(
            "Combinamos metodologías **cuantitativas y cualitativas** "
            "para captar la percepción desde múltiples ángulos. "
            "Esto incluye mediciones numéricas, análisis emocional, "
            "narrativas y experiencia reportada."
        )

    with st.container(border=True):
        st.markdown("### 📊 2. Modelo de percepción")
        st.write(
            "Definimos **dimensiones clave** que estructuran el análisis, "
            "como confianza, claridad, experiencia, satisfacción, "
            "narrativa percibida y coherencia institucional."
        )

    with st.container(border=True):
        st.markdown("### 👥 3. Segmentación y grupos")
        st.write(
            "Analizamos diferencias entre grupos poblacionales según "
            "edad, rol, nivel de exposición, interacción previa, "
            "territorio o tipo de experiencia."
        )

    with st.container(border=True):
        st.markdown("### 🧩 4. Análisis estructural")
        st.write(
            "Evaluamos cómo se relacionan las variables entre sí "
            "y qué factores tienen mayor peso en la percepción general, "
            "utilizando modelos estadísticos y analíticos."
        )

    with st.container(border=True):
        st.markdown("### 📈 5. Evolución temporal")
        st.write(
            "Monitoreamos los cambios en el tiempo para identificar "
            "mejoras, riesgos emergentes o momentos críticos "
            "en la percepción."
        )

    with st.container(border=True):
        st.markdown("### 💡 6. Insights transformadores")
        st.write(
            "La metodología asegura que los hallazgos no sean "
            "datos aislados, sino **insumos estratégicos** "
            "que orientan decisiones, ajustes y acciones concretas."
        )

    # =========================
    # CIERRE
    # =========================
    with st.container(border=True):
        st.info(
            "📌 **Una metodología sólida permite transformar la percepción "
            "en evidencia estructurada, trazable y accionable para la toma de decisiones.**"
        )
