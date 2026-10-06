# Página inicial (Home) da aplicação Audit Readiness AI.
#
# Como a navegação funciona:
# este arquivo (app.py) é o ponto de partida da aplicação: é ele que roda
# quando usamos `streamlit run app.py`. Como existe uma pasta `pages/`, o
# Streamlit monta sozinho o menu lateral, com a Home (este arquivo) e uma
# entrada para cada página dentro de `pages/`.

import streamlit as st

# Define o título da aba do navegador, o ícone e a largura da página.
# Deve ser o primeiro comando do Streamlit executado nesta página.
st.set_page_config(
    page_title="Audit Readiness AI",
    page_icon="🔎",
    layout="wide"
)

# Nome da aplicação.
st.title("🔎 Audit Readiness AI")

# Subtítulo com a finalidade resumida da ferramenta.
st.subheader("Preparação para auditorias de tecnologia")

# Breve explicação do propósito da ferramenta.
st.write(
    "Ferramenta para apoiar a preparação para auditorias de tecnologia, "
    "identificando lacunas, evidências necessárias e pontos de atenção."
)

# Linha separadora entre a apresentação e a chamada para começar.
st.divider()

# Chamada para iniciar uma nova avaliação.
st.write("Para começar, inicie uma nova avaliação.")

# st.button devolve True somente no momento em que o botão é clicado.
# Quando isso acontece, st.switch_page troca para a página indicada. O caminho
# é relativo à pasta onde está o app.py e precisa apontar para um arquivo
# dentro de `pages/`.
# type="primary" destaca o botão como a ação principal desta tela.
if st.button("Nova Auditoria", type="primary"):
    st.switch_page("pages/1_nova_auditoria.py")

# Aviso discreto de que a aplicação ainda está em desenvolvimento.
st.caption("🚧 Projeto em desenvolvimento.")