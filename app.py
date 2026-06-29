import requests
import streamlit as st

st.title("genshin artefatos")

def genshin_artefatos():
    try:
        endpoint = "https://genshin.jmp.blue/artifacts"
        response = requests.get(endpoint, timeout=5)
        response.raise_for_status()

        data = response.json()
        return {
            "data": data,
            "ok": True 
                }
    
    except requests.exceptions.Timeout:
        return {
            "ok":False,
            "error": "A API demorou demais para carregar"
        }

    except requests.exceptions.HTTPError:
        return {
            "ok":False,
            "error": "A API saiu do ar"
        }

    except requests.exceptions.InvalidURL:
        return {
            "ok":False,
            "error": "A URL está errada"
        }

artefatos = genshin_artefatos()

st.subheader("Lista de artefatos")

if artefatos["ok"]:
    for artefato in artefatos["data"]:
        st.markdown(f"- {artefato}")
    
else:
    st.error(artefatos["error"])

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

