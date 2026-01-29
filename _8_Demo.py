import streamlit as st
from pathlib import Path

def render():

    BASE_DIR = Path(__file__).resolve().parent

    estudios = {
        "Movilidad urbana": {
            "imagen": BASE_DIR / "assets" / "movilidad.jpg",
            "dashboard": BASE_DIR / "assets" / "dashboard_movilidad.png",
            "descripcion": "Análisis de percepción ciudadana sobre transporte, tiempos de viaje y seguridad vial."
        },
        "Educación": {
            "imagen": BASE_DIR / "assets" / "educacion.png",
            "dashboard": BASE_DIR / "assets" / "dashboard_educacion.png",
            "descripcion": "Percepción de calidad educativa, acceso, infraestructura y experiencia estudiantil."
        },
        "Canasta Familiar": {
            "imagen": BASE_DIR / "assets" / "servicios.png",
            "dashboard": BASE_DIR / "assets" / "dashboard_servicios.png",
            "descripcion": "La percepción sobre la canasta familiar en Colombia destaca una alta sensibilidad al aumento de precios, donde más del \(95\%\) de los hogares perciben escasez e incremento de costos en los alimentos."
        }
    }

    # =========================
    # CABECERA
    # =========================
    st.markdown("## 📊 Estudios de percepciones realizados")
    st.write("Visor de estudios desarrollados por Algebra Labs")
    st.divider()

    # =========================
    # SELECTOR
    # =========================
    estudio = st.radio(
        "Selecciona un estudio:",
        list(estudios.keys()),
        horizontal=True
    )

    data = estudios[estudio]

    # =========================
    # IMAGEN PRINCIPAL (CENTRADA)
    # =========================
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(
            str(data["imagen"]),
            width=420
        )

    st.markdown(f"### {estudio}")
    st.write(data["descripcion"])

    # =========================
    # DASHBOARD (OPCIONAL)
    # =========================
    with st.expander("📈 Ver visualización analítica"):
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.image(
                str(data["dashboard"]),
                use_container_width=True
            )
