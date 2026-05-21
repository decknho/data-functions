def info_tratar_nulos():

    print("""
        Estratégias disponíveis:

        - remover_linhas
        - remover_coluna
        - media
        - mediana
        - moda

        Exemplo:

        tratar_nulos(df=nome_do_dataframe, coluna='nome_da_coluna', estrategia='media') """)
    

def info_converter_dados():

    print("""
        Estratégias disponíveis para conversão de dados:

        - int64
            Converte valores inteiros.
            Exemplo: 1, 2, 3

        - float64
            Converte valores decimais.
            Exemplo: 10.5, 7.8

        - string
            Converte valores para texto.

        - bool
            Converte valores booleanos.
            Exemplo: True ou False

        - datetime
            Converte valores para data.
            Exemplo: 2025-01-01

        - category
            Converte valores categóricos para otimizar memória.
            Muito útil para colunas com poucos valores únicos.

        Exemplo de uso:

        novo_df = converter_dados(df=nome_do_dataframe, coluna='nome_da_coluna', estrategia='datetime') """)
    

