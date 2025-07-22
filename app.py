import streamlit as st

# ---------------------------
# CONFIGURACIÓN INICIAL
# ---------------------------
st.set_page_config(
    page_title="¿Por qué necesitas Magnesio, Potasio y Zinc?",
    page_icon="🌿",
    layout="centered"
)

# ---------------------------
# ESTILO PERSONALIZADO
# ---------------------------
st.markdown("""
<style>
h1 {
    color: #2c3e50;
    font-size: 38px;
}
h2 {
    color: #34495e;
}
div.stButton > button {
    background-color: #25D366;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.75em 1.5em;
    font-size: 18px;
}
.big-text {
    font-size: 20px;
    line-height: 1.6;
}
.highlight {
    background-color: #e8f5e9;
    padding: 1em;
    border-left: 5px solid #43a047;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# TÍTULO E INTRODUCCIÓN
# ---------------------------
st.markdown("# 🌿 El poder del Magnesio, el Potasio y el Zinc en tu salud")

st.markdown("""
<div class="big-text">
En un mundo lleno de estrés, mala alimentación y cansancio crónico, los minerales esenciales como el <strong>magnesio</strong>, <strong>potasio</strong> y <strong>zinc</strong> se han convertido en aliados clave para restaurar el equilibrio natural de tu cuerpo.<br><br>

Si sufres de insomnio, fatiga, ansiedad, presión alta o defensas bajas, es probable que tengas una deficiencia de estos nutrientes. Aquí te explicamos por qué los necesitas.
</div>
""", unsafe_allow_html=True)

# ---------------------------
# SECCIÓN DE BENEFICIOS
# ---------------------------
st.markdown("## 🧠 Beneficios del Magnesio")
st.markdown("""
<div class="highlight">
✅ Regula el sistema nervioso, ayudando a combatir el estrés y la ansiedad.<br>
✅ Mejora el sueño profundo y la recuperación muscular.<br>
✅ Participa en más de 300 funciones bioquímicas en tu cuerpo.<br>
✅ Reduce dolores de cabeza, calambres y mejora la digestión.
</div>
""", unsafe_allow_html=True)

st.markdown("## 💪 Beneficios del Potasio")
st.markdown("""
<div class="highlight">
✅ Controla la presión arterial y protege el corazón.<br>
✅ Mejora el rendimiento físico y reduce la fatiga muscular.<br>
✅ Previene calambres y equilibra líquidos en el cuerpo.
</div>
""", unsafe_allow_html=True)

st.markdown("## 🛡 Beneficios del Zinc")
st.markdown("""
<div class="highlight">
✅ Refuerza tu sistema inmune frente a virus y bacterias.<br>
✅ Mejora la piel, el cabello y la fertilidad.<br>
✅ Apoya la producción hormonal y la cicatrización.
</div>
""", unsafe_allow_html=True)

# ---------------------------
# VIDEOS INFORMATIVOS
# ---------------------------
st.markdown("## 🎥 ¿Qué dicen los expertos?")
st.video("https://youtu.be/_V8GAcucXKc?si=XdQ_SrsrvXkxKUoY")
st.video("https://youtu.be/NuoXHhgvt2M?si=WuGfb6M6dxcerKir")
st.markdown("🔗 [Ver otro video en Facebook](https://www.facebook.com/share/v/15oewXmRJw/)")

# ---------------------------
# OFERTA DEL PRODUCTO
# ---------------------------
st.markdown("## 💊 Presentamos: Sales de Magnesio B10")

st.markdown("""
<div class="highlight">
🔹 Fórmula avanzada con Magnesio (Citrato, Cloruro, Malato, Bisglicinato)<br>
🔹 Enriquecido con Zinc y Potasio<br>
🔹 Sin azúcar – endulzado con Stevia<br>
🔹 Ideal para adultos, fácil disolución y sabor neutro<br>
<br>
💵 <strong>Precio especial:</strong> <span style="color:green; font-size: 22px;">$64.900</span> con domicilio incluido en Colombia
</div>
""", unsafe_allow_html=True)

# ---------------------------
# BOTÓN WHATSAPP
# ---------------------------
st.markdown("")

whatsapp_text = "Hola, quiero saber más sobre el suplemento de Magnesio B10"
whatsapp_url = f"https://wa.me/573053447946?text={whatsapp_text.replace(' ', '%20')}"

if st.button("💬 Más información por WhatsApp"):
    st.markdown(f"[Click aquí para escribirnos]({whatsapp_url})", unsafe_allow_html=True)

# ---------------------------
# PIE DE PÁGINA
# ---------------------------
st.markdown("---")
st.markdown("📍 Elaborado por SAVIFAR · Producto 100% Colombiano · Distribución autorizada")
