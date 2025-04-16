import streamlit as st
import requests

st.set_page_config(page_title="Traductor LSA <> SPA", layout="centered")
st.title("Traductor LSA ⬌️ SPA con LLM")

# Estilos para separar los formularios
st.markdown("---")

# 🔹 Formulario 1: LSA ➔ SPA
st.subheader("Formulario 1: LSA a Español")
with st.form("lsa_form"):
    input_text_1 = st.text_input("Oración en LSA")
    prompt_1 = st.text_area("Prompt para el modelo")
    submitted_1 = st.form_submit_button("Traducir LSA ➔ SPA")

    if submitted_1:
        payload = {
            "text": input_text_1,
            "prompt_user": prompt_1
        }
        try:
            response = requests.post("http://localhost:8000/translator/translator_lsa", json=payload)
            result = response.json().get("response", {}).get("result", "Sin resultado")
            st.text_area("Resultado", value=result, height=150)
        except Exception as e:
            st.error(f"Error al llamar al endpoint: {e}")

# Separador visual
st.markdown("---")

# 🔹 Formulario 2: Español a LSA
st.subheader("Formulario 2: Español a LSA")
with st.form("spa_form"):
    input_text_2 = st.text_input("Oración en Español")
    prompt_2 = st.text_area("Prompt para el modelo")
    submitted_2 = st.form_submit_button("Traducir SPA ➔ LSA")

    if submitted_2:
        payload = {
            "text": input_text_2,
            "prompt_user": prompt_2
        }
        try:
            response = requests.post("http://localhost:8000/translator/translator_spa", json=payload)
            result = response.json().get("response", {}).get("result", "Sin resultado")
            st.text_area("Resultado", value=result, height=150)
        except Exception as e:
            st.error(f"Error al llamar al endpoint: {e}")