# Audit Readiness AI — Project Context

## 1. Objetivo do projeto

Desenvolver o Audit Readiness AI, um sistema voltado ao apoio de processos de preparação para auditorias, utilizando recursos de software e inteligência artificial.

> Esta seção será detalhada conforme os requisitos e objetivos forem definidos durante o desenvolvimento.

---

## 2. Estado atual do projeto

O projeto está em fase inicial de desenvolvimento (Sprint 1, sem IA).

A estrutura inicial do projeto já foi criada, o ambiente de desenvolvimento está configurado e a navegação inicial da Nova Auditoria está implementada: a tela inicial leva a uma página própria, com a estrutura inicial do formulário para o processo Gestão de Mudanças (Change Management).

---

## 3. Tecnologias

- Python
- Streamlit
- Git
- GitHub

> Outras tecnologias serão adicionadas conforme o desenvolvimento avançar.

---

## 4. Estrutura atual

A estrutura do projeto está organizada em diretórios para separar responsabilidades:

- `app.py` — tela inicial do Streamlit
- `pages/` — interface (páginas do Streamlit); contém `1_nova_auditoria.py`
- `core/` — regras de negócio (ainda vazio)
- `services/` — integrações e processamento (ainda vazio)
- `prompts/` — comportamento da IA (ainda vazio)
- `models/` — estruturas de dados (ainda vazio)
- `data/` — controles e exemplos (ainda vazio)
- `utils/` — funções auxiliares (ainda vazio)
- `test_cases/` — ainda vazio
- `requirements.txt` — dependências (Streamlit com versão fixada)

As pastas ainda vazias contêm apenas `.gitkeep`.

> Esta seção deve ser atualizada sempre que a estrutura do projeto sofrer alterações relevantes.

---

## 5. Funcionalidades implementadas

- [x] Estrutura inicial do projeto
- [x] Estrutura inicial de diretórios
- [x] Configuração inicial do Streamlit
- [x] Versionamento do projeto com Git
- [x] Repositório remoto configurado no GitHub
- [x] Navegação inicial: o botão "Nova Auditoria" da tela inicial leva à página `pages/1_nova_auditoria.py`
- [x] Página Nova Auditoria com estrutura inicial do formulário (seleção do processo Gestão de Mudanças; sem persistência definitiva)

---

## 6. Em desenvolvimento

Nenhuma funcionalidade está em desenvolvimento no momento.

Ainda não implementado na Sprint 1: biblioteca de controles e criticidade. Os campos adicionais do formulário de Nova Auditoria ainda não foram definidos.

---

## 7. Próximas etapas

As próximas etapas serão definidas conforme os requisitos do sistema forem detalhados.

---

## 8. Decisões técnicas

### Versionamento

O projeto utiliza Git para controle de versão e GitHub como repositório remoto.

### Interface

O Streamlit foi adotado como tecnologia inicial para a interface da aplicação.

### Navegação

A navegação usa o recurso de múltiplas páginas do Streamlit: arquivos dentro de `pages/` viram páginas da aplicação, e o botão da tela inicial usa `st.switch_page("pages/1_nova_auditoria.py")`. Não há solução de navegação customizada.

### Lista de processos

Nesta etapa, o único processo disponível (Gestão de Mudanças) é uma constante simples dentro de `pages/1_nova_auditoria.py`. Não foi criado um modelo de domínio em `models/`, porque ainda não há atributos ou regras definidos que justifiquem isso. A decisão deve ser revista quando a biblioteca de controles precisar associar controles a processos.

### Ambiente

O desenvolvimento utiliza um ambiente virtual Python (`.venv`), mantido fora do versionamento por meio do `.gitignore`.

---

## 9. Problemas conhecidos

Nenhum problema conhecido registrado no momento.

---

## 10. Última atualização

Data: 01/10/2026

Último commit conhecido:

`c30be63` — estado atual publicado no GitHub.

As alterações da Tarefa 01 (navegação e estrutura inicial da Nova Auditoria) foram implementadas, commitadas e enviadas ao repositório remoto.

---

## 11. Regras para desenvolvimento

Este arquivo representa o estado atual conhecido do projeto.

Alterações relevantes na arquitetura, tecnologias, funcionalidades ou decisões técnicas devem ser registradas aqui.

O código deve permanecer versionado no Git.

Após alterações relevantes, o contexto do projeto deve ser atualizado para manter o projeto compreensível para qualquer pessoa ou ferramenta que venha a trabalhar nele.