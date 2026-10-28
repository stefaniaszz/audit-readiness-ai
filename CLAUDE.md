# CLAUDE.md — Audit Readiness AI

Instruções para o Claude Code ao trabalhar neste repositório.

## Contexto

- Aplicação Streamlit (Python 3.13.5, Streamlit 1.64.0) de apoio à preparação para auditorias.
- Ponto de entrada: `app.py`. Páginas em `pages/`.
- Contexto detalhado e estado atual do projeto: `PROJECT_CONTEXT.md`.
- Idioma do projeto: português (código, interface, documentação e mensagens de commit).

## 1. Preservar o código existente

- Faça apenas as alterações necessárias para a tarefa solicitada.
- Não reescreva, renomeie, mova ou apague arquivos, funções ou trechos de código sem pedido explícito.
- Não refatore código que não faz parte da tarefa; se identificar melhorias, sugira-as em vez de aplicá-las.
- Mantenha o estilo, a nomenclatura e a organização já usados no projeto.
- Não altere dependências nem versões em `requirements.txt` sem autorização.
- Antes de sobrescrever ou excluir qualquer arquivo, leia o conteúdo atual e confirme comigo.
- Respeite alterações locais ainda não commitadas: não as descarte (`git checkout`, `git restore`, `git reset`, `git stash`) sem autorização.

## 2. Executar testes

Após qualquer alteração de código:

1. Verifique a sintaxe dos arquivos alterados:
   ```bash
   python -m py_compile app.py pages/*.py
   ```
2. Se existirem testes automatizados (por exemplo, com `pytest`), execute-os:
   ```bash
   python -m pytest
   ```
3. Quando a alteração afetar a interface, indique como validar manualmente:
   ```bash
   streamlit run app.py
   ```
- Use o ambiente virtual `.venv` do projeto.
- Relate os resultados com fidelidade: se algum teste falhar ou não puder ser executado, informe o motivo e a saída obtida.
- **Nunca afirme que testes passaram sem tê-los executado.** Informe quais comandos foram executados e o resultado de cada um. O que não foi executado deve ser declarado como não executado.
- Não declare uma tarefa concluída sem ter verificado o funcionamento.

## 3. Atualizar a documentação

**Obrigatório ao concluir cada AR:** revisar `PROJECT_CONTEXT.md` e `CHANGELOG.md` e atualizá-los quando aplicável.

- `PROJECT_CONTEXT.md` — estado atual do projeto, sprint e funcionalidades implementadas.
- `CHANGELOG.md` — nova entrada com data, descrição das alterações e hash do commit (o hash só é preenchido após o commit autorizado).
- `README.md` — revisar quando a AR alterar funcionalidades, instruções de execução ou tecnologias.

Se, após a revisão, algum desses arquivos não precisar de alteração, informe isso explicitamente e explique o motivo.

Registre apenas fatos confirmados (por exemplo, não afirme que o deploy foi atualizado sem confirmação).

Antes de declarar a documentação concluída, confirme as alterações executando:

```bash
git status
git diff
```

Verifique se apenas os arquivos esperados foram alterados e se o conteúdo do diff corresponde ao que foi descrito.

## 4. Commits e Git

- **Nunca faça commit sem minha autorização explícita.**
- **Nunca faça push** para o GitHub sem minha autorização explícita.
- Não crie branches, tags nem altere o histórico (rebase, amend, force push) sem autorização.
- Ao concluir uma tarefa, mostre um resumo das alterações e uma sugestão de mensagem de commit, e aguarde minha aprovação.
- Padrão de mensagens: Conventional Commits em português, por exemplo:
  - `feat: validar datas da nova auditoria`
  - `docs: atualizar documentação após AR11`
