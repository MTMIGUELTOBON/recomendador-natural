import streamlit as st

# Título llamativo emocional
st.markdown("""
<style>
.big-title {
    font-size: 32px;
    color: #2E86C1;
    font-weight: bold;
}
.subheading {
    font-size: 20px;
    color: #117A65;
}
.testimonial {
    font-style: italic;
    color: #5D6D7E;
    background-color: #F4F6F7;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">¿Cansancio, insomnio o ansiedad? Podrías estar perdiendo minerales esenciales sin saberlo...</p>', unsafe_allow_html=True)

# Test de síntomas
st.markdown('<p class="subheading">✅ ¿Te identificas con alguno de estos síntomas?</p>', unsafe_allow_html=True)
st.markdown("""
- 🔹 Me cuesta dormir profundamente  
- 🔹 Me siento sin energía todo el día  
- 🔹 Sufro de estrés constante o dolores musculares  
- 🔹 Tengo defensas bajas o problemas digestivos
""")

# Botón WhatsApp inicial
st.markdown("""
[🟢 ¡Lo necesito! Escríbeme por WhatsApp](https://wa.me/573053447946?text=Hola%2C+quiero+más+información+sobre+el+Magnesio+B10)  
""")

# Beneficios del producto
st.markdown('<p class="subheading">🌟 ¿Por qué tu cuerpo necesita Magnesio, Potasio y Zinc?</p>', unsafe_allow_html=True)
st.markdown("""
- ✅ **Magnesio**: Ayuda a relajar los músculos, mejorar el sueño y reducir el estrés.  
- ✅ **Potasio**: Regula la presión arterial, apoya la función nerviosa y muscular.  
- ✅ **Zinc**: Refuerza el sistema inmune y mejora la salud hormonal y digestiva.
""")

# Video de respaldo
st.video("https://youtu.be/_V8GAcucXKc?si=XdQ_SrsrvXkxKUoY")
st.video("https://youtu.be/NuoXHhgvt2M?si=WuGfb6M6dxcerKir")
st.markdown("[🎥 Ver video en Facebook](https://www.facebook.com/share/v/15oewXmRJw/)")

# Testimonios simulados
st.markdown('<p class="subheading">💬 Lo que dicen quienes ya lo usan</p>', unsafe_allow_html=True)
st.markdown('''
<div class="testimonial">
“Llevo tomando el Magnesio B10 2 semanas y ya duermo mejor y tengo más energía. ¡Gracias!”  
— Laura G., Bogotá
</div>
<div class="testimonial">
“Soy hipertenso y esta fórmula con potasio me ha ayudado muchísimo, muy recomendado.”  
— Julián M., Medellín
</div>
''', unsafe_allow_html=True)

# Comparativa de valor
st.markdown('<p class="subheading">📊 ¿Por qué elegir Magnesio B10?</p>', unsafe_allow_html=True)
st.markdown("""
| Característica                     | Magnesio B10 | Otros suplementos |
|----------------------------------|--------------|-------------------|
| 4 tipos de magnesio combinados   | ✅            | ❌                |
| Con zinc y potasio incluidos     | ✅            | ❌                |
| Sin azúcar, endulzado con stevia | ✅            | ❌                |
| Aprobado por laboratorio colombiano | ✅         | ❓                |
""")

# Oferta limitada
st.markdown('<p class="subheading">🎁 Oferta especial HOY:</p>', unsafe_allow_html=True)
st.markdown("""
💥 Precio promocional: **$64.900**  
📦 Domicilio incluido en Colombia  
📞 Escríbenos ahora por WhatsApp y recibe el tuyo
""")

# CTA final fuerte
st.markdown("""
[🚀 ¡Quiero comprar ahora!](https://wa.me/573053447946?text=Hola%2C+quiero+comprar+el+Magnesio+B10+y+aprovechar+la+oferta)  
""")

# Estética general
st.markdown("""
---
🧪 Producto natural certificado por **Laboratorios SAVIFAR**
""")

