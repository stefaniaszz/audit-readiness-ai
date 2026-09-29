import streamlit as st

st.set_page_config(
    page_title="Audit Readiness AI",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Audit Readiness AI")

st.subheader("Preparação inteligente para auditorias de tecnologia")

st.write(
    "Ferramenta para apoiar a preparação para auditorias, "
    "identificando lacunas, evidências necessárias e pontos de atenção."
)

st.divider()

st.info(
    "🚧 Projeto em desenvolvimento — Sprint 1"
)

st.button("Nova Auditoria")