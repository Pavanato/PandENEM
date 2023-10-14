import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# SEPARAR O DATAFRAME POR ESTADO
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

# SEPARAR O DATAFRAME POR REGIAO
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



# NOTAS 1000 DOS ALUNOS 
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


# RENDA FAMILIAR MEDIA PER CAPITA 
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
        
# CRIA DATAFRAME COM 1000 LINHAS CONTENDO AS MAIORES NOTAS
def obter_top_1000_maiores_medias(df):
    """
    Retorna as 1000 linhas do DataFrame com as maiores médias de notas.

    Esta função calcula a média das colunas 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC',
    'NU_NOTA_MT' e 'NU_NOTA_REDACAO' em cada linha do DataFrame e retorna as 1000 linhas
    com as maiores médias em ordem decrescente.

    Args:
        df (pd.DataFrame): O DataFrame de entrada com as notas.

    Returns:
        pd.DataFrame: Um novo DataFrame contendo as 1000 linhas com as maiores médias com nova coluna 'media'

    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'NU_NOTA_CN': [80, 90, 70, 85], 'NU_NOTA_CH': [75, 88, 92, 78], 'NU_NOTA_LC': [82, 79, 88, 85], 'NU_NOTA_MT': [87, 92, 78, 90], 'NU_NOTA_REDACAO': [80, 85, 88, 92]})
        >>> resultado = obter_top_1000_maiores_medias(df)
        >>> resultado.shape[0]
        4
        >>> resultado['media'].iloc[0] >= resultado['media'].iloc[1]
        True
    """
    try:
        if df is None:
            raise ValueError("O DataFrame 'df' não pode ser nulo.")

        colunas_com_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

        if not all(coluna in df.columns for coluna in colunas_com_notas):
            raise ValueError("O DataFrame não contém todas as colunas necessárias para calcular a média.")

        # Calcula a média das colunas especificadas em cada linha
        df['media'] = df[colunas_com_notas].mean(axis=1)

        # Ordena o dataframe pelo valor da coluna 'media' em ordem decrescente
        df = df.sort_values(by='media', ascending=False)

        # Pega as primeiras 1000 linhas
        top_1000 = df.head(1000)

        return top_1000

    except ValueError as e:
        print(f"Erro ao calcular as maiores médias: {str(e)}")

# CRIA DATAFRAME COM 1000 LINHAS CONTENDO AS MENORES NOTAS
def obter_top_1000_menores_medias(df):
    """
    Retorna as 1000 linhas do DataFrame com as menores médias de notas.

    Esta função calcula a média das colunas 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC',
    'NU_NOTA_MT' e 'NU_NOTA_REDACAO' em cada linha do DataFrame e retorna as 1000 linhas
    com as menores médias em ordem crescente.

    Args:
        df (pd.DataFrame): O DataFrame de entrada com as notas.

    Returns:
        pd.DataFrame: Um novo DataFrame contendo as 1000 linhas com as menores médias com nova coluna 'media'

    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'NU_NOTA_CN': [80, 90, 70, 85], 'NU_NOTA_CH': [75, 88, 92, 78], 'NU_NOTA_LC': [82, 79, 88, 85], 'NU_NOTA_MT': [87, 92, 78, 90], 'NU_NOTA_REDACAO': [80, 85, 88, 92]})
        >>> resultado = obter_top_1000_menores_medias(df)
        >>> resultado.shape[0]
        4
        >>> resultado['media'].iloc[0] <= resultado['media'].iloc[1]
        True
    """
    try:
        if df is None:
            raise ValueError("O DataFrame 'df' não pode ser nulo.")

        colunas_com_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

        if not all(coluna in df.columns for coluna in colunas_com_notas):
            raise ValueError("O DataFrame não contém todas as colunas necessárias para calcular a média.")

        # Calcula a média das colunas especificadas em cada linha
        df['media'] = df[colunas_com_notas].mean(axis=1)

        # Ordena o dataframe pelo valor da coluna 'media' em ordem crescente
        df = df.sort_values(by='media')

        # Pega as primeiras 1000 linhas
        top_1000 = df.head(1000)

        return top_1000

    except ValueError as e:
        print(f"Erro ao calcular as menores médias: {str(e)}")
        
        
# MEDIA ÚNICA DAS NOTAS DOS PARTICIPANTES DE CADA ESTADO
def nota_unificada_por_estado(df):
    '''
    Calcula a média das notas por estado em um DataFrame.

    Parameters:
    ----------
    df (pd.DataFrame): 
        O DataFrame contendo colunas de estados e as médias de cada participante.

    Returns:
    pd.DataFrame
        Um novo DataFrame que contém as médias das notas e os estados correspondentes.

    Example:
    >>> data = {'CO_UF_PROVA': ['MG', 'SP', 'RJ', 'MG', 'SP', 'MG'],
    ...         'media': [80, 85, 90, 78, 88, 92]}
    >>> df = pd.DataFrame(data)
    >>> medias_df = nota_unificada_por_estado(df)
    >>> print(medias_df)
    CO_UF_PROVA  Nota_unificada
    MG       83.333333
    RJ       90.000000
    SP       86.500000
    '''
    try:
        # Verifica se as colunas 'CO_UF_PROVA' e 'media' existem no DataFrame
        if 'CO_UF_PROVA' not in df.columns or 'media' not in df.columns:
            raise ValueError("Colunas 'CO_UF_PROVA' e 'media' não encontradas no DataFrame.")

        # Calcula a média das notas por estado
        medias = df.groupby('CO_UF_PROVA')['media'].mean().reset_index()
        medias.columns = ['CO_UF_PROVA', 'Nota_unificada']

        return medias

    except ValueError as e:
        print(f"Erro ao calcular a média unificada das notas por estado: {str(e)}")


# MEDIA ÚNICA DAS NOTAS DOS PARTICIPANTES DE CADA ESTADO
def renda_unificada_por_estado(df):
    '''
    Calcula a média unificada das rendas per capita familiar por estado.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo as colunas "CO_UF_PROVA" (código do estado) e "Renda_Per_Capita" (média da renda per capita).

    Returns
    -------
    df_renda_unificada_por_estado: pd.DataFrame
        Retorna um novo DataFrame com a coluna "CO_UF_PROVA" e a média unificada de renda por estado (coluna "Renda_Unificada").

    Raises
    ------
    ValueError
        Se o DataFrame não contiver as colunas "CO_UF_PROVA" e "Renda_Per_Capita."

    Examples
    --------
    >>> df_exemplo = pd.DataFrame({
    ...     'CO_UF_PROVA': [1, 2, 1, 2],
    ...     'Renda_Per_Capita': [500, 600, 700, 800],
    ...     'Outra_Coluna': [10, 20, 30, 40]
    ... })
    >>> resultado = renda_unificada_por_estado(df_exemplo)
    >>> resultado
       CO_UF_PROVA  Renda_unificada
    0           1             600.0
    1           2             700.0
    '''
    try:
        # Verifica se as colunas necessárias estão presentes no DataFrame
        if 'CO_UF_PROVA' not in df.columns or 'Renda_Per_Capita' not in df.columns:
            raise ValueError("O DataFrame deve conter as colunas 'CO_UF_PROVA' e 'Renda_Per_Capita'.")

        # Calcula a média da renda per capita por estado
        df_renda_unificada_por_estado = df.groupby('CO_UF_PROVA').agg({'Renda_Per_Capita': 'mean'}).reset_index()

        # Renomeia a coluna "Renda_Per_Capita" para "Renda_unificada"
        df_renda_unificada_por_estado.rename(columns={'Renda_Per_Capita': 'Renda_unificada'}, inplace=True)

        return df_renda_unificada_por_estado[['CO_UF_PROVA', 'Renda_unificada']]

    except KeyError as e:
        raise ValueError(f"Erro ao acessar coluna: {str(e)}")
