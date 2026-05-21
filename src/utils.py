import pandas as pd

def configurar_pandas():
    return

def configurar_seaborn():
    return


def salvar_grafico(nome):
    return


def carregar_csv(caminho, sep=';'):
    df = pd.read_csv(caminho, delimiter=sep)
    return df


def mostrar_percentual_nulos(df):
    print('Serão mostrados apenas as porcetagens de colunas com dados faltantes:')
    print('_' * 80)

    total_nulos = df.isnull().sum().sum()

    if total_nulos == 0:
        print('Não existe nenhuma coluna com dados faltantes.')
        return

    for coluna in df.columns:

        porcentagem = (df[coluna].isnull().sum() / len(df)) * 100

        if porcentagem == 0:
            continue
        
        print(f'\n\033[1;32;40mColuna: {coluna} | Dados faltantes: {porcentagem:.2f}%\033[0;0m\n')
        
        if porcentagem <= 5:
            print('Pouco impacto. Pode remover linhas ou '
                  'preencher com média, mediana ou moda.')
            print('_' * 80)

        elif porcentagem <= 20:
            print('Dependendo do contexto, pode ser melhor '
                  'imputar ou considerar remover a coluna.')
            print('_' * 80)
        elif porcentagem <= 40:
            print('Remover linhas pode ser arriscado. '
                  'Considere imputações mais robustas:\n'
                  '  - média/mediana\n'
                  '  - KNN\n'
                  '  - regressão')
            print('_' * 80)
        else:
            print('A coluna possui muitos dados faltantes.\n'
                  'Considere remover a coluna.\n'
                  'Caso a variável seja booleana, dependendo do contexto, '
                  'os valores nulos podem representar False.')
            print('_' * 80)
            

def renomear_colunas(df):
    ...


def converter_datas(df, coluna):
    ...


def verificar_dataframe(df):
    return df.head()


def memoria_dataframe(df):
    ...


def separar_features_target(df, target):
    ...
