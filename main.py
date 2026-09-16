import numpy as np
import pandas as pd
import streamlit as st
import math
import matplotlib.pyplot as plt
from mystats import media, mediana, moda, variancia, desvio_padrao, desvios, amplitude, percentil, quartil, coef_var, covariancia, correlacao

df_campanha = pd.read_csv("E-Commerce Sales Analytics.csv", sep = ",")



opcao = st.selectbox(" Escolha a variável para análise:",["Categoria do Produto", "Região", "Preço Unitario", "Desconto", "Quantidade", "Receita", "Tempo de entrega"])
df_amostra = df_campanha[opcao].sample(n=500, random_state=42)
if df_amostra.dtype == 'str':
    st.bar_chart(df_amostra.value_counts())
    st.write("Moda: ", moda(df_amostra))
else:
    # MEDIDAS DE TENDÊNCIA CENTRAL
    st.write("MEDIDAS DE TENDÊNCIA CENTRAL")
    fig1, ax1 = plt.subplots()
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
    ax2.scatter(range(len(df_amostra)), df_amostra, color='red', alpha=0.5)
    ax2.axhline(media(df_amostra), color='blue', linestyle='dashed', linewidth=1, label=f'Média: {media(df_amostra):.2f}')
    ax2.axhspan(media(df_amostra) - desvio_padrao(df_amostra), media(df_amostra) + desvio_padrao(df_amostra), color='yellow', alpha=0.2, label=f'Média ± Desvio Padrão: {desvio_padrao(df_amostra):.2f}')
    ax2.legend()
    st.pyplot(fig2)
    
    
