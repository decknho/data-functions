import pandas as pd
from utils import *


def tratar_nulos(df, coluna, estrategia):

    if estrategia == 'remover_linhas':
        return apagar_linhas(df, coluna)

    elif estrategia == 'remover_coluna':
        return apagar_coluna(df, coluna)

    elif estrategia == 'media':
        return preencher_media(df, coluna)

    elif estrategia == 'mediana':
        return preencher_mediana(df, coluna)

    elif estrategia == 'moda':
        return preencher_moda(df, coluna)

    else:
        raise ValueError('Estratégia inválida.')


def apagar_linhas(df, coluna):
    return df.dropna(subset=[coluna], inplace=True)


def apagar_coluna(df, coluna):
    return df.drop(columns=[coluna], inplace=True)


def preencher_media(df, coluna):
    df[coluna] = df[coluna].fillna(df[coluna].mean())
    return df


def preencher_mediana(df, coluna):
    df[coluna] = df[coluna].fillna(df[coluna].median())
    return df


def preencher_moda(df, coluna):
    df[coluna] = df[coluna].fillna(df[coluna].mode()[0])
    return df