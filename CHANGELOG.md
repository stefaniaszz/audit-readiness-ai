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
- URL pública: `https://audit-readiness-ai-xvskt2cm2b6exsv2v6bjx.streamlit.app/`.

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

## Próximas alterações

As próximas mudanças relevantes deverão ser registradas neste arquivo conforme o desenvolvimento avançar.