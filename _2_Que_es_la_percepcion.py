import streamlit as st

def render():
    # =========================
    # TÍTULO
    # =========================
    st.subheader("📌 ¿Qué es la percepción?")

    st.write(
        "La **percepción** es el conjunto de creencias, emociones, opiniones y narrativas "
        "que las personas construyen sobre una organización, marca, institución o persona.\n\n"
        "No describe necesariamente la *realidad*, sino **cómo la gente interpreta** esa realidad."
    )

    # =========================
    # CLAVES
    # =========================
    st.subheader("🔍 Claves")

    st.markdown(
        """
        - Es subjetiva  
        - Se basa en experiencias, emociones y fuentes externas  
        - Influye directamente en la confianza  
        - Cambia con el tiempo  
        """
    )

    with st.container(border=True):
        st.info(
            "💡 **Una buena estrategia de percepción no busca manipular, "
            "sino comprender patrones y tomar decisiones basadas en datos.**"
        )

    # =========================
    # FUNDAMENTOS
    # =========================
    st.markdown("## 🧠 Fundamentos de la percepción")

    st.write(
        "La percepción se construye a partir de estímulos externos, experiencias previas, "
        "memoria, emociones y marcos culturales que moldean cómo interpretamos la realidad."
    )

    # =========================
    # TARJETAS (ESTABLES)
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 🔍 Procesamiento cognitivo")
            st.write(
                "La mente selecciona, organiza e interpreta información "
                "según lo que considera relevante."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 🎭 Carga emocional")
            st.write(
                "Las emociones influyen directamente en la forma "
                "en la que interpretamos los estímulos."
            )

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.markdown("### 📚 Experiencias previas")
            st.write(
                "Lo vivido condiciona los significados que atribuimos "
                "a nuevas situaciones."
            )

    with col4:
        with st.container(border=True):
            st.markdown("### 🌐 Contexto social y cultural")
            st.write(
                "La sociedad entrega marcos simbólicos que guían "
                "la interpretación de la realidad."
            )
