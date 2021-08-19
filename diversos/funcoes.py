distancia = 100
tempo = 20

def velocidade_media(distancia, tempo):
    velocidade = divisao(distancia, tempo)
    return velocidade

def soma(x, y):
    resultado = x + y
    return resultado

def subtracao(x, y):
    resultado = x - y
    return resultado

def multiplicacao(x, y):
    resultado = x*y
    return resultado

def divisao(x, y):
    resultado = x/y
    return resultado

def calculadora(x, y):
    resultados = soma(x, y), subtracao(x, y), multiplicacao(x, y), divisao(x, y)
    return resultados
