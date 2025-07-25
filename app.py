import streamlit as st
import streamlit as st

# Estilo personalizado para fondo y tipografía
st.markdown("""
    <style>
    .stApp {
        background-color: #e0f7e9;
        color: #222;
        font-family: 'Arial', sans-serif;
    }

    h1, h2, h3 {
        color: #0d5d4c;
    }

    .css-1d391kg p {
        font-size: 1.1rem;
    }

    .css-1v0mbdj a {
        color: #0d5d4c !important;
    }

    </style>
""", unsafe_allow_html=True)

st.markdown("""
# 🌿 Sanar es posible: empieza por lo que comes

¿Cansancio frecuente? ¿Ansiedad, insomnio o dolores musculares?  
Muchas veces no son enfermedades… sino señales de que tu cuerpo necesita nutrientes esenciales.

Al dejar el azúcar, reducir harinas y volver a lo natural, puedes iniciar un cambio profundo.

Aquí descubrirás cómo minerales como el **Magnesio y el Potasio** pueden ayudarte a:

✅ Recuperar tu energía  
✅ Dormir mejor  
✅ Mejorar tu digestión  
✅ Sentirte más en equilibrio

""", unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=_V8GAcucXKc")

st.markdown("""
Vivimos en una época donde **lo común es sentirse mal**,  
pero **sanar es posible cuando comprendes lo que tu cuerpo necesita**.
""", unsafe_allow_html=True)
st.markdown("## El poder de los minerales")

st.markdown("""
Los desequilibrios de minerales son más comunes de lo que creemos,  
y afectan directamente cómo te sientes **cada día**.
""")

st.video("https://www.youtube.com/watch?v=NuoXHhgvt2M")

with st.expander("🧠 Magnesio: el mineral del equilibrio"):
    st.markdown("""
- Relaja el sistema nervioso y los músculos  
- Mejora el sueño y reduce el estrés   
- Apoya la digestión y el tránsito intestinal  
- Regula el azúcar y la presión arterial
""")

with st.expander("💪 Potasio: esencial para el corazón y los músculos"):
    st.markdown("""
- Regula los latidos del corazón y los impulsos nerviosos  
- Previene calambres y fatiga muscular  
- Mejora el rendimiento físico y mental  
- Ayuda a eliminar el exceso de sodio (reduce la hinchazón)
""")

with st.expander("🛡️ Zinc: defensa y reparación del cuerpo"):
    st.markdown("""
- Refuerza el sistema inmunológico  
- Mejora la cicatrización de la piel  
- Es clave en la producción de hormonas  
- Combate el envejecimiento celular  
- Aumenta la energía y vitalidad
""")

st.markdown("> 🔬 Tu cuerpo necesita estos minerales **a diario** para funcionar como debe.")

st.markdown("## 🌿 ¿Cómo empezar a cuidar tu salud mineral?")

st.markdown("""
Pequeños cambios diarios hacen una gran diferencia:

- 🧃 Elimina o reduce el azúcar refinada.  
- 🥬 Consume más vegetales de hoja verde.  
- 🚫 Disminuye harinas y productos ultraprocesados.  
- 💧 Toma suficiente agua pura.  
- 💊 Y si necesitas un apoyo extra, puedes incluir suplementos de calidad.
""")

st.markdown("---")

st.markdown("### 💙 Te recomendamos: **Sales de Magnesio B10 – Savifar**")

st.image("https://i.imgur.com/7Fh8Zn2.jpg", caption="Sales de Magnesio B10 – Compuesto Marino", use_column_width=True)

st.markdown("""
Con 7 tipos de magnesio, potasio, zinc, vitaminas B6, D y otros minerales esenciales.  
✅ Sin azúcar añadida  
✅ Apto para toda la familia  
✅ 600 gramos de pureza mineral
""")

# Botón de WhatsApp
import urllib.parse
mensaje = "Hola, estoy interesado en las Sales de Magnesio B10 que vi en tu página web. ¿Me puedes dar más información?"
url = f"https://wa.me/573053447946?text={urllib.parse.quote(mensaje)}"

st.markdown(f"""
👉 [**Haz clic aquí para pedir por WhatsApp**]({url})
""")
