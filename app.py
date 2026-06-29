import requests
import streamlit as st

st.title("genshin artefatos")

def genshin_artefatos():
    endpoint = "https://genshin.jmp.blue/artifacts"
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json()
    else: 
        return []

artefatos = genshin_artefatos()

st.subheader("Lista de artefatos")

for artefato in artefatos:
    st.markdown(f"- {artefato}")