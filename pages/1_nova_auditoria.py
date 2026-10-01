import streamlit as st

# Neste MVP, o único processo disponível é Gestão de Mudanças.
PROCESSOS_DISPONIVEIS = ["Gestão de Mudanças (Change Management)"]

st.set_page_config(
    page_title="Nova Auditoria | Audit Readiness AI",
    page_icon="🔎",
    layout="wide"
)

st.title("Nova Auditoria")

st.write(
    "Inicie a preparação de uma nova auditoria escolhendo "
    "o processo que será avaliado."
)

if st.button("← Voltar ao início"):
    st.switch_page("app.py")

st.divider()

st.subheader("Processo a ser auditado")

st.caption(
    "Neste momento, o único processo disponível é Gestão de Mudanças."
)

with st.form("form_nova_auditoria"):
    processo = st.selectbox(
        "Processo",
        options=PROCESSOS_DISPONIVEIS,
    )

    enviado = st.form_submit_button("Continuar")

if enviado:
    # Guarda apenas durante a sessão atual; não há persistência definitiva.
    st.session_state["nova_auditoria"] = {"processo": processo}

    st.success(f"Processo selecionado: {processo}")
    st.info(
        "🚧 As próximas etapas da Nova Auditoria "
        "(como a seleção de controles) ainda não foram implementadas."
    )