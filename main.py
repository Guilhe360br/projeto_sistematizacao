import numpy as np
import pandas as pd
import streamlit as st
import math
import matplotlib.pyplot as plt
from mystats import media, mediana, moda, variancia, desvio_padrao, desvios, amplitude, percentil, quartil, coef_var, covariancia, correlacao

df_campanha = pd.read_csv("E-Commerce Sales Analytics.csv", sep = ",")

@st.cache_data
def gerar_amostra(dados, n):
    return dados.sample(n=n, replace=False)

st.title("Módulo 2 — Estatística Descritiva Interativa")
#AREA DOS FILTROS 
st.sidebar.header("Filtros")
opcao = st.sidebar.selectbox(" Escolha a variável para análise:",["Categoria do Produto", "Região", "Preço Unitario", "Desconto", "Avaliação do Cliente", "Receita", "Tempo de entrega"])
qtd_amostra = st.sidebar.select_slider("Quantidade da Amostra", range(1, len(df_campanha[opcao])), value= 500)
df_amostra = gerar_amostra(df_campanha[opcao], n = qtd_amostra)



# APRESENTACAO DO GRAFICOS
if df_amostra.dtype == 'str':
    st.bar_chart(df_amostra.value_counts())
    st.write("Moda: ", moda(df_amostra))
else:
    # MEDIDAS DE TENDÊNCIA CENTRAL
    st.write("MEDIDAS DE TENDÊNCIA CENTRAL")
    fig1, ax1 = plt.subplots()
    ax1.set_title(f'Histograma de {opcao}')
    ax1.set_xlabel(opcao)
    ax1.set_ylabel('Frequência')
    ax1.hist(df_amostra, color='skyblue', edgecolor='black')
    ax1.axvline(media(df_amostra), color='red', linestyle='dashed', linewidth=1, label=f'Média: {media(df_amostra):.2f}')
    ax1.axvline(mediana(df_amostra), color='green', linestyle='dashed', linewidth=1, label=f'Mediana: {mediana(df_amostra):.2f}')
    ax1.axvline(moda(df_amostra), color='orange', linestyle='dashed', linewidth=1, label=f'Moda: {moda(df_amostra):.2f}')
    ax1.legend()
    st.pyplot(fig1)

    st.write("MEDIDAS DE DISPERSÃO")
    fig2, ax2 = plt.subplots()
    ax2.set_title(f'Dispersão de {opcao}')
    ax2.set_ylabel(opcao)
    ax2.set_xlabel('Quantidade')
    ax2.scatter(range(len(df_amostra)),df_amostra, color='red', alpha=0.5)
    ax2.axhline(media(df_amostra), color='blue', linestyle='dashed', linewidth=1, label=f'Média: {media(df_amostra):.2f}')
    ax2.axhspan(media(df_amostra) - desvio_padrao(df_amostra), media(df_amostra) + desvio_padrao(df_amostra), color='green', alpha=0.2, label=f'Média ± Desvio Padrão: {desvio_padrao(df_amostra):.2f}')
    ax2.legend()
    st.write(f"Amplitude: {amplitude(df_amostra):.2f}  |  ", f"Variância: {variancia(df_amostra):.2f}  |  ", f"Desvio Padrão: {desvio_padrao(df_amostra):.2f}  |  ", f"Coeficiente de Variacao: {coef_var(df_amostra):.2f}  |  ")
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    q1, q2, q3 = quartil(df_amostra)
    ax3.boxplot(df_amostra, vert=False)
    ax3.set_xlabel(opcao)
    ax3.set_title('Boxplot com Quartis')
    ax3.legend()
    st.pyplot(fig3)
    st.write(f"Quartis: Q1 = {q1:.2f}, Q2 = {q2:.2f}, Q3 = {q3:.2f}, IQR = {q3 - q1:.2f}")
    

#filtros para Lei de Grandes Numeros
st.title("Módulo 3 — Probabilidade e Simulação ")
st.header("LEI DOS GRANDES NUMEROS")
prob_sim = st.selectbox("Selecione a Variavel", ["Preço Unitario", "Desconto", "Avaliação do Cliente", "Receita", "Tempo de entrega"])


#VARIAVEIS PARA O GRAFICO LGN
tam_amostra = st.select_slider("Tamanho da Amostra: ", range(0, 5001, 50))
amostras = gerar_amostra(df_campanha[prob_sim], n = tam_amostra)
media_acumulada = np.cumsum(amostras) / np.arange(1, tam_amostra + 1)


#GRAFICO DA LEI DE GRANDE NUMEROS
fig4, ax4 = plt.subplots()
ax4.plot(range(tam_amostra), media_acumulada, label="Média acumulada")
ax4.axhline(media(df_campanha[prob_sim]), color='red', linestyle='--', label="Valor esperado")
ax4.legend()
st.pyplot(fig4)

#VARIAVEIS PARA O GRAFICO TEOREMA CENTRAL DO LIMITE
st.header("TEORIA CENTRAL DO LIMITE")
n_repet = st.select_slider("nº de repetições", range(0, 500, 5))

#USANDO O FOR PARA CALCULAR E ARMARZENAR AS MEDIAS DAS AMOSTRAS
medias_tcl = []
for i in range(n_repet):
    amostra_tcl = df_campanha[prob_sim].sample(n = 100)
    medias_tcl.append(media(amostra_tcl))

#GRAFICO DA TEORIA CENTRAL DO LIMITE
fig5, ax5 = plt.subplots()

ax5.hist(medias_tcl, bins=20, edgecolor = "black")
ax5.axvline(media(df_campanha[prob_sim]) , color='red', linestyle='dashed', linewidth=1, label=f'Média: {media(df_campanha[prob_sim]):.2f}')
ax5.legend()
st.pyplot(fig5)



