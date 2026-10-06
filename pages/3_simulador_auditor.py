# Página "Simular Auditor".
# No futuro, vai permitir simular como um auditor avaliaria o processo.
# Por enquanto é apenas uma página provisória.
#
# A navegação funciona como explicado em 2_resultado.py: o Streamlit cria o
# menu lateral a partir dos arquivos da pasta `pages/`.

import streamlit as st

# Título da aba do navegador, ícone e largura da página
# (deve ser o primeiro comando do Streamlit nesta página).
st.set_page_config(
    page_title="Simular Auditor | Audit Readiness AI",
    page_icon="🔎",
    layout="wide"
)

st.title("Simular Auditor")

# Aviso provisório, até esta funcionalidade ser desenvolvida.
st.info("🚧 Esta funcionalidade ainda está em desenvolvimento.")