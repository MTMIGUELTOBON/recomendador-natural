import streamlit as st

st.set_page_config(page_title="Recomendador Natural", layout="centered")

st.title("🌿 Recomendador Natural de Bienestar")

st.markdown("Selecciona un producto para conocer sus beneficios y solicitarlo por WhatsApp.")

# --- Productos ---
productos = {
    "Sales de Magnesio B10": {
        "descripcion": "Complemento alimenticio con magnesio elemental, ideal para apoyar el bienestar general del cuerpo y el sistema muscular.",
        "beneficios": [
            "Contribuye al equilibrio electrolítico y la función muscular.",
            "Puede ayudar a reducir la fatiga ocasional.",
            "Aporta magnesio para complementar tu alimentación.",
            "Puede favorecer el descanso natural del cuerpo.",
            "Apoyo nutricional en estilos de vida activos o con tensión muscular."
        ],
        "precio": "$60.000",
        "whatsapp": "https://wa.me/573053447946?text=Hola%2C%20estoy%20interesado(a)%20en%20las%20Sales%20de%20Magnesio%20B10"
    },
    "Colágeno Hidrolizado Marino Savifar": {
        "descripcion": "Fórmula avanzada con colágeno marino, péptidos, antioxidantes y vitaminas. Apoya el bienestar de la piel, articulaciones y tejidos.",
        "beneficios": [
            "Puede favorecer la elasticidad, hidratación y firmeza de la piel.",
            "Aporta colágeno tipo 1 y 2, ideal para articulaciones y tejido conectivo.",
            "Incluye antioxidantes como resveratrol, vitamina E y astaxantina.",
            "Contiene aminoácidos esenciales y biotina para piel, cabello y uñas.",
            "Puede actuar como aliado en rutinas de cuidado antiedad."
        ],
        "precio": "$65.000",
        "whatsapp": "https://wa.me/573053447946?text=Hola%2C%20estoy%20interesado(a)%20en%20el%20Colágeno%20Hidrolizado%20Marino%20Savifar"
    }
}

# --- Interfaz de usuario ---
opcion = st.selectbox("Selecciona un producto:", list(productos.keys()))

prod = productos[opcion]
st.subheader(opcion)
st.markdown(f"**{prod['descripcion']}**")
st.markdown(f"**💵 Precio:** {prod['precio']}")
st.markdown("**🌟 Beneficios:**")
for b in prod["beneficios"]:
    st.markdown(f"- {b}")

# Enlace a WhatsApp funcional
st.markdown(
    f"[📲 Solicitar por WhatsApp]({prod['whatsapp']})",
    unsafe_allow_html=True
)

