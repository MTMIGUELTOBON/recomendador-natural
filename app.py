import streamlit as st

# Título emocional directo
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

st.markdown('<p class="big-title">¿Estás perdiendo energía, malhumorado o con insomnio?</p>', unsafe_allow_html=True)

st.markdown('<p class="subheading">Tu cuerpo podría estar bajo en minerales esenciales como Magnesio, Potasio y Zinc.</p>', unsafe_allow_html=True)

st.markdown("""
---

### 🔍 Identifica tus síntomas:
- Problemas para dormir
- Cansancio crónico
- Estrés o ansiedad
- Calambres musculares
- Inmunidad baja

---

### 💪 Beneficios de Magnesio B10:
- **Magnesio**: Relaja músculos, mejora el sueño y regula el sistema nervioso
- **Potasio**: Equilibra la presión arterial y fortalece músculos
- **Zinc**: Refuerza defensas, mejora digestión y producción hormonal

---

### 📹 Videos recomendados:
""")

st.video("https://youtu.be/_V8GAcucXKc?si=XdQ_SrsrvXkxKUoY")
st.video("https://youtu.be/NuoXHhgvt2M?si=WuGfb6M6dxcerKir")
st.markdown("[Ver en Facebook](https://www.facebook.com/share/v/15oewXmRJw/)")

st.markdown("""
---

### 📊 Comparativa del producto:

| Característica                     | Magnesio B10 | Otros productos |
|----------------------------------|--------------|-----------------|
| 4 tipos de magnesio               | ✅            | ❌              |
| Incluye potasio y zinc           | ✅            | ❌              |
| Sin azúcar, con stevia           | ✅            | ❌              |
| Hecho en laboratorio colombiano  | ✅            | ❓              |

---

### ⭐ Testimonios:
""")

st.markdown('''
<div class="testimonial">
"Después de 3 días ya dormía mejor. Lo recomiendo 100%"  
— María Fernanda, Medellín
</div>
<div class="testimonial">
"Lo tomo antes de dormir y me relaja el cuerpo completo."  
— Andrés L., Cali
</div>
''', unsafe_allow_html=True)

st.markdown("""
---

### 🎯 ¡Aprovecha la oferta!
💰 **$64.900 con envío incluido**
📦 Entregas a toda Colombia

[🟢 Pedir ahora por WhatsApp](https://wa.me/573053447946?text=Hola%2C+quiero+comprar+el+Magnesio+B10+y+aprovechar+la+oferta)

---
🧪 Producto natural certificado por **Laboratorios SAVIFAR**
""")
