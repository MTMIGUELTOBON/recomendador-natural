import streamlit as st

# ---------------------------
# CONFIGURACIÓN INICIAL
# ---------------------------
st.set_page_config(
    page_title="Sales de Magnesio B10",
    page_icon="💊",
    layout="centered",
)

# ---------------------------
# ENCABEZADO
# ---------------------------
st.markdown("""
# 💙 Sales de Magnesio B10  
### Compuesto Marino + Potasio + Zinc  
""")
st.image("1000083186.jpg", caption="600g - Línea Premium Gold Savifar", use_column_width=True)

st.markdown("""
¿Sabías que más del 70% de las personas tienen deficiencia de **magnesio, potasio o zinc** y no lo saben?

Este suplemento ayuda a tu cuerpo a recuperar el equilibrio natural y mejorar funciones clave como el sueño, la digestión, el sistema inmune y la energía.
""")

# ---------------------------
# BENEFICIOS
# ---------------------------
st.markdown("## ✅ Beneficios del Magnesio, Potasio y Zinc")

with st.expander("🧠 Magnesio"):
    st.markdown("""
- Relaja el sistema nervioso y muscular.
- Mejora el sueño, la digestión y reduce el estrés.
- Esencial en más de 300 funciones bioquímicas del cuerpo.
""")

with st.expander("💪 Potasio"):
    st.markdown("""
- Regula la presión arterial.
- Ayuda al equilibrio de líquidos y el ritmo cardíaco.
- Reduce calambres musculares y fatiga.
""")

with st.expander("🛡 Zinc"):
    st.markdown("""
- Refuerza el sistema inmunológico.
- Mejora la piel, el cabello y la fertilidad.
- Acelera la cicatrización y mejora las defensas.
""")

# ---------------------------
# VIDEOS INFORMATIVOS
# ---------------------------
st.markdown("## 🎥 Videos Recomendados")

st.video("https://youtu.be/_V8GAcucXKc?si=XdQ_SrsrvXkxKUoY")
st.video("https://youtu.be/NuoXHhgvt2M?si=WuGfb6M6dxcerKir")

st.markdown("""
🔗 [Ver otro video en Facebook](https://www.facebook.com/share/v/15oewXmRJw/)
""")

# ---------------------------
# SECCIÓN DEL PRODUCTO
# ---------------------------
st.markdown("## 🛒 ¿Quieres probarlo?")

st.image("1000083186.jpg", caption="Sales de Magnesio B10 - 600g", use_column_width=True)

st.markdown("""
💵 **Precio:** $64.900 (con domicilio incluido en Colombia)  
📦 Contiene: Citrato, Cloruro, Bisglicinato y Malato de Magnesio, Zinc, Potasio, y más.

✅ Apto para adultos, sin azúcar, endulzado con stevia.
""")

# ---------------------------
# BOTÓN WHATSAPP
# ---------------------------
whatsapp_text = "Hola, vi las Sales de Magnesio B10 y quiero más información."
whatsapp_url = f"https://wa.me/573053447946?text={whatsapp_text.replace(' ', '%20')}"

st.markdown(f"""
<a href="{whatsapp_url}" target="_blank">
    <button style="background-color: #25D366; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px;">
        💬 Hablar por WhatsApp
    </button>
</a>
""", unsafe_allow_html=True)

# ---------------------------
# PIE DE PÁGINA
# ---------------------------
st.markdown("---")
st.markdown("📍 Elaborado por SAVIFAR | Producto 100% Colombiano")

