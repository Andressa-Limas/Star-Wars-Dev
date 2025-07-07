# 🌌 Star Wars Dev – Documentação de Acesso

Bem-vindo(a)! Aqui você encontrará todas as instruções para acessar o front-end e as rotas da API do projeto **Star Wars Dev**.

---

## 🔁 API REST – Back-end em Python

A API está pública e pode ser acessada por qualquer ferramenta de requisição HTTP (como Postman, Insomnia ou diretamente no navegador para `GET`).
> **URL base da API:**  
🔗 [https://apidocs/](https://star-wars-dev-663524319048.us-central1.run.app/apidocs/)

## 🌐 Aplicação Front-end

Espere a API do back carregar completamente e mostrar os endpoints e após isso rode a API do front. A interface está disponível no seguinte endereço:

🔗 [https://filmes](https://hallowed-pipe-465219-u2.web.app/filmes)

Essa aplicação consome a API desenvolvida em Python e exibe os dados em tempo real.

---

# 🚀 Projeto Fullstack – Python (Back-end) + React (Front-end)

Este projeto é dividido em duas partes:

- **Back-end**: Python
- **Front-end**: React

---

## 📁 Estrutura de pastas

```

.
├── back               # Código do back-end (Python)
├── front              # Código do front-end (React)
├── .gitignore
├── README.md

````

---

## 📥 1. Clonar o repositório

```bash
git clone https://github.com/Andressa-Limas/Star-Wars-Dev
cd Star-Wars-Dev
````
---

## ⚙️ 2. Rodar o Back-end (Python)

### a) Acessar a pasta `back`

```bash
cd back
```

### b) Criar e ativar um ambiente virtual (recomendado)

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (CMD):**

```cmd
python -m venv venv
venv\Scripts\activate
```

### c) Instalar as dependências

```bash
pip install -r ../requirements.txt
```

### d) Iniciar o servidor

```bash
python app.py
```
---
## 🧪 Rodar os testes (Python)

Certifique-se de estar com o ambiente virtual ativado e dentro da pasta `back`.

### 📌 Comando para rodar o arquivo específico de teste,`test_app.py`:

```bash
python test_app.py
```
---
## 💻 3. Rodar o Front-end (React)

### a) Em outro terminal, acessar a pasta `front`

```bash
cd front
```

### b) Instalar as dependências

```bash
npm install
```

### c) Iniciar o servidor de desenvolvimento

```bash
npm start
```

> Isso abrirá automaticamente o navegador em `http://localhost:5000`.

---

## ✅ Tudo pronto!

* O front estará disponível em `http://localhost:5000`
* O back estará rodando localmente e pronto para receber requisições

---

💻 Feito por Andressa Lima

