# Página "Configurações".
# No futuro, vai reunir as configurações da aplicação.
# Por enquanto é apenas uma página provisória.
#
# A navegação funciona como explicado em 2_resultado.py: o Streamlit cria o
# menu lateral a partir dos arquivos da pasta `pages/`.
#
# Observação: o nome do arquivo não tem acento (configuracoes) de propósito,
# para evitar problemas com nomes de arquivo em diferentes sistemas. Por isso
# o texto do menu lateral aparece sem acento. O título abaixo, que é um texto
# do código, pode ter acento normalmente.

import streamlit as st

# Título da aba do navegador, ícone e largura da página
# (deve ser o primeiro comando do Streamlit nesta página).
st.set_page_config(
    page_title="Configurações | Audit Readiness AI",
    page_icon="🔎",
    layout="wide"
)

st.title("Configurações")

# Aviso provisório, até esta funcionalidade ser desenvolvida.
st.info("🚧 Esta funcionalidade ainda está em desenvolvimento.")