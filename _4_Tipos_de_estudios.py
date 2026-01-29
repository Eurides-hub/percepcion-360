import streamlit as st

def render():
    # =========================
    # TÍTULO
    # =========================
    st.markdown("## 📊 Tipos de estudios de percepción")

    st.write(
        "Existen distintos enfoques para medir la percepción. "
        "Cada uno se adapta a las necesidades de investigación, "
        "los objetivos estratégicos y la profundidad analítica requerida."
    )

    st.divider()

    st.write(
        "La percepción se puede estudiar desde tres enfoques principales: "
        "**cualitativo**, **cuantitativo** y **mixto**. "
        "Cada uno responde preguntas distintas y aporta piezas complementarias."
    )

    # ======================================================
    # 1. CUALITATIVO
    # ======================================================
    st.markdown("## 🎤 1. Enfoque cualitativo: entender la percepción")

    with st.container(border=True):
        st.markdown("### 🧠 Propósito")
        st.write(
            "Explorar cómo perciben las personas, qué sienten, "
            "qué narrativas construyen y por qué piensan como piensan."
        )

    with st.container(border=True):
        st.markdown("### 📌 Métodos principales")
        st.markdown(
            """
            - Entrevistas en profundidad  
            - Grupos focales  
            - Observación de experiencias  
            - Análisis narrativo  
            """
        )

    with st.container(border=True):
        st.markdown("### 🎯 Qué aporta")
        st.markdown(
            """
            - Identifica causas raíz  
            - Revela emociones, barreras y motivaciones  
            - Permite diseñar instrumentos cuantitativos mejor enfocados  
            """
        )

    # ======================================================
    # 2. CUANTITATIVO
    # ======================================================
    st.markdown("## 📊 2. Enfoque cuantitativo: medir la percepción")

    with st.container(border=True):
        st.markdown("### 📐 ¿Qué mide?")
        st.write(
            "Mide el **cuánto**: cuánto confían, cuánto valoran, "
            "cuánto recomiendan o cuánto perciben. "
            "Genera datos comparables, escalables y analizables estadísticamente."
        )

    # -------------------------
    # 2.1 PASO A PASO
    # -------------------------
    st.markdown("### 🔹 2.1 Cómo funciona un estudio cuantitativo")

    with st.container(border=True):
        st.markdown("#### 1️⃣ Diseño de la encuesta")
        st.write(
            "Puede ser por muestreo probabilístico o no probabilístico, "
            "según los recursos y la población objetivo."
        )

    with st.container(border=True):
        st.markdown("#### 2️⃣ Preguntas con escalas estandarizadas")
        st.markdown(
            """
            - Escalas Likert (1–5, 1–7)  
            - Diferenciales semánticos (malo–bueno, lento–rápido)  
            """
        )

    with st.container(border=True):
        st.markdown("#### 3️⃣ Transformación en indicadores")
        st.markdown(
            """
            - Índice de satisfacción  
            - Índice de clima laboral  
            - Índice de calidad percibida  
            - NPS (Net Promoter Score)  
            """
        )
        st.write(
            "Estos indicadores permiten comparar sedes, grupos, áreas "
            "o periodos de tiempo."
        )

    with st.container(border=True):
        st.markdown("#### 4️⃣ Modelos estadísticos aplicados")
        st.markdown(
            """
            - Regresión lineal o logística  
            - Modelos ordinales  
            - Clústeres o segmentación  
            - PCA o análisis factorial  
            """
        )
        st.write(
            "Estos modelos permiten identificar qué variables explican "
            "realmente la percepción."
        )

    # -------------------------
    # 2.2 MÉTODOS DIRECTOS
    # -------------------------
    st.markdown("### 🔹 2.2 Métodos cuantitativos directos")
    st.caption("La percepción se pregunta explícitamente")

    with st.container(border=True):
        st.markdown("#### 📝 1. Encuestas estructuradas")
        st.write(
            "Instrumento clásico con preguntas cerradas, "
            "escalas Likert y diferenciales semánticos."
        )

    with st.container(border=True):
        st.markdown("#### 📱 2. Formularios de micropercepción")
        st.markdown(
            """
            - Pop-ups en web  
            - Preguntas de un solo ítem  
            - NPS al finalizar un servicio  
            """
        )
        st.write("Permiten capturar percepción en tiempo real.")

    with st.container(border=True):
        st.markdown("#### 🧪 3. Escalas psicométricas")
        st.write(
            "Instrumentos validados científicamente para medir "
            "satisfacción, liderazgo, clima laboral o confianza."
        )

    # -------------------------
    # 2.3 MÉTODOS INDIRECTOS
    # -------------------------
    st.markdown("### 🔹 2.3 Métodos cuantitativos indirectos")
    st.caption("La percepción se infiere a partir del comportamiento")

    with st.container(border=True):
        st.markdown("#### 📈 4. Analítica web o de aplicaciones")
        st.markdown(
            """
            - Abandono de carrito → percepción de dificultad  
            - Tasa de rebote → percepción de relevancia  
            - Tiempo en página → interés  
            - Quejas digitales → percepción negativa  
            """
        )

    with st.container(border=True):
        st.markdown("#### 🎧 5. Indicadores de uso del servicio")
        st.markdown(
            """
            - Volumen de reclamos  
            - Frecuencia de uso  
            - Retención  
            - Cumplimiento de citas  
            """
        )
        st.write("Reflejan niveles reales de satisfacción o frustración.")

    # -------------------------
    # 2.4 TEXTO
    # -------------------------
    st.markdown("### 🔹 2.4 Métodos cuantitativos basados en texto")

    with st.container(border=True):
        st.markdown("#### 💬 6. Análisis de sentimiento")
        st.write(
            "Convierte opiniones en indicadores (positivo, neutro, negativo). "
            "Aplicable a comentarios, PQRS, redes sociales, reseñas o chatbots."
        )

    with st.container(border=True):
        st.markdown("#### 🧩 7. Modelos de tópicos")
        st.write(
            "Modelos como LDA o BERTopic permiten identificar patrones "
            "ocultos en grandes volúmenes de texto."
        )

    # -------------------------
    # 2.5 EXPERIMENTALES
    # -------------------------
    st.markdown("### 🔹 2.5 Métodos experimentales")

    with st.container(border=True):
        st.markdown("#### 🧪 8. A/B Testing")
        st.write(
            "Comparación de dos versiones para evaluar experiencia, "
            "preferencia o confianza."
        )

    with st.container(border=True):
        st.markdown("#### 🎁 9. Experimentos de precio o empaque")
        st.write(
            "Evalúan percepción de valor, diseño, claridad "
            "y confianza visual."
        )

    # -------------------------
    # 2.6 PUNTOS DE SERVICIO
    # -------------------------
    st.markdown("### 🔹 2.6 Escalas rápidas en puntos de servicio")

    with st.container(border=True):
        st.markdown("#### 😊 10. Terminales físicos de satisfacción")
        st.write(
            "Botones tipo feliz–neutral–triste, comunes en retail, "
            "transporte y aeropuertos."
        )

    with st.container(border=True):
        st.markdown("#### 📝 11. Tarjetas de puntuación")
        st.write(
            "Escalas 0–10, 1–5 o excelente–bueno–regular–malo, "
            "usadas en atención al cliente y servicios."
        )

    # -------------------------
    # APORTE CUANTITATIVO
    # -------------------------
    st.markdown("### 🔍 ¿Qué aporta el enfoque cuantitativo?")

    with st.container(border=True):
        st.markdown(
            """
            - Medición precisa  
            - Comparaciones entre grupos  
            - Análisis de tendencias  
            - Indicadores estratégicos para la gestión  
            """
        )

    # ======================================================
    # 3. MIXTO
    # ======================================================
    st.markdown("## 🔄 3. Enfoque mixto: la combinación ideal")

    with st.container(border=True):
        st.markdown("### 🔧 Cómo funciona")
        st.markdown(
            """
            - Se exploran problemas mediante entrevistas  
            - Luego se diseñan encuestas para medirlos a gran escala  
            """
        )

    with st.container(border=True):
        st.markdown("### 🎯 Qué aporta")
        st.markdown(
            """
            - Explicaciones + métricas  
            - Recomendaciones sólidas  
            - Visión 360°  
            """
        )
        st.write(
            "Es ideal para analizar temas como confianza institucional, "
            "seguridad, programas territoriales o políticas públicas."
        )
