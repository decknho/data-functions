import pandas as pd

def carregar_csv(caminho, sep=';'):
    df = pd.read_csv(caminho)
    return df


caminho = '../data/raw/telecon.csv'
df = carregar_csv(caminho)


df.head()