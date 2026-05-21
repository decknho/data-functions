import pandas as pd
from utils import carregar_csv
caminho = '../data/raw/telecon.csv'
df = carregar_csv(caminho)

df.head()
def tratar_nulos():
    return