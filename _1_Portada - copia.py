import streamlit as st
from pathlib import Path

def render():

    # =========================
    # ESTADO SEGURO
    # =========================
    if "portada_index" not in st.session_state:
        st.session_state.portada_index = 0

    BASE_DIR = Path(__file__).resolve().parent

    # ❗ NOMBRES ORIGINALES (NO SE CAMBIAN)
    imagenes = [
        BASE_DIR / "assets" / "patoconejo.png",
        BASE_DIR / "assets" / "copa.png",
        BASE_DIR / "assets" / "triangulo.png",
    ]

    # =========================
    # CABECERA FIJA
    # =========================
    st.markdown("## 📱 Percepción 360")
    st.write("Cómo interpretamos la realidad depende más de nosotros de lo que creemos")
    st.divider()

    # =========================
    # NAVEGACIÓN
    # =========================
    col_prev, _, col_next = st.columns([1, 6, 1])

    with col_prev:
        if st.button("⬅️", key="portada_prev"):
            st.session_state.portada_index = (
                st.session_state.portada_index - 1
            ) % len(imagenes)
            st.rerun()

    with col_next:
        if st.button("➡️", key="portada_next"):
            st.session_state.portada_index = (
                st.session_state.portada_index + 1
            ) % len(imagenes)
            st.rerun()

    # =========================
    # IMAGEN (ÚNICO ELEMENTO DINÁMICO)
    # =========================
    ruta = imagenes[st.session_state.portada_index]

    st.image(str(ruta), use_container_width=True)

    # =========================
    # TEXTO FIJO (NO CAMBIA)
    # =========================
    st.info(
        "💡 La percepción no es solo lo que vemos, sino cómo interpretamos la información."
    )
