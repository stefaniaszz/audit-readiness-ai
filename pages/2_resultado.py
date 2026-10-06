# Página "Resultado".
# No futuro, vai mostrar o resultado de uma auditoria.
# Por enquanto é apenas uma página provisória.
#
# Como a navegação funciona:
# o Streamlit procura todos os arquivos .py dentro da pasta `pages/` e cria
# sozinho o menu lateral, uma entrada para cada arquivo (por isso não foi
# preciso alterar o app.py). O número no começo do nome do arquivo (2_) define
# a ordem no menu, e o resto do nome vira o texto exibido ("resultado").
# O mesmo vale para 1_nova_auditoria.py, 3_simular_auditor.py e
# 4_configuracoes.py.

import streamlit as st

# Define o título da aba do navegador, o ícone e a largura da página.
# Deve ser o primeiro comando do Streamlit executado nesta página.
st.set_page_config(
    page_title="Resultado | Audit Readiness AI",
    page_icon="🔎",
    layout="wide"
)

st.title("Resultado")

# Aviso provisório, até esta funcionalidade ser desenvolvida.
st.info("🚧 Esta funcionalidade ainda está em desenvolvimento.")