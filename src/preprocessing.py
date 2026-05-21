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


def converter_dados(df, coluna, estrategia):
    try:

        if estrategia == 'int64':
            df[coluna] = df[coluna].astype('int64')

        elif estrategia == 'float64':
            df[coluna] = df[coluna].astype('float64')

        elif estrategia == 'string':
            df[coluna] = df[coluna].astype('string')

        elif estrategia == 'bool':
            df[coluna] = df[coluna].astype('bool')

        elif estrategia == 'datetime':
            df[coluna] = pd.to_datetime(df[coluna])

        elif estrategia == 'category':
            df[coluna] = df[coluna].astype('category')

        else:
            print('Estratégia inválida.')

    except Exception as erro:
        print(f'Erro ao converter a coluna "{coluna}": {erro}')

    return df


def mapear_coluna(df, coluna, mapeamento):
    df[coluna] = df[coluna].map(mapeamento)
    return df
     