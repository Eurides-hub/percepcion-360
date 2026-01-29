import streamlit as st

def render():
    # =========================
    # TÍTULO
    # =========================
    st.markdown("## 🧬 Pipeline Algebra Labs")

    st.write(
        "El **Pipeline Algebra Labs** es el flujo operativo y tecnológico que "
        "transforma la percepción en **datos estructurados** y en **decisiones accionables**.\n\n"
        "A diferencia de la *metodología* —que define el **enfoque conceptual** del estudio—, "
        "el pipeline describe **cómo fluyen los datos en la práctica**, "
        "qué herramientas se utilizan y cómo se garantiza velocidad, calidad y consistencia."
    )

    st.divider()

    # ======================================================
    # 1. CAPTURA
    # ======================================================
    with st.container(border=True):
        st.markdown("### 🔁 1. Captura de información")
        st.markdown(
            """
            Recolectamos datos desde múltiples fuentes:
            - Formularios de percepción  
            - Entrevistas digitales  
            - Datos administrativos  
            - Señales complementarias (texto, audio, entre otros)  
            """
        )
        st.caption("🟦 Tecnologías: Gradio, Streamlit Forms, Google Sheets API")

    # ======================================================
    # 2. LIMPIEZA
    # ======================================================
    with st.container(border=True):
        st.markdown("### 🧹 2. Limpieza y validación")
        st.write(
            "Estandarizamos formatos, detectamos inconsistencias "
            "y garantizamos la calidad de la información antes del análisis."
        )
        st.caption("🟩 Tecnologías: Pandas, validadores en Python")

    # ======================================================
    # 3. TRANSFORMACIÓN
    # ======================================================
    with st.container(border=True):
        st.markdown("### 🔧 3. Transformación y normalización")
        st.markdown(
            """
            Convertimos los datos en estructuras comparables mediante:
            - Codificación de respuestas  
            - Normalización de escalas  
            - Integración con datos demográficos o institucionales  
            """
        )
        st.caption("🟨 Tecnologías: Pandas, NumPy")

    # ======================================================
    # 4. ANÁLISIS
    # ======================================================
    with st.container(border=True):
        st.markdown("### 📊 4. Análisis estadístico y medición")
        st.markdown(
            """
            Aplicamos técnicas cuantitativas y cualitativas para generar evidencia:
            - Modelos de percepción  
            - Segmentación y clústeres  
            - Análisis de tendencias temporales  
            - Generación de insights automáticos  
            """
        )
        st.caption("🟪 Tecnologías: Python, Scikit-learn, StatsModels")

    # ======================================================
    # 5. VISUALIZACIÓN
    # ======================================================
    with st.container(border=True):
        st.markdown("### 📈 5. Visualización e interpretación")
        st.markdown(
            """
            Construimos dashboards claros y orientados a la toma de decisiones:
            - Vista general  
            - Vista individual  
            - Evolución por variable  
            """
        )
        st.caption("🟧 Tecnologías: Streamlit, Plotly, Altair")

    # ======================================================
    # 6. INSIGHTS
    # ======================================================
    with st.container(border=True):
        st.markdown("### 🧠 6. Insights y acciones recomendadas")
        st.markdown(
            """
            Transformamos los hallazgos analíticos en decisiones concretas:
            - Acciones de reputación  
            - Ajustes operativos  
            - Estrategias de comunicación  
            - Seguimiento y mejora continua  
            """
        )

    # =========================
    # CIERRE
    # =========================
    st.divider()

    with st.container(border=True):
        st.info(
            "🎯 **En pocas palabras:**\n\n"
            "Una **metodología sólida** define cómo se estudia la percepción;\n"
            "el **Pipeline Algebra Labs** muestra cómo esos datos "
            "se convierten en valor real para la toma de decisiones."
        )
