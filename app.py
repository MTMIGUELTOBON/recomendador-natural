import streamlit as st

# ---------------------------
# CONFIGURACIÓN INICIAL
# ---------------------------
st.set_page_config(
    page_title="Descubre los beneficios del Magnesio",
    page_icon="💊",
    layout="centered",
)

# ---------------------------
# TITULAR PROFESIONAL
# ---------------------------
st.markdown("""
# 🌿 ¿Sabías que el Magnesio puede transformar tu salud?

Más del 70% de las personas sufren deficiencia de **magnesio, potasio o zinc** sin saberlo.

Estos tres minerales son fundamentales para que el cuerpo funcione de manera óptima. Descubre cómo pueden ayudarte a mejorar tu energía, tu descanso y tu bienestar diario.
""")

# ---------------------------
# BENEFICIOS EDUCATIVOS
# ---------------------------
st.markdown("## ✅ Beneficios de cada mineral")

with st.expander("🧠 Magnesio"):
    st.markdown("""
- Relaja el sistema nervioso y reduce el estrés.
- Mejora la calidad del sueño y el descanso profundo.
- Alivia dolores musculares y calambres.
- Apoya la digestión y el equilibrio emocional.
""")

with st.expander("💪 Potasio"):
    st.markdown("""
- Regula la presión arterial.
- Mejora la contracción muscular y la energía.
- Previene la fatiga y los calambres.
- Mantiene el equilibrio de líquidos en el cuerpo.
""")

with st.expander("🛡 Zinc"):
    st.markdown("""
- Refuerza el sistema inmune.
- Ayuda a la cicatrización de la piel.
- Mejora el cabello, las uñas y la fertilidad.
- Regula hormonas y el metabolismo celular.
""")

# ---------------------------
# VIDEOS RECOMENDADOS
# ---------------------------
st.markdown("## 🎥 ¿Qué dicen los expertos?")

st.video("https://youtu.be/_V8GAcucXKc?si=XdQ_SrsrvXkxKUoY")
st.video("https://youtu.be/NuoXHhgvt2M?si=WuGfb6M6dxcerKir")
st.markdown("🔗 [Ver otro video en Facebook](https://www.facebook.com/share/v/15oewXmRJw/)")

# ---------------------------
# SECCIÓN DEL PRODUCTO
# ---------------------------
st.markdown("## 🛒 ¿Quieres mejorar tu salud con un solo suplemento?")

st.markdown("""
Te presentamos **Sales de Magnesio B10**, una fórmula completa con:

- Magnesio (Citrato, Cloruro, Malato y Bisglicinato)
- Potasio
- Zinc
- Libre de azúcar, endulzado con stevia

💵 **Precio especial:** $64.900 (con domicilio incluido en Colombia)
""")

# ---------------------------
# BOTÓN WHATSAPP
# ---------------------------
whatsapp_text = "Hola, quiero saber más sobre el suplemento de Magnesio B10"
whatsapp_url = f"https://wa.me/573053447946?text={whatsapp_text.replace(' ', '%20')}"

st.markdown(f"""
<div style='text-align: center; margin-top: 30px;'>
    <a href="{whatsapp_url}" target="_blank">
        <button style="background-color: #25D366; color: white; padding: 12px 30px; border: none; border-radius: 8px; font-size: 18px;">
            💬 Más información por WhatsApp
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# PIE DE PÁGINA
# ---------------------------
st.markdown("---")
st.markdown("📍 Elaborado por SAVIFAR | Producto 100% Colombiano")

