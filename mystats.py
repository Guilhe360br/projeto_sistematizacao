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
        