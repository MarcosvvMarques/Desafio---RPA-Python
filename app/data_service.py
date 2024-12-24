# data_service.py
import pandas as pd

def contar_citacoes(citacoes):
    series = pd.Series(citacoes)
    return series.count()


def obter_autor_mais_recorrente(citacoes):
    autores = [citacao['autor'] for citacao in citacoes]
    series = pd.Series(autores)
    autor_mais_recorrente = series.value_counts().idxmax()
    return autor_mais_recorrente


def obter_tag_mais_recorrente(citacoes):
    tags = [citacao['tags'].split(';') for citacao in citacoes]
    series = pd.Series(tags).explode()
    tag_mais_recorrente = series.value_counts().idxmax()
    return tag_mais_recorrente



