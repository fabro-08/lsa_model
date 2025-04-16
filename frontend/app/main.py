import streamlit as st
import requests
from config import config

st.set_page_config(page_title="Traductor LSA <> SPA", layout="centered")
st.title("Traductor LSA ⬌️ SPA con LLM")

# Estilos para separar los formularios
st.markdown("---")

example_prompt_lsa ="""
- LSA significa lengua de señas argentina. Es un sistema de comunicación que se utiliza en Argentina.
- La oración en LSA tiene la siguiente estructura: tiempo + sujeto + objeto + verbo(infinitivo) + circunstanciales
- En LSA los artículos no se señan y tampoco existe el verbo ser por ejemplo... la oración "Juan es alto, delgado y bueno", las señas erían "Juan alto, delgado, bueno"
- Cuando el verbo "estar" está a continuacion de un adjetivo se quita de la oracion.
Ejemplos:
"yo comí una manzana ayer" en LSA se traduce a "ayer yo manzana comer".
"hoy tenemos evaluación de matemática" en LSA se traduce "hoy evaluación matemática hay"
"Juan viene en auto" en LSA se traduce "Juan auto venir"
"""

example_prompt_spa ="""
- LSA significa lengua de señas argentina. Es un sistema de comunicación que se utiliza en Argentina.
- La oración en LSA tiene la siguiente estructura: tiempo + sujeto + objeto + verbo(infinitivo) + circunstanciales
- En LSA los artículos no se señan y tampoco existe el verbo ser por ejemplo... la oración "Juan es alto, delgado y bueno", las señas erían "Juan alto, delgado, bueno"

Ejemplos:
"yo comí una manzana ayer" en LSA se traduce a "ayer yo manzana comer".
"hoy tenemos evaluación de matemática" en LSA se traduce "hoy evaluación matemática hay"
"Juan viene en auto" en LSA se traduce "Juan auto venir"

Ahora traducir de LSA a español
"""

# 🔹 Formulario 1: LSA ➔ SPA
st.subheader("Formulario 1: LSA a Español")
with st.form("lsa_form"):
    input_text_1 = st.text_input("Oración en LSA", value="El precio de la compu es alto")
    prompt_1 = st.text_area("Prompt para el modelo", value=example_prompt_lsa, height=150)
    model_1 = st.text_input("Modelo a utilizar", value="microsoft/phi-4")  # Nuevo campo
    submitted_1 = st.form_submit_button("Traducir LSA ➔ SPA")

    if submitted_1:
        payload = {
            "text": input_text_1,
            "prompt_user": prompt_1,
            "model": model_1
        }
        try:
            response = requests.post(f"{config.API_LSA}/translator/translator_lsa", json=payload)
            result = response.json().get("response", {}).get("result", "Sin resultado")
            st.text_area("Resultado", value=result, height=150)
        except Exception as e:
            st.error(f"Error al llamar al endpoint: {e}")

# Separador visual
st.markdown("---")

# 🔹 Formulario 2: Español a LSA
st.subheader("Formulario 2: Español a LSA")
with st.form("spa_form"):
    input_text_2 = st.text_input("Oración en Español", value="precio compu alto")
    prompt_2 = st.text_area("Prompt para el modelo", value=example_prompt_spa, height=150)
    model_2 = st.text_input("Modelo a utilizar", value="microsoft/phi-4")  # Nuevo campo
    submitted_2 = st.form_submit_button("Traducir SPA ➔ LSA")

    if submitted_2:
        payload = {
            "text": input_text_2,
            "prompt_user": prompt_2,
            "model": model_2
        }
        try:
            response = requests.post(f"{config.API_LSA}/translator/translator_spa", json=payload)
            result = response.json().get("response", {}).get("result", "Sin resultado")
            st.text_area("Resultado", value=result, height=150)
        except Exception as e:
            st.error(f"Error al llamar al endpoint: {e}")