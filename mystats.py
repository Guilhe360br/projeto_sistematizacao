import math

def media(dados):
    return sum(dados) / len(dados)

def mediana(dados):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    meio = n // 2

    if n % 2 == 0:
        return (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2
    else:
        return dados_ordenados[meio]

def moda(dados):    
    contagem = {}
    for numero in dados:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    modas = max(contagem, key=contagem.get)        
    return modas

def amplitude(dados):
    return max(dados) - min(dados)

def desvios(dados):
    media_dados = media(dados)
    return [x - media_dados for x in dados]

def  variancia(dados, amostral = True):
    desvios_quadrados = [(x - media(dados)) ** 2 for x in dados]
    divisor = len(dados) - 1 if amostral else len(dados)
    return sum(desvios_quadrados) / divisor

def desvio_padrao(dados):
    return  math.sqrt(variancia(dados)) 

def percentil(dados, k):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    posicao = (k / 100) * (n - 1)
    if posicao == int(posicao):
        return dados_ordenados[int(posicao)]
    else:
        indice_inferior = dados_ordenados[int(posicao)]
        indice_superior = dados_ordenados[int(posicao) + 1]
        fracao = posicao - int(posicao)
        return indice_inferior + fracao * (indice_superior - indice_inferior)

def quartil(dados):
    Q1 = percentil(dados, 25)
    Q2 = percentil(dados, 50)
    Q3 = percentil(dados, 75)
    return Q1, Q2, Q3

def coef_var(dados):
    return (desvio_padrao(dados) / media(dados)) * 100

def covariancia(dados_x, dados_y, amostral = True):
    media_x = media(dados_x)
    media_y = media(dados_y)
    return sum((x - media_x) * (y - media_y) for x, y in zip(dados_x, dados_y)) / (len(dados_x) - 1 if amostral else len(dados_x))

def correlacao(dados_x, dados_y):
    cov = covariancia(dados_x, dados_y)
    desvio_x = desvio_padrao(dados_x)
    desvio_y = desvio_padrao(dados_y)
    return cov / (desvio_x * desvio_y)

def regressao_linear(x, y):
    x_media = media(x)
    y_media =  media(y)
    b1 = sum((x - x_media) * (y - y_media)) / sum((x - x_media)**2)
    b0 = y_media - b1 * x_media
    return b0, b1

def r_quadrado(x, y, b0, b1):
    y_pred = b0 + b1 * x
    ss_res = sum((y - y_pred)**2)
    ss_tot = sum((y - media(y))**2)
    return 1 - (ss_res / ss_tot)