import streamlit as st

def render():

    # =========================
    # TÍTULO
    # =========================
    st.markdown("## 🧭 Identificación de necesidades del cliente")
    st.caption(
        "Línea base para el diseño de estudios de percepción, diagnósticos sociales y consultoría estratégica"
    )

    st.write(
        "Todo estudio de percepción riguroso comienza con una **comprensión clara de la necesidad**. "
        "Antes de recolectar datos, aplicar modelos o construir dashboards, "
        "es fundamental entender **qué decisión se quiere tomar**, "
        "**qué problema se busca resolver** y **qué información falta hoy**."
    )

    st.divider()

    # =========================
    # OBJETIVO
    # =========================
    with st.container(border=True):
        st.markdown("### 🎯 Objetivo del diagnóstico inicial")
        st.write(
            "El diagnóstico inicial permite traducir una inquietud general "
            "en un **problema analizable**, definiendo el alcance, "
            "la profundidad y el enfoque del estudio de percepción."
        )

        st.markdown(
            """
            Este proceso busca:
            - Identificar el problema real (no solo sus síntomas)
            - Alinear expectativas entre el cliente y el equipo analítico
            - Definir qué información es realmente útil para la toma de decisiones
            - Establecer una línea base clara y trazable
            """
        )

    # =========================
    # PREGUNTAS CLAVE
    # =========================
    st.markdown("### 📋 Preguntas clave para identificar la necesidad")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("#### 🔍 1. Sobre el problema")
            st.markdown(
                """
                - ¿Qué situación motivó la necesidad del estudio?  
                - ¿Qué está ocurriendo actualmente que genera preocupación?  
                - ¿Desde cuándo se presenta esta situación?  
                """
            )

        with st.container(border=True):
            st.markdown("#### 👥 3. Sobre la población")
            st.markdown(
                """
                - ¿A quién se quiere escuchar?  
                - ¿Quiénes están directamente afectados?  
                - ¿Existen grupos prioritarios o poblaciones sensibles?  
                """
            )

        with st.container(border=True):
            st.markdown("#### 💬 5. Sobre la percepción actual")
            st.markdown(
                """
                - ¿Qué cree hoy la organización que está pasando?  
                - ¿Existen hipótesis previas o supuestos?  
                - ¿Hay tensiones, desconfianza o ruido reputacional?  
                """
            )

    with col2:
        with st.container(border=True):
            st.markdown("#### 🧠 2. Sobre la decisión")
            st.markdown(
                """
                - ¿Qué decisiones se esperan tomar con los resultados?  
                - ¿Quién tomará esas decisiones?  
                - ¿Qué pasaría si no se realiza el estudio?  
                """
            )

        with st.container(border=True):
            st.markdown("#### 📊 4. Sobre el uso de los resultados")
            st.markdown(
                """
                - ¿Se requieren indicadores, recomendaciones o ambos?  
                - ¿Se necesita seguimiento en el tiempo?  
                - ¿Cómo se comunicarán los hallazgos?  
                """
            )

    # =========================
    # RESULTADOS DEL DIAGNÓSTICO
    # =========================
    st.markdown("### 🧩 ¿Qué se obtiene con este diagnóstico?")

    with st.container(border=True):
        st.markdown(
            """
            A partir de estas preguntas es posible:
            - Definir el tipo de estudio (cualitativo, cuantitativo o mixto)
            - Seleccionar las dimensiones de percepción relevantes
            - Diseñar instrumentos adecuados y proporcionales a la necesidad
            - Estimar tiempos, costos y complejidad
            - Construir una propuesta **a la medida**, no genérica
            """
        )

    # =========================
    # CIERRE ESTRATÉGICO
    # =========================
    with st.container(border=True):
        st.info(
            "💡 **Un buen estudio de percepción no comienza preguntando al público, "
            "sino formulando las preguntas correctas al cliente.**\n\n"
            "Este diagnóstico es la base para transformar percepciones "
            "en evidencia útil, decisiones informadas y acciones concretas."
        )


    st.markdown("## 🧭 Diagnóstico inicial de necesidades")
    st.caption(
        "Herramienta base para el diseño de estudios de percepción y consultoría estratégica"
    )

    st.write(
        "Este diagnóstico permite identificar de forma clara "
        "la necesidad del cliente y convertirla en un estudio de percepción "
        "bien definido, útil y accionable."
    )

    st.divider()

    # =========================
    # BLOQUE 1 – CONTEXTO
    # =========================
    with st.container(border=True):
        st.markdown("### 1️⃣ Contexto del problema")

        problema = st.text_area(
            "¿Qué situación o problema motiva la necesidad del estudio?",
            placeholder="Ejemplo: baja confianza ciudadana, quejas frecuentes, baja participación..."
        )

        antiguedad = st.selectbox(
            "¿Desde cuándo se presenta esta situación?",
            [
                "Menos de 6 meses",
                "Entre 6 meses y 1 año",
                "Más de un año",
                "No se tiene claridad"
            ]
        )

    # =========================
    # BLOQUE 2 – DECISIÓN
    # =========================
    with st.container(border=True):
        st.markdown("### 2️⃣ Decisiones que se buscan apoyar")

        decision = st.multiselect(
            "¿Qué tipo de decisiones se quieren tomar con este estudio?",
            [
                "Mejorar un servicio",
                "Rediseñar un programa",
                "Ajustar estrategia de comunicación",
                "Evaluar impacto",
                "Gestionar riesgos reputacionales",
                "Soportar toma de decisiones directivas"
            ]
        )

        decisor = st.text_input(
            "¿Quién tomará las decisiones con base en los resultados?",
            placeholder="Ejemplo: dirección, secretaría, gerencia, comité técnico"
        )

    # =========================
    # BLOQUE 3 – POBLACIÓN
    # =========================
    with st.container(border=True):
        st.markdown("### 3️⃣ Población de interés")

        poblacion = st.multiselect(
            "¿A quién se quiere escuchar?",
            [
                "Ciudadanía en general",
                "Usuarios de un servicio",
                "Beneficiarios de un programa",
                "Funcionarios / colaboradores",
                "Grupos específicos o vulnerables"
            ]
        )

        territorio = st.text_input(
            "Territorio o ámbito de análisis",
            placeholder="Ejemplo: ciudad, localidad, institución, región"
        )

    # =========================
    # BLOQUE 4 – PERCEPCIÓN
    # =========================
    with st.container(border=True):
        st.markdown("### 4️⃣ Percepción actual (hipótesis)")

        percepcion_actual = st.multiselect(
            "¿Qué se cree que está pasando actualmente?",
            [
                "Desconfianza",
                "Desinformación",
                "Insatisfacción",
                "Baja visibilidad",
                "Percepción positiva",
                "No se tiene claridad"
            ]
        )

    # =========================
    # RESULTADO / RESUMEN
    # =========================
    st.divider()
    st.markdown("## 🧾 Resumen del diagnóstico")

    with st.container(border=True):
        st.markdown("### 📌 Línea base identificada")

        st.markdown(f"""
        **Problema identificado:**  
        {problema if problema else "No especificado"}

        **Antigüedad del problema:**  
        {antiguedad}

        **Decisiones a soportar:**  
        {", ".join(decision) if decision else "No especificadas"}

        **Decisor principal:**  
        {decisor if decisor else "No especificado"}

        **Población objetivo:**  
        {", ".join(poblacion) if poblacion else "No especificada"}

        **Territorio / ámbito:**  
        {territorio if territorio else "No especificado"}

        **Hipótesis de percepción actual:**  
        {", ".join(percepcion_actual) if percepcion_actual else "No especificada"}
        """)

    # =========================
    # CIERRE ESTRATÉGICO
    # =========================
    with st.container(border=True):
        st.info(
            "🎯 **Este resumen constituye la línea base del estudio de percepción.**\n\n"
            "A partir de esta información se puede definir el enfoque metodológico, "
            "los instrumentos, los indicadores y la propuesta técnica "
            "de forma clara, coherente y a la medida del cliente."
        )
