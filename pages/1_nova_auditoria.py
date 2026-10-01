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
    "Preencha os dados iniciais da avaliação que será preparada."
)

if st.button("← Voltar ao início"):
    st.switch_page("app.py")

st.divider()

st.subheader("Dados da avaliação")

with st.form("form_nova_auditoria"):
    nome_avaliacao = st.text_input("Nome da avaliação")

    processo = st.selectbox(
        "Processo",
        options=PROCESSOS_DISPONIVEIS,
    )
    st.caption(
        "Neste momento, o único processo disponível é Gestão de Mudanças."
    )

    st.markdown("**Período avaliado**")
    col_inicial, col_final = st.columns(2)
    with col_inicial:
        data_inicial = st.date_input(
            "Data inicial",
            value=None,
            format="DD/MM/YYYY",
        )
    with col_final:
        data_final = st.date_input(
            "Data final",
            value=None,
            format="DD/MM/YYYY",
        )

    objetivo = st.text_area("Objetivo")

    escopo = st.text_area("Escopo")

    descricao_processo = st.text_area("Descrição do processo")

    enviado = st.form_submit_button("Continuar")

if enviado:
    # Guarda apenas durante a sessão atual; não há persistência definitiva.
    st.session_state["nova_auditoria"] = {
        "nome_avaliacao": nome_avaliacao,
        "processo": processo,
        "data_inicial": data_inicial,
        "data_final": data_final,
        "objetivo": objetivo,
        "escopo": escopo,
        "descricao_processo": descricao_processo,
    }

    st.success("Dados da avaliação recebidos nesta sessão.")
    st.info(
        "🚧 As próximas etapas da Nova Auditoria "
        "(como a seleção de controles) ainda não foram implementadas."
    )