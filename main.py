import numpy as np
import pandas as pd
import streamlit as st
import math
import matplotlib.pyplot as plt
from mystats import media, mediana, moda, variancia, desvio_padrao, desvios, amplitude, percentil, quartil, coef_var, covariancia, correlacao, regressao_linear, interpretar_assimetria

df_performance = pd.read_csv("IBM_HR_Attrition_Enhanced.csv", sep = ",")


def gerar_amostra(dados, n):
    return dados.sample(n=n, replace=False)

st.title("Módulo 2 — Estatística Descritiva Interativa")
#AREA DOS FILTROS 
st.header("Filtros")
opcao = st.selectbox(" Escolha a variável para análise:",["BusinessTravel","Department","Age","Salary","TotalWorkingYears", "YearsAtCompany", "JobLevel"])
qtd_amostra = st.select_slider("Quantidade da Amostra", range(1, len(df_performance[opcao])), value= 500)
df_amostra = gerar_amostra(df_performance[opcao], n = qtd_amostra)



# APRESENTACAO DOS GRAFICOS
if pd.api.types.is_numeric_dtype(df_amostra):
    # MEDIDAS DE TENDÊNCIA CENTRAL
    st.write("MEDIDAS DE TENDÊNCIA CENTRAL")
    fig1, ax1 = plt.subplots()
    ax1.set_title(f'Histograma de {opcao}')
    ax1.set_xlabel(opcao)
    ax1.set_ylabel('Frequência')
    ax1.hist(df_amostra, bins= 10, color='skyblue', edgecolor='black')
    ax1.axvline(media(df_amostra), color='red', linestyle='dashed', linewidth=1, label=f'Média: {media(df_amostra):.2f}')
    ax1.axvline(mediana(df_amostra), color='green', linestyle='dashed', linewidth=1, label=f'Mediana: {mediana(df_amostra):.2f}')
    ax1.axvline(moda(df_amostra), color='orange', linestyle='dashed', linewidth=1, label=f'Moda: {moda(df_amostra):.2f}')
    ax1.legend()
    st.pyplot(fig1)
    st.write(interpretar_assimetria(media(df_amostra), mediana(df_amostra), desvio_padrao(df_amostra)))

    st.write("MEDIDAS DE DISPERSÃO")
    fig2, ax2 = plt.subplots()
    ax2.set_title(f'Dispersão de {opcao}')
    ax2.set_ylabel(opcao)
    ax2.set_xlabel('Quantidade')
    ax2.scatter(range(len(df_amostra)),df_amostra, color='red', alpha=0.5)
    ax2.axhline(media(df_amostra), color='blue', linestyle='dashed', linewidth=1, label=f'Média: {media(df_amostra):.2f}')
    ax2.axhspan(media(df_amostra) - desvio_padrao(df_amostra), media(df_amostra) + desvio_padrao(df_amostra), color='green', alpha=0.2, label=f'Média ± Desvio Padrão: {desvio_padrao(df_amostra):.2f}')
    st.write(f"Amplitude: {amplitude(df_amostra):.2f}  |  ", f"Variância: {variancia(df_amostra):.2f}  |  ", f"Coeficiente de Variacao: {coef_var(df_amostra):.2f}  |  ")
    ax2.legend()
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    q1, q2, q3 = quartil(df_amostra)
    iqr = q3 - q1
    limite_superior = q3 + 1.5*iqr
    limite_inferior = q1 - 1.5*iqr
    outliers = df_amostra[(df_amostra < limite_inferior) | (df_amostra > limite_superior)]
    ax3.boxplot(df_amostra, vert=False)
    ax3.axvline(limite_superior, color='blue', linestyle='dashed',  label= "LIMITE SUPERIOR: Q3 + 1.5*IQR")
    ax3.plot([],[],' ',label=f' {len(outliers)} outliers (REGRA DE IQR)')
    ax3.set_title('Boxplot com Quartis')
    ax3.legend()
    st.pyplot(fig3)
    st.write(f"Quartis: Q1 = {q1:.2f}, Q2 = {q2:.2f}, Q3 = {q3:.2f}, IQR = {q3 - q1:.2f}")
else:
    st.bar_chart(df_amostra.value_counts())
    st.write("Moda: ", moda(df_amostra))
    

#filtros para Modulo 3
st.title("Módulo 3 — Probabilidade e Simulação ")
st.header("LEI DOS GRANDES NUMEROS")
prob_sim = st.selectbox("Selecione a Variavel", ["Age","Salary","TotalWorkingYears", "YearsAtCompany", "JobLevel"])


#VARIAVEIS PARA O GRAFICO LGN
tam_amostra = st.select_slider("Tamanho da Amostra: ", range(0, 1000), value= 500)
amostras = gerar_amostra(df_performance[prob_sim], n = tam_amostra)
media_acumulada = np.cumsum(amostras) / np.arange(1, tam_amostra + 1)


#GRAFICO DA LEI DE GRANDE NUMEROS
fig4, ax4 = plt.subplots()
ax4.plot(range(tam_amostra), media_acumulada, label="Média acumulada")
ax4.axhline(media(df_performance[prob_sim]), color='red', linestyle='--', label="Valor esperado")
ax4.set_xlabel("Tamanho da Amostra")
ax4.set_ylabel(f"Media {prob_sim}")
ax4.legend()
st.pyplot(fig4)

#VARIAVEIS PARA O GRAFICO TEOREMA CENTRAL DO LIMITE
st.header("TEORIA CENTRAL DO LIMITE")
n_repet = st.select_slider("nº de repetições", range(0, 500, 5), value=100)

#USANDO O FOR PARA CALCULAR E ARMARZENAR AS MEDIAS DAS AMOSTRAS
medias_tcl = []
for i in range(n_repet):
    amostra_tcl = df_performance[prob_sim].sample(n = 300)
    medias_tcl.append(media(amostra_tcl))

#GRAFICO DA TEORIA CENTRAL DO LIMITE
fig5, ax5 = plt.subplots()
ax5.hist(medias_tcl, bins=20, edgecolor = "black")
ax5.axvline(media(df_performance[prob_sim]) , color='red', linestyle='dashed', linewidth=1, label=f'Média: {media(df_performance[prob_sim]):.2f}')
ax5.legend()
st.pyplot(fig5)

#MODULO 4
st.title("Módulo 4 — Distribuições Teóricas")


#VARIAVEIS/CALCULOS PARA AS CURVAS DE DISTRIBUICAO NORMAL E EXPONENCIAL
variavel_escolhida = df_performance["YearsAtCompany"]
mu = media(variavel_escolhida)
sigma = desvio_padrao(variavel_escolhida)
lambda_ = 1 / mu
x = np.linspace(variavel_escolhida.min(), variavel_escolhida.max(), 1470)
y_normal = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
y_exponencial = lambda_ * np.exp(-lambda_ * x)

fig6, ax6 = plt.subplots()
ax6.set_title(f'Histograma de YearsAtCompany')
ax6.set_xlabel("YearsAtCompany")
ax6.set_ylabel('DENSIDADE')
ax6.hist(variavel_escolhida, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.7)
ax6.plot(x, y_normal, color='red', linewidth=2, label='Distribuição Normal')
ax6.plot(x, y_exponencial, color='green', linewidth=2, label='Distribuição Exponencial')
ax6.legend()
st.pyplot(fig6)

st.title("Módulo 5 — Correlação e Regressão Linear")
variavel1 = st.selectbox("Selecione a primeira variavel", ["Age","Salary","TotalWorkingYears", "YearsAtCompany", "JobLevel"])
variavel2 = st.selectbox("Selecione a segunda variavel", ["Age","Salary","TotalWorkingYears", "YearsAtCompany", "JobLevel"])


# CALCULOS PARA CORRELACAO, REGRESSAO LINEAR E R2

correlacao_ = correlacao(df_performance[variavel1], df_performance[variavel2])
b0, b1, r2 = regressao_linear(df_performance[variavel1], df_performance[variavel2])

#GRAFICO DE DISPERSAO ENTRE 2 VARIAVEIS
fig7, ax7 = plt.subplots()
ax7.scatter(df_performance[variavel1],df_performance[variavel2], label = "Dados")
ax7.plot(df_performance[variavel1], b0 + b1*df_performance[variavel1], color="red", label=f"Ŷ = {b0:.2f} + {b1:.2f}x    R²: {r2:.2f}")
ax7.set_xlabel(variavel1)
ax7.set_ylabel(variavel2)
ax7.legend()
st.pyplot(fig7)

correlacao_abs = abs(correlacao_)

if 0 <= correlacao_abs < 0.2:
    st.write(f"Correlação: {correlacao_:.2f}  |  Insignificante")
elif 0.2 <= correlacao_abs < 0.5:
    st.write(f"Correlação: {correlacao_:.2f}  |  Fraca")
elif 0.5 <= correlacao_abs < 0.8:
    st.write(f"Correlação: {correlacao_:.2f}  |  Moderada")
elif 0.8 <= correlacao_abs <= 1:
    st.write(f"Correlação: {correlacao_:.2f}  |  Forte")
else:
    st.write(f"Correlação: {correlacao_:.2f}  |  Fora do intervalo esperado")


#predição interativa
x_input = st.number_input("Digite um valor de X para prever Ŷ:")
if x_input:
    y_pred = b0 + b1 * x_input
    st.write(f"Predição: Para X={x_input}, Ŷ={y_pred:.4f}")