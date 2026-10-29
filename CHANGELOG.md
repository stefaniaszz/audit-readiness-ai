# Changelog — Audit Readiness AI

Registro das principais alterações realizadas no projeto.

---

## 2026-09-29 — Estrutura inicial

Commit: `c2c2e9d`

- Criada a estrutura inicial do projeto.
- Inicializado o versionamento com Git.
- Criado o repositório inicial do projeto.

---

## 2026-10-01 — Estrutura de diretórios

Commit: `13a0dd5`

- Adicionada a estrutura inicial de diretórios.
- Organização inicial dos arquivos do projeto.

---

## 2026-10-01 — Fixação da versão do Streamlit

Commit: `ec495cc`

- Fixada a versão utilizada do Streamlit.
- Atualizada a configuração de dependências do projeto.

---

## 2026-10-01 — Navegação e estrutura inicial da Nova Auditoria

Commit: `ecbdd33`

- Criada a página `pages/1_nova_auditoria.py` com a estrutura inicial do formulário, incluindo a seleção do processo Gestão de Mudanças (Change Management).
- O botão "Nova Auditoria" do `app.py` passou a direcionar para a nova página.
- Adicionado botão para voltar à tela inicial.
- Sem IA, motor de avaliação, análise de evidências, score, dashboard, banco de dados ou persistência definitiva.

---

## 2026-10-01 — Formulário completo de Nova Auditoria

Commit: `de674a9`

- Completo o formulário da página `pages/1_nova_auditoria.py` conforme a especificação, mantendo o processo disponível como Gestão de Mudanças (Change Management).
- Adicionados os campos: Nome da avaliação, Período avaliado (Data inicial e Data final), Objetivo, Escopo e Descrição do processo.
- Os campos começam vazios; as datas utilizam o formato DD/MM/YYYY.
- Ao enviar, os dados são armazenados em `st.session_state` e a página apresenta uma confirmação simples. Não há persistência definitiva.
- Sem validação de campos obrigatórios ou de período, sem IA, biblioteca de controles, criticidade, score, dashboard ou banco de dados.

---

## 2026-10-06 — Navegação principal da aplicação

Commit: `3189620`

- Criadas as páginas provisórias `pages/2_resultado.py`, `pages/3_simulador_auditor.py` e `pages/4_configuracoes.py`, cada uma contendo título e aviso de que a funcionalidade está em desenvolvimento.
- A navegação utiliza o menu lateral automático do Streamlit, gerado a partir dos arquivos presentes em `pages/`.
- O `app.py` e a página `pages/1_nova_auditoria.py` não foram alterados nesta etapa.
- Adicionados comentários explicativos nas novas páginas para facilitar a compreensão da estrutura e da navegação.
- Não foram implementadas funcionalidades de resultado, simulação ou configurações nesta etapa.

---

## 2026-10-06 — Home da aplicação 

Commit: `32dd9ad`

- Ajustada a Home (`app.py`) para apresentar o nome "Audit Readiness AI", uma breve explicação do propósito da ferramenta e uma chamada para iniciar uma nova avaliação.
- O botão "Nova Auditoria" foi destacado (`type="primary"`) e continua levando a `pages/1_nova_auditoria.py` com `st.switch_page`.
- O subtítulo passou de "Preparação inteligente para auditorias de tecnologia" para "Preparação para auditorias de tecnologia", pois ainda não há IA.
- O aviso "Projeto em desenvolvimento — Sprint 1" foi substituído por uma legenda discreta.
- Adicionados comentários explicativos no `app.py`.
- As páginas de `pages/` e o `requirements.txt` não foram alterados. Sem novas dependências.

---

## 2026-10-06 — Primeiro deploy no Streamlit Community Cloud 

- Publicada a primeira versão da aplicação no Streamlit Community Cloud.
- Repositório utilizado: `stefaniaszz/audit-readiness-ai`.
- Branch utilizada: `master`.
- Arquivo principal da aplicação: `app.py`.
- Aplicação disponibilizada através de uma URL pública.
- Realizados testes da Home e das páginas de Nova Auditoria, Resultado, Simulador Auditor e Configurações.
- Todas as páginas foram carregadas e utilizadas sem erros.
- Não foram necessárias alterações no código da aplicação ou inclusão de novas dependências para realizar o deploy.
- URL pública: `https://audit-readiness-ai-xvskt2cm2b6exsv2v6vbjx.streamlit.app/`.

---

## 2026-10-13 — Validação do formulário de Nova Auditoria (AR11)

Commit: `548fbc7` (`feat: validar formulário de nova auditoria`)

- Reorganizado o formulário de `pages/1_nova_auditoria.py` nas seções Identificação, Período avaliado e Contexto da avaliação.
- O botão "Continuar" passou a se chamar "Enviar dados".
- Adicionada validação ao enviar: o nome da avaliação é obrigatório (um nome só com espaços é considerado vazio) e, quando as duas datas forem informadas, a data inicial não pode ser posterior à data final. Cada erro tem mensagem específica.
- Datas, objetivo, escopo e descrição do processo continuam opcionais.
- Os dados passaram a ser gravados em `st.session_state["nova_auditoria"]` somente depois que todas as validações passam (o nome é gravado sem espaços nas pontas).
- Após um envio válido, a página mostra a confirmação, um aviso de que os dados ficam apenas na sessão atual e não são salvos permanentemente, um resumo dos dados enviados (datas em DD/MM/YYYY; campos vazios como "Não informado") e o aviso sobre as próximas etapas.
- Ao clicar em "← Voltar ao início", os dados da avaliação atual são descartados: `st.session_state["nova_auditoria"]` é removido e o formulário volta vazio na próxima visita. Para isso, o nome do formulário e das chaves dos campos passou a incluir um número de versão (`st.session_state["nova_auditoria_versao"]`), que aumenta a cada descarte. O descarte vale somente para esse botão.
- Adicionados comentários explicativos nas partes novas da página.
- Alteração restrita a `pages/1_nova_auditoria.py`; `app.py`, `requirements.txt` e as demais páginas não foram alterados. Sem novas dependências.
- Testado manualmente pela desenvolvedora no VS Code; todos os testes realizados passaram.
- Sem persistência definitiva e sem funcionalidades de IA.
- O commit foi enviado ao GitHub, mas ainda não há registro de que a aplicação publicada no Streamlit Community Cloud tenha sido atualizada com esta alteração.

---

## 2026-10-27 — Datas obrigatórias na Nova Auditoria (AR13)

Commit: `e05efc7` (`feat: validar datas da nova auditoria`)

- Em `pages/1_nova_auditoria.py`, a data inicial e a data final passaram a ser obrigatórias: cada data não preenchida gera a sua própria mensagem de erro ("Informe a data inicial." / "Informe a data final.").
- A regra de ordem foi mantida: a data inicial não pode ser posterior à data final (datas iguais são permitidas), verificada somente quando as duas datas foram informadas.
- Os dados continuam sendo gravados em `st.session_state["nova_auditoria"]` somente depois que todas as validações passam. Objetivo, escopo e descrição do processo continuam opcionais.
- Esse commit removeu, sem intenção, dois elementos da AR11 (o aviso de que os dados ficam apenas na sessão atual e o subtítulo "Resumo dos dados enviados"); eles foram restaurados na alteração da AR14, descrita abaixo.
- Alteração restrita a `pages/1_nova_auditoria.py`. Sem novas dependências e sem persistência definitiva.

---

## 2026-10-28 — Campo "Objetivo da avaliação" (AR14)

Commit: `e31d9cb` (`feat: melhorar identificação do objetivo da avaliação`)

- Em `pages/1_nova_auditoria.py`, o campo "Objetivo" passou a se chamar "Objetivo da avaliação" e ganhou uma orientação curta logo abaixo (`st.caption`): "Descreva o propósito da avaliação e os resultados esperados."
- O campo continua opcional e continua guardado na chave `objetivo` do dicionário já existente em `st.session_state["nova_auditoria"]` (nenhuma estrutura nova). No resumo após o envio, aparece como "Objetivo da avaliação" (ou "Não informado", se vazio).
- Restaurados os dois elementos da AR11 removidos sem intenção pelo commit `e05efc7`: o aviso `st.info` de que os dados ficam apenas na sessão atual e o subtítulo "Resumo dos dados enviados".
- As validações da AR13 (nome e datas obrigatórias, ordem das datas) foram preservadas.
- Alteração restrita a `pages/1_nova_auditoria.py`; `app.py`, `requirements.txt` e as demais páginas não foram alterados. Sem novas dependências, sem banco de dados e sem persistência definitiva.
- Verificações realizadas em 28/10/2026: verificação de sintaxe (`py_compile`), simulação da interface com `streamlit.testing.v1.AppTest` (envio vazio, nome só com espaços, data ausente, ordem inválida, datas iguais, envio válido, resumo, descarte ao voltar ao início, abertura das demais páginas) e subida do servidor Streamlit com resposta de saúde HTTP 200. O ambiente usado foi Python 3.13 com Streamlit 1.64.0. Não há testes automatizados (`pytest`) no repositório. Validação manual no navegador pela desenvolvedora (28/10/2026): a AR14 foi testada e funcionou.
- O commit da AR14 (`e31d9cb`) foi enviado ao GitHub (branch `master`), assim como o da AR13 (`e05efc7`), mas não há registro de que a aplicação publicada no Streamlit Community Cloud contenha as alterações da AR13 e da AR14.

---

## 2026-10-28 — Campo "Escopo da avaliação" (AR15)

Commit: `1edd2a5` (`feat: melhorar identificação do escopo da avaliação`)

- Em `pages/1_nova_auditoria.py`, o campo "Escopo" passou a se chamar "Escopo da avaliação" e ganhou uma orientação curta (`st.caption`): "Delimite os processos, controles, áreas ou unidades incluídos na avaliação."
- O campo permanece opcional e mantém a chave `escopo` no dicionário `st.session_state["nova_auditoria"]` (nenhuma estrutura nova).
- O resumo dos dados enviados identifica o campo como "Escopo da avaliação" e exibe "Não informado" quando vazio.
- Preservadas as validações de nome e período (AR11/AR13), o campo "Objetivo da avaliação" e sua orientação (AR14), a confirmação, o aviso de armazenamento na sessão e o subtítulo do resumo.
- Alteração de código restrita a `pages/1_nova_auditoria.py`. Sem novas dependências, persistência definitiva ou mudanças na estrutura do projeto.
- Verificações realizadas em 28/10/2026: verificação de sintaxe (`py_compile`), simulação da interface com `streamlit.testing.v1.AppTest` (campos e orientações, escopo guardado na chave `escopo`, exibição literal e "Não informado" no resumo, validações de nome e datas, descarte ao voltar ao início, abertura das demais páginas) e subida do servidor Streamlit com resposta de saúde HTTP 200. Não há testes automatizados (`pytest`) no repositório.
- Validação manual no navegador pela desenvolvedora (28/10/2026): a AR15 foi testada e funcionou.
- O commit da AR15 (`1edd2a5`) foi enviado ao GitHub (branch `master`).

---

## 2026-10-28 — Orientação do campo "Descrição do processo" (AR16)

Commit: `7528282` (`feat: orientar preenchimento da descrição do processo`)

- Em `pages/1_nova_auditoria.py`, o campo existente "Descrição do processo" ganhou uma orientação curta logo abaixo (`st.caption`): "Descreva como o processo funciona atualmente, incluindo as principais atividades, as responsabilidades e os controles existentes."
- O campo permanece opcional, sem novas validações nem novos campos, e mantém a chave `descricao_processo` no dicionário `st.session_state["nova_auditoria"]` (nenhuma estrutura nova). O rótulo e o resumo ("Descrição do processo" ou "Não informada", se vazio) não foram alterados.
- Preservadas as validações de nome e datas (AR11/AR13), as orientações dos campos "Objetivo da avaliação" (AR14) e "Escopo da avaliação" (AR15), a confirmação, o aviso de armazenamento na sessão e o subtítulo do resumo.
- Alteração de código restrita a `pages/1_nova_auditoria.py`. Sem novas dependências, persistência definitiva ou análises. O texto informado apenas fica disponível na sessão para análises futuras, que não fazem parte desta tarefa.
- Verificações realizadas em 28/10/2026: verificação de sintaxe (`py_compile`), simulação da interface com `streamlit.testing.v1.AppTest` (22 verificações: orientação exibida com o texto exato, texto guardado na chave `descricao_processo`, exibição literal no resumo, "Não informada" quando vazio, validações de nome e datas, aviso de sessão e subtítulo do resumo, abertura das demais páginas), fluxo Home, Nova Auditoria, envio, "Voltar ao início" e reabertura com campos vazios, e subida do servidor Streamlit com resposta de saúde HTTP 200. Não há testes automatizados (`pytest`) no repositório.
- Validação manual no navegador pela desenvolvedora (28/10/2026): a AR16 foi testada e funcionou.
- O commit da AR16 (`7528282`) foi enviado ao GitHub (branch `master`).

---

## 2026-10-28 — Modelo de dados da avaliação (AR17)

Commit: pendente (alterações ainda não commitadas)

- Criado `models/avaliacao.py` com a classe `Avaliacao`, um `dataclass` imutável (biblioteca padrão, sem novas dependências) que reúne os dados da avaliação: `nome_avaliacao`, `processo`, `data_inicial`, `data_final`, `objetivo`, `escopo`, `descricao_processo` e `controles_selecionados`. Os nomes são os mesmos já usados em `st.session_state["nova_auditoria"]`.
- Obrigatórios (mesmas regras do formulário): nome (texto não vazio; só espaços conta como vazio), processo (texto não vazio) e as duas datas (tipo `date`; a inicial não pode ser posterior à final; datas iguais permitidas). Opcionais, com padrão vazio: objetivo, escopo, descrição do processo e controles selecionados. Dados inválidos geram `ValueError`.
- `controles_selecionados` é uma tupla de textos (identificadores). Ainda não existem biblioteca de controles nem seleção na interface, e nada disso foi criado: o campo fica sempre vazio por enquanto, e seu tipo poderá ser revisto quando a biblioteca existir.
- `para_dicionario()` gera o dicionário no formato do formulário, mais `controles_selecionados` (lista vazia); `de_dicionario()` faz o caminho inverso e aceita o dicionário antigo, sem essa chave.
- Em `pages/1_nova_auditoria.py`, adicionados o import de `Avaliacao` e, no envio válido, a criação do objeto e a gravação de `avaliacao.para_dicionario()` na mesma chave `st.session_state["nova_auditoria"]`. Campos, validações, mensagens, resumo e demais comportamentos foram preservados; não houve mudança visual na interface.
- Criado `test_cases/test_avaliacao.py` com 18 testes `unittest` (criação e campos, obrigatórios, opcionais, tipos, compatibilidade com o dicionário do formulário).
- Atualizados `PROJECT_CONTEXT.md` e `CHANGELOG.md`; corrigido o estado das AR15 e AR16, que já estão commitadas (`1edd2a5` e `7528282`) e enviadas ao GitHub.
- Verificações realizadas em 28/10/2026 no ambiente de desenvolvimento do Claude (Python 3.13 e Streamlit 1.64.0): `py_compile` dos arquivos `.py`; `python -m unittest test_cases.test_avaliacao -v` (18 testes, todos aprovados); simulação da interface com `streamlit.testing.v1.AppTest` (22 de 22 verificações aprovadas; a verificação das chaves do dicionário foi atualizada para incluir `controles_selecionados`) e fluxo Home, Nova Auditoria, envio, "Voltar ao início" e reabertura; subida do servidor Streamlit com resposta de saúde HTTP 200 e um envio válido em navegador automatizado (Playwright), confirmando que o import funciona na página. Não foi usado `pytest`.
- Ainda não validada manualmente no navegador pela desenvolvedora e não commitada nem enviada ao GitHub.
- Limitações: sem biblioteca de controles, seleção de controles na interface, banco de dados, persistência definitiva ou análise por IA, que dependem de tarefas futuras. Os dados continuam apenas na sessão atual, e o restante da página ainda lê o dicionário, não o objeto.

---

## Próximas alterações

As próximas mudanças relevantes deverão ser registradas neste arquivo conforme o desenvolvimento avançar.
