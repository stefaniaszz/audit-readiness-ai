# Página "Nova Auditoria".
# Reúne o formulário com os dados iniciais da avaliação. Os dados enviados
# ficam apenas na sessão atual: ainda não há banco de dados nem persistência.
# Ao clicar em "Voltar ao início", os dados da avaliação atual são descartados.

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

# Número da "versão" do formulário. Ele faz parte do nome (key) do formulário e
# de cada campo. Sempre que o usuário volta ao início, o número aumenta em 1;
# assim, na próxima visita, o Streamlit cria campos novos, com valores vazios.
# (Mudar a key é mais seguro do que tentar apagar o valor de campos existentes.)
versao = st.session_state.get("nova_auditoria_versao", 0)

if st.button("← Voltar ao início"):
    # Descarta os dados da avaliação atual (se existirem) e troca a versão
    # do formulário, o que "limpa" os campos para a próxima visita.
    st.session_state.pop("nova_auditoria", None)
    st.session_state["nova_auditoria_versao"] = versao + 1
    st.switch_page("app.py")

st.divider()

# st.form agrupa os campos: a página só reage (e valida) quando o botão de
# envio é clicado, e não a cada letra digitada.
with st.form(f"form_nova_auditoria_{versao}"):
    st.subheader("Identificação")

    nome_avaliacao = st.text_input("Nome da avaliação", key=f"nome_avaliacao_{versao}")

    processo = st.selectbox(
        "Processo",
        options=PROCESSOS_DISPONIVEIS,
        key=f"processo_{versao}",
    )
    st.caption(
        "Neste momento, o único processo disponível é Gestão de Mudanças."
    )

    st.subheader("Período avaliado")

    col_inicial, col_final = st.columns(2)
    with col_inicial:
        # value=None deixa a data vazia (sem valor padrão).
        data_inicial = st.date_input(
            "Data inicial",
            value=None,
            format="DD/MM/YYYY",
            key=f"data_inicial_{versao}",
        )
    with col_final:
        data_final = st.date_input(
            "Data final",
            value=None,
            format="DD/MM/YYYY",
            key=f"data_final_{versao}",
        )

    st.subheader("Contexto da avaliação")

    # Objetivo, escopo e descrição são opcionais.
    # O objetivo explica o propósito da avaliação e os resultados esperados;
    # o texto é guardado na chave "objetivo" (veja o dicionário mais abaixo).
    objetivo = st.text_area("Objetivo da avaliação", key=f"objetivo_{versao}")
    st.caption(
        "Descreva o propósito da avaliação e os resultados esperados."
    )

    escopo = st.text_area("Escopo da avaliação", key=f"escopo_{versao}")
    st.caption(
        "Delimite os processos, controles, áreas ou unidades incluídos na avaliação."
    )

    descricao_processo = st.text_area("Descrição do processo", key=f"descricao_processo_{versao}")

    enviado = st.form_submit_button("Enviar dados")

# Tudo abaixo só acontece depois do clique em "Enviar dados".
if enviado:
    # Lista com as mensagens de erro encontradas na validação.
    erros = []

    # strip() remove espaços das pontas: um nome só com espaços conta como vazio.
    nome_avaliacao = nome_avaliacao.strip()
    if not nome_avaliacao:
        erros.append("Informe o nome da avaliação.")

   
    # As duas datas são obrigatórias.
    if data_inicial is None:
        erros.append("Informe a data inicial.")

    if data_final is None:
        erros.append("Informe a data final.")

    # A ordem só é comparada quando as duas datas foram preenchidas.
    # Datas iguais são permitidas: só é erro quando a inicial vem DEPOIS da final.
    if data_inicial is not None and data_final is not None and data_inicial > data_final:
        erros.append("A data inicial não pode ser posterior à data final.")

    if erros:
        # Com erros, nada é guardado: o usuário corrige e envia de novo.
        for erro in erros:
            st.error(erro)
    else:
        # Só chegamos aqui se todas as validações passaram.
        # st.session_state guarda os dados enquanto a sessão estiver aberta.
        st.session_state["nova_auditoria"] = {
            "nome_avaliacao": nome_avaliacao,
            "processo": processo,
            "data_inicial": data_inicial,
            "data_final": data_final,
            "objetivo": objetivo,
            "escopo": escopo,
            "descricao_processo": descricao_processo,
        }

        st.success("Dados da avaliação recebidos com sucesso.")
        st.info(
            "Os dados permanecem apenas na sessão atual e não foram salvos "
            "permanentemente. Se você recarregar ou fechar a página, "
            "eles serão perdidos."
        )

        st.subheader("Resumo dos dados enviados")

        # Datas no formato brasileiro; campos vazios aparecem como "Não informado".
        resumo = [
            ("Nome da avaliação", nome_avaliacao),
            ("Processo", processo),
            (
                "Data inicial",
                data_inicial.strftime("%d/%m/%Y") if data_inicial else "Não informada",
            ),
            (
                "Data final",
                data_final.strftime("%d/%m/%Y") if data_final else "Não informada",
            ),
            ("Objetivo da avaliação", objetivo.strip() or "Não informado"),
            ("Escopo da avaliação", escopo.strip() or "Não informado"),
            ("Descrição do processo", descricao_processo.strip() or "Não informada"),
        ]

        for rotulo, valor in resumo:
            st.markdown(f"**{rotulo}**")
            # st.text mostra o texto exatamente como foi digitado, sem
            # interpretar símbolos de formatação (como * ou #).
            st.text(valor)

        st.info(
            "🚧 As próximas etapas da Nova Auditoria "
            "(como a seleção de controles) ainda não foram implementadas."
        )