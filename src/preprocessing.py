import pandas as pd
from utils import *


def tratar_nulos(df, coluna, funcao):
    if funcao == 1:
        return apagar_linhas(df=df, coluna=coluna)
    elif funcao == 2:
        return apagar_coluna(df=df, coluna=coluna)
    elif funcao == 3:
        return preencher_media(df=df, coluna=coluna)
    elif funcao == 4:
        return preencher_mediana(df=df, coluna=coluna)
    elif funcao == 5:
        return preencher_moda(df=df, coluna=coluna)


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