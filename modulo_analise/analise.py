''' Módulo de Análise
    --------------------------------
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#SEPARAR O DATAFRAME POR ESTADO
def separar_ufs(df: pd.DataFrame, ufs: list) -> pd.DataFrame:
    """
    Toma o DataFrame e o filtra por qualquer quantidade de estados

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame original
    
    ufs : list
        Lista com estados que queira separar do DataFrame original. Os estados devem ser
        escritos pela sigla UF.
    
    Returns
    -------
    pd.DataFrame
        DataFrame filtrado pelos estados escolhidos

    Raises
    ------
    ValueError
        Se a entrada fornecida não tiver estados válidos

    Exemplos
    --------
    >>> import pandas as pd
    >>> data = {'SG_UF_PROVA': ['SP', 'RJ', 'MG', 'SP', 'RJ'],
    ...         'Nota': [70, 80, 90, 85, 95]}
    >>> df = pd.DataFrame(data)
    >>> estados_para_filtrar = ['SP', 'MG']
    >>> separar_ufs(df, estados_para_filtrar)
      Cidade  Nota
    0     SP    70
    2     MG    90
    3     SP    85
    """
    ufs = [uf.upper() for uf in ufs]

    if 'SG_UF_PROVA' not in df.columns:
        raise ValueError("A coluna 'SG_UF_PROVA' deve estar presente no DataFrame.")
    if not set(ufs).issubset(df['SG_UF_PROVA']):
        raise ValueError("A entrada fornecida não contém estados válidos.")

    return df[df['SG_UF_PROVA'].isin(ufs)]

#SEPARAR O DATAFRAME POR REGIAO
def separar_regiao(df: pd.DataFrame, regiao: str) -> pd.DataFrame:
    """
    Toma o DataFrame e o filtra de acordo com a região escolhida

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame original
    
    regiao : str
        Uma das cinco regiões brasileiras
    
    Returns
    -------
    pd.DataFrame
        DataFrame filtrado pela região escolhida

    Raises
    ------
    ValueError
        Se a entrada fornecida não for uma região válida

    Exemplos
    --------
    >>> import pandas as pd
    >>> data = {'CO_UF_PROVA': ['AM', 'SP', 'BA', 'SC', 'GO', 'RS'],
    ...         'OutrosDados': [1, 2, 3, 4, 5, 6]}
    >>> df = pd.DataFrame(data)
    >>> separar_regiao(df, 'sudeste')
      CO_UF_PROVA  OutrosDados
    1          SP            2
    """
    
    regiao = regiao.lower()
    regioes = {"norte": ["AM", "RR", "AP", "PA", "TO", "RO", "AC"],
               "nordeste": ["MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA"],
               "centro_oeste": ["MT", "MS", "GO"],
               "sudeste": ["SP", "RJ", "ES", "MG"],
               "sul": ["PR", "SC", "RS"]}

    if "CO_UF_PROVA" not in df.columns:
        raise ValueError("A DataFrame fornecido não é tem a coluna 'CO_UF_PROVA'")
    if regiao not in regioes:
        raise ValueError("A entrada fornecida não é uma região válida")
    
    filt = df["CO_UF_PROVA"].isin(regioes[regiao])
    return df.loc[filt]


def media(df: pd.DataFrame) -> float:
    """
    Toma o DataFrame e tira a média dos participantes

    Parâmetros
    ----------
    df : pd.DataFrame
    
    Returns
    -------
    float
        Média das médias das colunas especificadas

    Raises
    ------
    ValueError
        Se o DataFrame não contiver todas as colunas necessárias

    Exemplo
    --------
    >>> import pandas as pd
    >>> data = {'NU_NOTA_CN': [70, 80, 90],
    ...         'NU_NOTA_CH': [75, 85, 95],
    ...         'NU_NOTA_LC': [72, 82, 92],
    ...         'NU_NOTA_MT': [68, 78, 88],
    ...         'NU_NOTA_REDACAO': [80, 85, 90]}
    >>> df = pd.DataFrame(data)
    >>> media(df)
    82.0
    """
    colunas_media = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]

    if not set(colunas_media).issubset(df.columns):
        raise ValueError("O DataFrame não contém todas as colunas necessárias para calcular a média.")
    
    df_media = df[colunas_media].mean().mean()
    return df_media



#NOTAS 1000 DOS ALUNOS 
def nota_1000_ano(df : pd.DataFrame, anos : list) -> pd.DataFrame:
    """
    Toma o DataFrame e retorna um DataFrame com os anos e a quantidade de notas 1000

    Parâmetros
    ----------
    df : pd.DataFrame
    
    ano : list
        Cada valor da lista deve ser um ano do qual você quer saber a nota 1000
    
    Returns
    -------
    pd.DataFrame
        As linhas do DataFrame são os anos escolhidos e a única coluna a quantidade de notas 1000 neste ano

    Raises
    ------
    ValueError
        Se as colunas 'NU_NOTA_REDACAO' e 'NU_ANO' não estiverem presentes no DataFrame.

    """
    if 'NU_NOTA_REDACAO' not in df.columns or 'NU_ANO' not in df.columns:
        raise ValueError("As colunas 'NU_NOTA_REDACAO' e 'NU_ANO' devem estar presentes no DataFrame.")
    
    resultados = []

    for ano in anos:
        ocorrencias = (df[df['NU_ANO'] == ano]['NU_NOTA_REDACAO'] == 1000).sum()
        resultados.append({'NU_ANO': ano, 'Quantidade de notas 1000': ocorrencias})

    return pd.DataFrame(resultados)
