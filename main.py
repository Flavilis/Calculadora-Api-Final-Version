from fastapi import FastAPI, HTTPException, Request     # Classe principal, erros HTTP e Request para templates
from pydantic import BaseModel                          # Define modelos de dados e validação
from fastapi.responses import HTMLResponse              # Para retornar páginas HTML
from fastapi.staticfiles import StaticFiles             # Para servir arquivos estáticos (CSS, JS)
from fastapi.templating import Jinja2Templates          # Para renderizar templates HTML

# Criando a aplicação FastAPI -> framework Python para criar APIs RESTful.
app = FastAPI(
    title="Calculadora API",
    description="API de Calculadora para Sistemas Distribuidos",
    version="1.0.0"
)

# Configuração para servir frontend
app.mount("/static", StaticFiles(directory="static"), name="static")   # Pasta static/ para CSS e JS
templates = Jinja2Templates(directory="templates")                     # Pasta templates/ para HTML

# Rota raiz para abrir o frontend (index.html)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Classe que define os dados de entrada e seus tipos. O Pydantic valida se os dados são float.
class OperacaoRequest(BaseModel):
    numero1: float
    numero2: float

# Classe que define os dados de resposta. Garante que o JSON de saída tenha sempre esses campos.
class ResultadoResponse(BaseModel):
    operacao: str
    numero1: float
    numero2: float
    resultado: float

# Rota para realizar a soma
@app.post("/somar", response_model=ResultadoResponse)
def somar(dados: OperacaoRequest):
    resultado = dados.numero1 + dados.numero2
    return ResultadoResponse(operacao="soma", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

# Rota para realizar a subtração
@app.post("/subtrair", response_model=ResultadoResponse)
def subtrair(dados: OperacaoRequest):
    resultado = dados.numero1 - dados.numero2
    return ResultadoResponse(operacao="subtracao", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

# Rota para realizar a multiplicação
@app.post("/multiplicar", response_model=ResultadoResponse)
def multiplicar(dados: OperacaoRequest):
    resultado = dados.numero1 * dados.numero2
    return ResultadoResponse(operacao="multiplicacao", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

# Rota para realizar a divisão com tratamento de erro
@app.post("/dividir", response_model=ResultadoResponse)
def dividir(dados: OperacaoRequest):
    if dados.numero2 == 0:
        raise HTTPException(status_code=400, detail="Divisao por zero nao e permitida!")
    resultado = dados.numero1 / dados.numero2
    return ResultadoResponse(operacao="divisao", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

#EXERCICIO 1: IMPLEMENTAR OPERAÇÃO DE RAIZ E POTÊNCIA
@app.post("/raiz", response_model=ResultadoResponse)
def calcular_raiz(dados: OperacaoRequest):
    if dados.numero2 == 0:
        raise HTTPException(status_code=400, detail="Não é possível calcular raiz de ordem zero!")
    resultado = dados.numero1 ** (1 / dados.numero2)
    return ResultadoResponse(operacao="raiz", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

@app.post("/potencia", response_model=ResultadoResponse)
def calcular_potencia(dados: OperacaoRequest):
    resultado = dados.numero1 ** dados.numero2
    return ResultadoResponse(operacao="potencia", numero1=dados.numero1, numero2=dados.numero2, resultado=resultado)

# Rota alternativa usando Query Parameters (Passagem de dados via URL)
@app.get("/calcular")
def calcular_query(numero1: float, numero2: float, operacao: str):
    operacoes = {
        "soma": lambda a, b: a + b,
        "subtracao": lambda a, b: a - b,
        "multiplicacao": lambda a, b: a * b,
        "divisao": lambda a, b: a / b if b != 0 else None,
        "raiz": lambda a, b: a ** (1 / b) if b != 0 else None,
        "potencia": lambda a, b: a ** b,
    }

    if operacao not in operacoes:
        raise HTTPException(status_code=400, detail=f"Operacao invalida. Use: {list(operacoes.keys())}")

    resultado = operacoes[operacao](numero1, numero2)
    if resultado is None:
        raise HTTPException(status_code=400, detail="Erro na operação (ex: divisão ou raiz por zero).")

    return {"operacao": operacao, "numero1": numero1, "numero2": numero2, "resultado": resultado}