# 🧮 Calculadora API com FastAPI

> Projeto avaliativo desenvolvido para a disciplina **Programação de Sistemas Distribuídos** da Universidade dos Grandes Lagos (UNILAGO), sob supervisão do Professor Gleydes Oliveira.

---

## 📋 Índice
- [Instalação](#-instalação)
- [Como Rodar](#-como-rodar)
- [Endpoints](#-endpoints)
- [Documentação](#-documentação)
- [Testes](#-testes)

---

## 💻 Instalação

### Pré-requisitos
- Python 3.8+
- pip ou conda

### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/Flavilis/calculadora-api.git
cd calculadora-api
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
   - **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   - **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Execute a aplicação:**
```bash
uvicorn main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`

---

## 🚀 Como Rodar

Após seguir os passos de instalação, a API estará pronta para uso. A aplicação executa em modo desenvolvimento com hot-reload habilitado.

---

## 📡 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Retorna uma mensagem de boas-vindas |
| `POST` | `/somar` | Realiza a soma de dois números |
| `POST` | `/subtrair` | Realiza a subtração de dois números |
| `POST` | `/multiplicar` | Realiza a multiplicação de dois números |
| `POST` | `/dividir` | Realiza a divisão com tratamento para divisão por zero |
| `POST` | `/raiz` | Calcula a raiz n-ésima de um número |
| `POST` | `/potencia` | Calcula a potência de um número |
| `GET` | `/calcular` | Recebe parâmetros pela URL e executa a operação |

### Exemplo de Requisição

```bash
# Somar
curl -X POST "http://127.0.0.1:8000/somar" \
  -H "Content-Type: application/json" \
  -d '{"numero1": 10, "numero2": 5}'

# Usar endpoint genérico
http://127.0.0.1:8000/calcular?numero1=10&numero2=5&operacao=soma
```

---

## 📚 Documentação

O FastAPI gera automaticamente documentação interativa para os endpoints:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **Redoc:** http://127.0.0.1:8000/redoc

Acesse uma dessas URLs após iniciar a aplicação para explorar todos os endpoints interativamente.

---

## ✅ Testes

Todas as operações foram testadas utilizando o **Insomnia**. As requisições retornam respostas em formato JSON com status `200 OK` quando executadas corretamente.

### Status de Teste
- ✓ Operações básicas (somar, subtrair, multiplicar)
- ✓ Divisão com tratamento de erro (divisão por zero)
- ✓ Operações avançadas (raiz, potência)
- ✓ Endpoint genérico `/calcular`

> 📹 Um vídeo demonstrativo dos testes está disponível [aqui](#).

---

## 🛠️ Tecnologias

- **FastAPI** - Framework web moderno
- **Python** - Linguagem de programação
- **Uvicorn** - Servidor ASGI
- **Insomnia** - Testes de API

---

## 📝 Licença

Este projeto é fornecido como atividade avaliativa para a disciplina de Programação de Sistemas Distribuídos.
