import numpy as np
import test_mystats
from mystats import media, mediana, moda, variancia, desvio_padrao, desvios, amplitude, percentil, quartil, coef_var, covariancia, correlacao, regressao_linear, r_quadrado



dados = [10, 20, 30, 40, 50]
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 8, 10]


def test_media():
    resultado = media(dados)
    esperado = np.mean(dados)

    assert resultado == esperado


def test_mediana():
    resultado = mediana(dados)
    esperado = np.median(dados)

    assert resultado == esperado


def test_moda():
    dados_moda = [1, 2, 2, 3, 4, 2, 5]

    resultado = moda(dados_moda)
    esperado = 2

    assert resultado == esperado


def test_amplitude():
    resultado = amplitude(dados)
    esperado = np.ptp(dados)

    assert resultado == esperado


def test_desvios():
    resultado = desvios(dados)
    esperado = (np.array(dados) - np.mean(dados)).tolist()

    assert resultado == esperado


def test_variancia_amostral():
    resultado = variancia(dados, amostral=True)
    esperado = np.var(dados, ddof=1)

    assert resultado == esperado


def test_variancia_populacional():
    resultado = variancia(dados, amostral=False)
    esperado = np.var(dados, ddof=0)

    assert resultado == esperado


def test_desvio_padrao():
    resultado = desvio_padrao(dados)
    esperado = np.std(dados, ddof=1)

    assert resultado == esperado


def test_percentil():
    resultado = percentil(dados, 25)
    esperado = np.percentile(dados, 25)

    assert resultado == esperado


def test_coef_var():
    resultado = coef_var(dados)

    esperado = (
        np.std(dados, ddof=1) /
        np.mean(dados)
    ) * 100

    assert resultado == esperado


def test_covariancia():
    resultado = covariancia(x, y)
    esperado = np.cov(x, y, ddof=1)[0, 1]

    assert resultado == esperado


def test_correlacao():
    resultado = correlacao(x, y)
    esperado = np.corrcoef(x, y)[0, 1]

    assert np.isclose(resultado, esperado, rtol=1e-9, atol=1e-9)
