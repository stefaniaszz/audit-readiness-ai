# Changelog — Audit Readiness AI

Registro das principais alterações realizadas no projeto.

---

## 2026-09-XX — Estrutura inicial

Commit: `c2c2e9d`

- Criada a estrutura inicial do projeto.
- Inicializado o versionamento com Git.
- Criado o repositório inicial do projeto.

---

## 2026-09-XX — Estrutura de diretórios

Commit: `13a0dd5`

- Adicionada a estrutura inicial de diretórios.
- Organização inicial dos arquivos do projeto.

---

## 2026-09-XX — Fixação da versão do Streamlit

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

- Criadas as páginas provisórias `pages/2_resultado.py`, `pages/3_simular_auditor.py` e `pages/4_configuracoes.py`, cada uma contendo título e aviso de que a funcionalidade está em desenvolvimento.
- A navegação utiliza o menu lateral automático do Streamlit, gerado a partir dos arquivos presentes em `pages/`.
- O `app.py` e a página `pages/1_nova_auditoria.py` não foram alterados nesta etapa.
- Adicionados comentários explicativos nas novas páginas para facilitar a compreensão da estrutura e da navegação.
- Não foram implementadas funcionalidades de resultado, simulação ou configurações nesta etapa.


---

## 2026-10-06 — Navegação principal da aplicação 

Commit: `3189620`

- Criadas as páginas provisórias `pages/2_resultado.py`, `pages/3_simular_auditor.py` e `pages/4_configuracoes.py`, cada uma contendo título e aviso de que a funcionalidade está em desenvolvimento.
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


## Próximas alterações

As próximas mudanças relevantes deverão ser registradas neste arquivo conforme o desenvolvimento avançar.