import pandas as pd

def carregar_csv(caminho, sep=';'):
    df = pd.read_csv(caminho, delimiter=sep)
    return df

