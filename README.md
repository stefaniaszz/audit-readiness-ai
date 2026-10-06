# 🔎 Audit Readiness AI

Aplicação web para apoiar a preparação para auditorias de tecnologia.

## 🎯 Objetivo

O **Audit Readiness AI** tem como objetivo auxiliar na preparação para auditorias, permitindo identificar antecipadamente possíveis lacunas, necessidades de evidências e pontos de atenção relacionados aos processos avaliados.

A proposta é ajudar a organização a identificar pontos que podem gerar questionamentos durante uma auditoria antes da realização da avaliação formal.

## 📌 Problema

Durante uma auditoria, podem existir diferenças entre o processo que a organização afirma executar, o que está documentado, os controles definidos, a execução real e as evidências disponíveis.

O projeto busca apoiar a identificação dessas possíveis diferenças durante a preparação para a auditoria.

## 🛠️ Tecnologias

Atualmente, o projeto utiliza:

* **Python 3.13.5**
* **Streamlit 1.64.0**
* **Git**
* **GitHub**
* **Streamlit Community Cloud**

## ▶️ Execução local

### 1. Clonar o repositório

```bash
git clone https://github.com/stefaniaszz/audit-readiness-ai.git
cd audit-readiness-ai
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
streamlit run app.py
```

Após a execução, o Streamlit disponibilizará a aplicação localmente no navegador.

## 🌐 Aplicação publicada

A primeira versão do projeto está disponível no Streamlit Community Cloud:

**Audit Readiness AI:**
https://audit-readiness-ai-xvskt2cm2b6exsv2v6vbjx.streamlit.app/

## 🚧 Status do projeto

**Em desenvolvimento.**

O projeto está atualmente em sua fase inicial de desenvolvimento (**Sprint 1**).

As funcionalidades serão implementadas gradualmente conforme o desenvolvimento avançar.

Neste momento, a aplicação possui a estrutura inicial, navegação principal, formulário de Nova Auditoria e páginas provisórias para Resultado, Simulador Auditor e Configurações.

A integração com Inteligência Artificial ainda não foi implementada nesta etapa.

---

**Audit Readiness AI — Preparação para auditorias de tecnologia.**
