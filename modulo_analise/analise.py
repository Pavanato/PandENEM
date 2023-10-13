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


#RENDA FAMILIAR MEDIA PER CAPITA 
def renda_media_per_capita_familiar(df, colunas_extras):
    '''
    Calcula a renda média per capita familiar de cada participante.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo a coluna "Q006" (letras) e a coluna "Q005" (números).
    colunas_extras : list
        Lista com o nome das colunas que você quer que permaneçam no novo DataFrame.

    Returns
    -------
    df_renda_e_colunas_específicas: pd.DataFrame
        Retorna um novo DataFrame com a coluna de renda per capita e as colunas citadas em colunas_extras.

    Raises
    ------
    ValueError
        Se o DataFrame não contiver as colunas "Q006" e "Q005".
    KeyError
        Se os nomes das colunas não existirem no DataFrame

    Examples
    --------
    >>> df_exemplo = pd.DataFrame({'Q006': ['A', 'D', 'I'], 'Q005': [4, 3, 5]})
    >>> colunas_extras = ['outra_coluna']
    >>> resultado = renda_media_per_capita_familiar(df_exemplo, colunas_extras)
    >>> resultado
       Renda_Per_Capita outra_coluna
    0          0.000000   outra_coluna
    1        665.333333   outra_coluna
    2       1996.000000   outra_coluna

    '''
    try:
        # Verifica se as colunas necessárias estão presentes no DataFrame
        if 'Q006' not in df.columns or 'Q005' not in df.columns:
            raise ValueError("O DataFrame deve conter as colunas 'Q006' e 'Q005'.")

        # Dicionário de valores mínimos e máximos das rendas
        valores_minimos_maximos = {
            'A': (0, 0),
            'B': (0, 998.00),
            'C': (998.00, 1497.00),
            'D': (1497.00, 1996.00),
            'E': (1996.00, 2495.00),
            'F': (2495.00, 2994.00),
            'G': (2994.00, 3992.00),
            'H': (3992.00, 4990.00),
            'I': (4990.00, 5988.00),
            'J': (5988.00, 6986.00),
            'K': (6986.00, 7984.00),
            'L': (7984.00, 8982.00),
            'M': (8982.00, 9980.00),
            'N': (9980.00, 11976.00),
            'O': (11976.00, 14970.00),
            'P': (14970.00, 19960.00),
            'Q': (19961.00, 999999.00)  # Valor máximo padrão para Q
        }
    
        # Calcule as médias das rendas com base no dicionário de valores mínimos e máximos
        valores_medios = {letra: sum(valores) / 2 for letra, valores in valores_minimos_maximos.items()}
    
        # Mapeia a coluna "Q006" do DataFrame diretamente para as médias
        df['Q006'] = df['Q006'].map(valores_medios.get)
    
        # Divide os valores da coluna "Q006" pelos valores correspondentes na coluna "Q005"
        df['Renda_Per_Capita'] = df['Q006'] / df['Q005']
    
        # Crie um novo DataFrame com a coluna "Renda_Per_Capita" e colunas extras
        df_renda_e_colunas_específicas = df[['Renda_Per_Capita'] + colunas_extras]
    
        return df_renda_e_colunas_específicas

    except KeyError as e:
        raise ValueError(f"Erro ao acessar coluna: {str(e)}")
