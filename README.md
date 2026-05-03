# 🧮 Flask API Calculadora

Uma API REST leve construída com Flask para avaliação segura de expressões matemáticas. Utiliza a árvore sintática abstrata (AST) do Python para processar expressões sem o uso de `eval()`, evitando riscos de injeção de código.

## 🚀 Deploy

A aplicação está configurada para deploy com **Gunicorn** via `Procfile`, compatível com plataformas como Heroku e Railway.

## 🛠️ Stack

- **Python** + **Flask**
- **Gunicorn** (servidor de produção)
- **flask-cors** (suporte a CORS)

## 📦 Instalação local

```bash
# Clone o repositório
git clone https://github.com/zTheo47/flask-api-calculadora.git
cd flask-api-calculadora

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py
```

A API estará disponível em `http://localhost:5000`.

## 📡 Endpoints

### `GET /ping`

Verifica se a API está online.

**Resposta:**
```json
{
  "message": "API online"
}
```

---

### `POST /calculate`

Avalia uma expressão matemática e retorna o resultado.

**Body (JSON):**
```json
{
  "expression": "2 + 3 * 4",
  "x": 0
}
```

| Campo        | Tipo   | Obrigatório | Descrição                                              |
|--------------|--------|-------------|--------------------------------------------------------|
| `expression` | string | ✅           | Expressão matemática a ser avaliada                    |
| `x`          | number | ❌           | Valor da variável `x` na expressão (padrão: `0`)       |

**Resposta:**
```json
{
  "result": 14
}
```

**Operadores suportados:**

| Operador | Descrição      |
|----------|----------------|
| `+`      | Adição         |
| `-`      | Subtração      |
| `*`      | Multiplicação  |
| `/`      | Divisão        |
| `**`     | Potenciação    |

**Exemplo com variável `x`:**
```json
{
  "expression": "x * 2 + 1",
  "x": 5
}
```
```json
{
  "result": 11
}
```

## 🔒 Segurança

A avaliação de expressões utiliza o módulo `ast` do Python, percorrendo a árvore sintática e permitindo apenas operações binárias e constantes numéricas. Qualquer expressão inválida ou que contenha operações não suportadas retorna um erro.

## 📁 Estrutura

```
flask-api-calculadora/
├── app.py            # Aplicação principal
├── requirements.txt  # Dependências
├── Procfile          # Configuração de deploy (Gunicorn)
└── .gitignore
```

## 📋 Dependências

```
flask
flask-cors
gunicorn
```
