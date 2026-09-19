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

def interpretar_assimetria(media_valor, mediana_valor, desvio):
    diferenca = media_valor - mediana_valor

    if diferenca > 0.3 * desvio:
        return "Assimetria à direita"

    elif diferenca < -0.3 * desvio:
        return "Assimetria à esquerda"

    else:
        return "Aproximadamente simétrica"

def regressao_linear(x, y):
    """Minimos quadrados simples. Retorna (b0, b1, r2)."""
    mx, my = media(x), media(y)
    b1 = sum((xi-mx)*(yi-my) for xi, yi in zip(x, y)) / \
         sum((xi-mx)**2 for xi in x)
    b0 = my - b1*mx
    yhat = [b0 + b1*xi for xi in x]
    sq_res = sum((yi-yh)**2 for yi, yh in zip(y, yhat))
    sq_tot = sum((yi-my)**2 for yi in y)
    r2 = 1 - sq_res/sq_tot
    return b0, b1, r2

