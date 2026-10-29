# Audit Readiness AI — Project Context

## 1. Objetivo do projeto

Desenvolver o Audit Readiness AI, um sistema voltado ao apoio de processos de preparação para auditorias, utilizando recursos de software e inteligência artificial.

> Esta seção será detalhada conforme os requisitos e objetivos forem definidos durante o desenvolvimento.

---

## 2. Estado atual do projeto

O projeto está em fase inicial de desenvolvimento, atualmente na Sprint 2. Ainda não há funcionalidades de inteligência artificial implementadas.

A estrutura inicial do projeto já foi criada, o ambiente de desenvolvimento está configurado, a página Nova Auditoria está implementada com o formulário da especificação para o processo Gestão de Mudanças (Change Management), com validação do nome da avaliação e da ordem das datas, confirmação e resumo dos dados enviados e descarte dos dados ao clicar em "Voltar ao início" (AR11), com as datas inicial e final tornadas obrigatórias depois, pela AR13, e a navegação principal está preparada: o menu lateral do Streamlit dá acesso a Nova Auditoria, Resultado, Simular Auditor e Configurações. As três últimas são páginas provisórias, apenas com título e aviso de que estão em desenvolvimento.

A Home da aplicação foi implementada com a identificação do Audit Readiness AI, uma breve explicação do propósito da ferramenta e uma chamada para iniciar uma nova avaliação.

A primeira versão da aplicação foi publicada no Streamlit Community Cloud e está disponível através de uma URL pública. O deploy foi realizado a partir do repositório GitHub `stefaniaszz/audit-readiness-ai`, utilizando a branch `master` e o arquivo principal `app.py`.

A aplicação publicada foi validada funcionalmente. Foram testadas a Home, Nova Auditoria, Resultado, Simulador Auditor e Configurações, todas funcionando sem erros. Essa validação foi realizada no primeiro deploy, antes da AR11.

A AR11 (formulário de nova avaliação com validação, resumo e descarte dos dados ao voltar ao início) foi implementada, testada manualmente pela desenvolvedora, commitada (`548fbc7`) e enviada ao GitHub. O commit enviado ao GitHub não confirma, por si só, que o deploy publicado foi atualizado: ainda não há registro de que a aplicação publicada contenha a AR11.

A AR13 (datas inicial e final obrigatórias) foi commitada (`e05efc7`). Esse commit removeu, sem intenção, o aviso de sessão e o subtítulo "Resumo dos dados enviados" da AR11.

A AR14 (campo "Objetivo da avaliação", com orientação curta, mantido no resumo e na estrutura de dados existente) e a restauração desses dois elementos da AR11 estão implementadas em `pages/1_nova_auditoria.py` e foram validadas manualmente no navegador pela desenvolvedora (funcionou), commitadas (`e31d9cb`) e enviadas ao GitHub.

A AR15 (campo "Escopo da avaliação") está implementada em `pages/1_nova_auditoria.py` e foi validada manualmente no navegador pela desenvolvedora (funcionou), commitada (`1edd2a5`) e enviada ao GitHub.

A AR16 (orientação do campo "Descrição do processo") está implementada em `pages/1_nova_auditoria.py`, verificada com simulação da interface e validada manualmente no navegador pela desenvolvedora (funcionou), commitada (`7528282`) e enviada ao GitHub. Não há registro de que a aplicação publicada contenha a AR13, a AR14, a AR15 ou a AR16.

A AR17 (modelo de dados `Avaliacao`, em `models/avaliacao.py`) está implementada e integrada ao envio do formulário de Nova Auditoria. Foi verificada com testes automatizados (`unittest`) e com simulação da interface, mas **ainda não foi validada manualmente no navegador pela desenvolvedora nem commitada**.

Os dados informados no formulário de Nova Auditoria permanecem apenas na sessão atual: ainda não há persistência definitiva.

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
- `pages/` — interface (páginas do Streamlit); contém `1_nova_auditoria.py`, `2_resultado.py`, `3_simulador_auditor.py` e `4_configuracoes.py`
- `core/` — regras de negócio (ainda vazio)
- `services/` — integrações e processamento (ainda vazio)
- `prompts/` — comportamento da IA (ainda vazio)
- `models/` — estruturas de dados; contém `avaliacao.py` (modelo `Avaliacao`, AR17)
- `data/` — controles e exemplos (ainda vazio)
- `utils/` — funções auxiliares (ainda vazio)
- `test_cases/` — testes automatizados; contém `test_avaliacao.py` (testes do modelo `Avaliacao`, AR17)
- `requirements.txt` — dependências (Streamlit com versão fixada)

As pastas ainda vazias contêm apenas `.gitkeep`; `models/` e `test_cases/` também mantêm o `.gitkeep`.

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
- [x] Formulário de Nova Auditoria completo conforme a especificação (Nome da avaliação, Processo, Período avaliado, Objetivo, Escopo e Descrição do processo); os valores ficam apenas na sessão
- [x] Validação e resumo do formulário de Nova Auditoria (AR11): seções Identificação, Período avaliado e Contexto da avaliação; nome da avaliação obrigatório; na época da AR11, as datas ainda eram opcionais e a ordem (data inicial não posterior à data final) só era verificada quando as duas eram informadas, regra substituída pela AR13 (próximo item: as duas datas obrigatórias, data final não anterior à inicial e datas iguais permitidas); confirmação e resumo dos dados após envio válido; dados gravados em `st.session_state["nova_auditoria"]` somente após a validação, apenas na sessão atual e sem persistência definitiva; descarte dos dados e limpeza do formulário ao clicar em "← Voltar ao início" (commit `548fbc7`; testado manualmente pela desenvolvedora)
- [x] Datas obrigatórias na Nova Auditoria (AR13): data inicial e data final passaram a ser obrigatórias, cada uma com mensagem de erro própria; a regra de ordem foi mantida (commit `e05efc7`)
- [x] Campo "Objetivo da avaliação" (AR14), com orientação curta, opcional, exibido no resumo e guardado na chave `objetivo` da estrutura existente; inclui a restauração do aviso de sessão e do subtítulo "Resumo dos dados enviados" da AR11 (implementado e validado manualmente pela desenvolvedora; commit `e31d9cb`, enviado ao GitHub)
- [x] Campo "Escopo da avaliação" (AR15): campo opcional com rótulo e orientação, mantido na chave `escopo` e apresentado no resumo (implementado em `pages/1_nova_auditoria.py`; verificado com simulação da interface e validado manualmente pela desenvolvedora; commit `1edd2a5`, enviado ao GitHub)
- [x] Orientação do campo "Descrição do processo" (AR16): campo opcional mantido, com orientação sobre o funcionamento atual, as principais atividades, as responsabilidades e os controles existentes; chave `descricao_processo` e resumo preservados (implementado em `pages/1_nova_auditoria.py`; verificado com simulação da interface e validado manualmente pela desenvolvedora; commit `7528282`, enviado ao GitHub)
- [ ] Modelo de dados da avaliação (AR17): classe `Avaliacao` em `models/avaliacao.py`, que reúne nome, processo, período, objetivo, escopo, descrição do processo e controles selecionados; usada pelo formulário ao gravar `st.session_state["nova_auditoria"]` (implementado e testado com `unittest` e simulação da interface; ainda não validado manualmente no navegador nem commitado)
- [x] Navegação principal (AR-07): menu lateral do Streamlit com Nova Auditoria, Resultado, Simular Auditor e Configurações
- [x] Páginas provisórias `2_resultado.py`, `3_simulador_auditor.py` e `4_configuracoes.py` (apenas título e aviso de desenvolvimento)
- [x] Home da aplicação (AR-08), com identificação do sistema, descrição do propósito e acesso à Nova Auditoria

- [x] Primeiro deploy da aplicação no Streamlit Community Cloud (AR-09)

- [x] Validação da aplicação publicada, incluindo Home, Nova Auditoria, Resultado, Simulador Auditor e Configurações

---

## 6. Em desenvolvimento

A AR17 (modelo de dados `Avaliacao`) está implementada em `models/avaliacao.py` e integrada a `pages/1_nova_auditoria.py`, com testes em `test_cases/test_avaliacao.py`. Ainda não foi validada manualmente no navegador pela desenvolvedora nem commitada. A AR16 está concluída, commitada (`7528282`) e enviada ao GitHub, assim como a AR15 (`1edd2a5`) e a AR14 (`e31d9cb`). A AR11 e a AR13 estão concluídas e commitadas.

Ainda não implementados: biblioteca de controles e criticidade (itens listados no escopo original da Sprint 1) e a seleção de controles na interface; por isso `controles_selecionados` do modelo `Avaliacao` fica sempre vazio por enquanto. Também não existem funcionalidades de inteligência artificial nem persistência definitiva dos dados.

As páginas Resultado, Simular Auditor e Configurações existem apenas como espaços provisórios; suas funcionalidades ainda não foram desenvolvidas.

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

A navegação utiliza o recurso de múltiplas páginas do Streamlit: arquivos dentro de `pages/` são reconhecidos como páginas da aplicação, e o botão da tela inicial utiliza `st.switch_page("pages/1_nova_auditoria.py")`.

As páginas Resultado, Simular Auditor e Configurações foram adicionadas apenas criando os respectivos arquivos dentro de `pages/`; o `app.py` não precisou ser alterado.

O número no início do nome do arquivo define a ordem das páginas no menu lateral. O restante do nome do arquivo é utilizado pelo Streamlit para definir o nome exibido no menu. Por isso, os nomes dos arquivos não utilizam acentos e, nessa configuração, o menu pode exibir nomes como "configuracoes" sem acento.

Para definir nomes de menu personalizados, com acentos e letras maiúsculas, seria necessário utilizar uma configuração de navegação explícita com `st.navigation` e `st.Page` no `app.py`. Essa abordagem não foi adotada nesta etapa para manter a implementação simples e compatível com a estrutura atual.

### Formulário de Nova Auditoria

O formulário usa `st.form`, organizado nas seções Identificação, Período avaliado e Contexto da avaliação. A validação ocorre ao clicar em "Enviar dados": o nome da avaliação é obrigatório (um nome só com espaços é considerado vazio); as duas datas são obrigatórias, regra introduzida pela AR13 (na AR11 eram opcionais), cada uma com mensagem própria; a data inicial não pode ser posterior à data final, sendo permitidas datas iguais. O objetivo, o escopo e a descrição do processo são opcionais. Os campos "Objetivo da avaliação", "Escopo da avaliação" e "Descrição do processo" têm orientações curtas e são guardados nas chaves `objetivo`, `escopo` e `descricao_processo`, respectivamente. Cada erro de validação tem uma mensagem específica.

Os dados são gravados em `st.session_state["nova_auditoria"]` somente depois que todas as validações passam (na AR17, o formulário cria um objeto `Avaliacao` e grava o resultado de `para_dicionario()`: as mesmas chaves de antes, mais `controles_selecionados`, hoje sempre uma lista vazia); um envio inválido não altera dados já gravados. Após um envio válido, a página mostra a confirmação, um aviso de que os dados ficam apenas na sessão atual e não são salvos permanentemente, e um resumo dos dados. Os valores do resumo são exibidos com `st.text`, para que símbolos de formatação digitados pelo usuário não sejam interpretados como markdown. Não há persistência definitiva.

Ao clicar em "← Voltar ao início", os dados da avaliação atual são descartados: `st.session_state["nova_auditoria"]` é removido e o formulário volta vazio na próxima visita. Para limpar os campos, o nome do formulário e das chaves (`key`) dos campos inclui um número de versão, guardado em `st.session_state["nova_auditoria_versao"]`, que aumenta a cada descarte; na visita seguinte o Streamlit cria campos novos, com valores vazios. Essa estratégia foi escolhida no lugar de apagar o valor dos campos existentes, por não depender de onde o Streamlit guarda esse valor (servidor ou navegador) nem escrever em estado de widgets já criados. O descarte vale somente para o botão "Voltar ao início": sair pelo menu lateral, pelo botão voltar do navegador ou pelo botão "Nova Auditoria" da Home não limpa os dados.

### Modelo de dados da avaliação (AR17)

A classe `Avaliacao` (`models/avaliacao.py`) é um `dataclass` imutável (`frozen=True`) da biblioteca padrão do Python, sem novas dependências. Ela usa os mesmos nomes de campos que o formulário já guardava em `st.session_state["nova_auditoria"]`, para manter a compatibilidade:

- Obrigatórios: `nome_avaliacao` (texto não vazio; só espaços conta como vazio), `processo` (texto não vazio), `data_inicial` e `data_final` (tipo `date`, não `datetime`; a inicial não pode ser posterior à final e datas iguais são permitidas). São as mesmas regras do formulário.
- Opcionais, com valor padrão vazio: `objetivo`, `escopo` e `descricao_processo` (textos) e `controles_selecionados`.
- `controles_selecionados` é uma tupla de textos (identificadores de controles). Como ainda não existem biblioteca de controles nem seleção na interface, o modelo apenas reserva o espaço e valida que cada item é um texto não vazio. O tipo poderá ser revisto quando a biblioteca existir.
- O modelo valida os dados ao ser criado (`ValueError`). O formulário continua mostrando suas mensagens específicas e só cria o objeto depois de passar pelas validações; a validação do modelo é uma segunda barreira. Os textos opcionais não são alterados (nem têm espaços removidos), para que o dicionário gravado continue igual ao de antes.
- `para_dicionario()` gera o dicionário no formato do formulário, mais `controles_selecionados` (lista); `de_dicionario()` faz o caminho inverso e aceita o dicionário antigo, sem essa chave.
- O restante do código ainda lê o dicionário em `st.session_state`; migrar a página para usar o objeto diretamente não foi necessário nesta tarefa.

### Lista de processos

Nesta etapa, o único processo disponível (Gestão de Mudanças) é uma constante simples dentro de `pages/1_nova_auditoria.py`, e a `Avaliacao` guarda o processo como texto. Não foi criado um modelo de domínio próprio para processos em `models/`, porque ainda não há atributos ou regras definidos que justifiquem isso. A decisão deve ser revista quando a biblioteca de controles precisar associar controles a processos.

### Ambiente

O desenvolvimento utiliza um ambiente virtual Python (`.venv`), mantido fora do versionamento por meio do `.gitignore`.

---

## 9. Problemas conhecidos

Nenhum problema conhecido registrado no momento.

---

## 10. Última atualização

Data: 28/10/2026

**Último commit no repositório:**

`7528282 feat: orientar preenchimento da descrição do processo` (enviado ao GitHub; `origin/master` em `7528282`). As alterações da AR17 descritas abaixo ainda não estão commitadas.

A Tarefa 01 (navegação e estrutura inicial da Nova Auditoria) foi implementada, commitada e enviada ao repositório remoto.

A Tarefa 02 (completar o formulário de Nova Auditoria) foi implementada, commitada e enviada ao repositório remoto.

A tarefa AR-07 (navegação principal) foi implementada, commitada e enviada ao repositório remoto.

A tarefa AR-08 (Home da aplicação) foi implementada, validada localmente, commitada e enviada ao repositório remoto.

A tarefa AR-09 (primeiro deploy no Streamlit Community Cloud) foi executada com sucesso. A aplicação foi publicada em uma URL pública e todas as páginas existentes foram validadas sem erros.

URL pública da aplicação:

`https://audit-readiness-ai-xvskt2cm2b6exsv2v6vbjx.streamlit.app/`

A tarefa AR11 (formulário de nova avaliação com validação, resumo e descarte dos dados ao voltar ao início) foi implementada, testada manualmente pela desenvolvedora, commitada (`548fbc7`) e enviada ao repositório remoto. O commit no GitHub não confirma que o deploy publicado foi atualizado; ainda não há registro de que a aplicação publicada contenha a AR11.

A tarefa AR13 (datas obrigatórias) foi implementada e commitada (`e05efc7`).

A tarefa AR14 (campo "Objetivo da avaliação" e restauração do aviso de sessão e do subtítulo do resumo, removidos sem intenção pelo commit `e05efc7`) foi implementada em `pages/1_nova_auditoria.py`, verificada com simulação da interface (AppTest), validada manualmente no navegador pela desenvolvedora em 28/10/2026 (funcionou), commitada (`e31d9cb`) e enviada ao GitHub.

A AR15 (campo opcional "Escopo da avaliação", com orientação, chave `escopo` e inclusão no resumo) foi implementada em `pages/1_nova_auditoria.py`, verificada com simulação da interface (AppTest), validada manualmente no navegador pela desenvolvedora em 28/10/2026 (funcionou) commitada (`1edd2a5`) e enviada ao GitHub.

A AR16 (orientação do campo "Descrição do processo", mantendo a chave `descricao_processo`, o campo opcional e o resumo) foi implementada em `pages/1_nova_auditoria.py`, verificada com simulação da interface (AppTest, 22 verificações) e com a subida do servidor, validada manualmente no navegador pela desenvolvedora em 28/10/2026 (funcionou), commitada (`7528282`) e enviada ao GitHub.

A AR17 (modelo de dados `Avaliacao`) foi implementada em 28/10/2026: criados `models/avaliacao.py` e `test_cases/test_avaliacao.py`; modificado `pages/1_nova_auditoria.py` (apenas o import e a gravação dos dados no envio válido). Verificações realizadas: `py_compile` dos arquivos `.py`; 18 testes `unittest` (`python -m unittest test_cases.test_avaliacao -v`), todos aprovados; simulação da interface com AppTest (as mesmas 22 verificações da AR16, com a verificação das chaves do dicionário atualizada para incluir `controles_selecionados`), 22 de 22 aprovadas, e fluxo Home, Nova Auditoria, envio, "Voltar ao início" e reabertura; subida do servidor Streamlit com resposta de saúde HTTP 200 e um envio válido em navegador automatizado (Playwright), confirmando que o import `models.avaliacao` funciona na página. Essas verificações foram feitas no ambiente de desenvolvimento do Claude (não em `pytest`, que não é usado). **Ainda não foi validada manualmente no navegador pela desenvolvedora nem commitada.**

---

## 11. Regras para desenvolvimento

Este arquivo representa o estado atual conhecido do projeto.

Alterações relevantes na arquitetura, tecnologias, funcionalidades ou decisões técnicas devem ser registradas aqui.

O código deve permanecer versionado no Git.

Após alterações relevantes, o contexto do projeto deve ser atualizado para manter o projeto compreensível para qualquer pessoa ou ferramenta que venha a trabalhar nele.
