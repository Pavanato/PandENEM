import pandas as pd

def separar_ufs_e_anos(df: pd.DataFrame, ufs: list, anos: list) -> pd.DataFrame:
    """
    Toma o DataFrame e o filtra por qualquer quantidade de estados e anos.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame original
    
    ufs : list
        Lista com estados que queira separar do DataFrame original. Os estados devem ser
        escritos pela sigla UF.

    anos : list
        Lista com anos que queira separar do DataFrame original.
    
    Returns
    -------
    pd.DataFrame
        DataFrame filtrado pelos estados e anos escolhidos.

    Raises
    ------
    ValueError
        Se a entrada fornecida não tiver estados ou anos válidos.

    Exemplos
    --------
    >>> import pandas as pd
    >>> data = {'SG_UF_PROVA': ['SP', 'RJ', 'MG', 'SP', 'RJ'],
    ...         'NU_ANO': [2020, 2020, 2021, 2021, 2021],
    ...         'Nota': [70, 80, 90, 85, 95]}
    >>> df = pd.DataFrame(data)
    >>> estados_para_filtrar = ['SP', 'MG']
    >>> anos_para_filtrar = [2020]
    >>> separar_ufs_e_anos(df, estados_para_filtrar, anos_para_filtrar)
      SG_UF_PROVA   Ano  Nota
    0          SP  2020    70
    1          RJ  2020    80
    """
    ufs = [uf.upper() for uf in ufs]

    if 'SG_UF_PROVA' not in df.columns or 'NU_ANO' not in df.columns:
        raise ValueError("As colunas 'SG_UF_PROVA' e 'NU_ANO' devem estar presentes no DataFrame.")

    if not set(ufs).issubset(df['SG_UF_PROVA']):
        raise ValueError("A entrada fornecida não contém estados válidos.")

    if not set(anos).issubset(df['NU_ANO']):
        raise ValueError("A entrada fornecida não contém anos válidos.")

    return df[(df['SG_UF_PROVA'].isin(ufs)) & (df['NU_ANO'].isin(anos))]

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
    >>> data = {'SG_UF_PROVA': ['AM', 'SP', 'BA', 'SC', 'GO', 'RS'],
    ...         'OutrosDados': [1, 2, 3, 4, 5, 6]}
    >>> df = pd.DataFrame(data)
    >>> separar_regiao(df, 'sudeste')
      SG_UF_PROVA  OutrosDados
    1          SP            2
    """
    
    regiao = regiao.lower()
    regioes = {"norte": ["AM", "RR", "AP", "PA", "TO", "RO", "AC"],
               "nordeste": ["MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA"],
               "centro_oeste": ["MT", "MS", "GO"],
               "sudeste": ["SP", "RJ", "ES", "MG"],
               "sul": ["PR", "SC", "RS"]}

    if "SG_UF_PROVA" not in df.columns:
        raise ValueError("A DataFrame fornecido não é tem a coluna 'SG_UF_PROVA'")
    if regiao not in regioes:
        raise ValueError("A entrada fornecida não é uma região válida")
    
    filt = df["SG_UF_PROVA"].isin(regioes[regiao])
    return df.loc[filt]

def media(df):
    """
    Calcula a média de colunas específicas e adiciona uma nova coluna ao DataFrame.

    Args:
        df (pandas.DataFrame): O DataFrame que você deseja modificar.
        nome_nova_coluna (str): O nome da nova coluna que conterá as médias.

    Returns:
        pandas.DataFrame: O DataFrame modificado com a nova coluna de médias.
    """
    colunas_media = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
    df['media'] = df[colunas_media].mean(axis=1)
    return df

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
    TypeError
        se o tipo de argumento dado for errado
    
    
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
            'Q': (19961.00, 50000.00)  # Valor máximo padrão para Q
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
        
    except TypeError as typeerro:
        raise TypeError(f"Erro ao acessar coluna: {str(typeerro)}")
        
def obter_top_500000_maiores_medias(df):
    """
    Retorna as 500000 linhas do DataFrame com as maiores médias de notas.

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
        top_500000 = df.head(500000)

        return top_500000

    except ValueError as e:
        print(f"Erro ao calcular as maiores médias: {str(e)}")

def obter_top_500000_menores_medias(df):
    """
    Retorna as 100000 linhas do DataFrame com as menores médias de notas.

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

        # Pega as primeiras 1000 linhas
        top_500000 = df.head(500000)

        return top_500000

    except ValueError as e:
        print(f"Erro ao calcular as menores médias: {str(e)}")
        
def nota_unificada_por_estado_e_ano(df):
    """
    Calcula a média das notas por estado em um DataFrame, também separado por ano.

    Parâmetros:
    ----------
    df (pd.DataFrame): 
        O DataFrame contendo colunas de estados, anos e as médias de cada participante.

    Retorna:
    pd.DataFrame
        Um novo DataFrame que contém as médias das notas, os estados correspondentes e, opcionalmente, os anos.

    Exemplo:
    >>> data = {'SG_UF_PROVA': ['MG', 'SP', 'RJ', 'MG', 'SP', 'MG'],
    ...         'Ano': [2020, 2020, 2021, 2021, 2021, 2021],
    ...         'media': [80, 85, 90, 78, 88, 92]}
    >>> df = pd.DataFrame(data)
    >>> medias_df = nota_unificada_por_estado_e_ano(df)
    >>> print(medias_df)
      SG_UF_PROVA   Ano  Nota_unificada
    0          MG  2020       81.000000
    1          MG  2021       90.000000
    2          RJ  2021       90.000000
    3          SP  2020       85.000000
    4          SP  2021       90.000000
    """
    try:
        # Verifica se as colunas necessárias existem no DataFrame
        if 'SG_UF_PROVA' not in df.columns or 'media' not in df.columns or 'NU_ANO' not in df.columns:
            raise ValueError("Colunas 'SG_UF_PROVA', 'NU_ANO' e 'media' não encontradas no DataFrame.")

        # Calcula a média das notas por estado e ano
        medias = df.groupby(['SG_UF_PROVA', 'NU_ANO'])['media'].mean().reset_index()
        medias.columns = ['SG_UF_PROVA', 'NU_ANO', 'Nota_unificada']

        return medias

    except ValueError as e:
        print(f"Erro ao calcular a média unificada das notas por estado e ano: {str(e)}")

def renda_unificada_por_estado(df):
    '''
    Calcula a média unificada das rendas per capita familiar por estado.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo as colunas "SG_UF_PROVA" (código do estado) e "Renda_Per_Capita" (média da renda per capita).

    Returns
    -------
    df_renda_unificada_por_estado: pd.DataFrame
        Retorna um novo DataFrame com a coluna "SG_UF_PROVA" e a média unificada de renda por estado (coluna "Renda_Unificada").

    Raises
    ------
    ValueError
        Se o DataFrame não contiver as colunas "SG_UF_PROVA" e "Renda_Per_Capita."

    Examples
    --------
    >>> df_exemplo = pd.DataFrame({
    ...     'SG_UF_PROVA': [1, 2, 1, 2],
    ...     'Renda_Per_Capita': [500, 600, 700, 800],
    ...     'Outra_Coluna': [10, 20, 30, 40]
    ... })
    >>> resultado = renda_unificada_por_estado(df_exemplo)
    >>> resultado
       SG_UF_PROVA  Renda_unificada
    0           1             600.0
    1           2             700.0
    '''
    try:
        # Verifica se as colunas necessárias estão presentes no DataFrame
        if 'SG_UF_PROVA' not in df.columns or 'Renda_Per_Capita' not in df.columns:
            raise ValueError("O DataFrame deve conter as colunas 'SG_UF_PROVA' e 'Renda_Per_Capita'.")

        # Calcula a média da renda per capita por estado
        df_renda_unificada_por_estado = df.groupby('SG_UF_PROVA').agg({'Renda_Per_Capita': 'mean'}).reset_index()

        # Renomeia a coluna "Renda_Per_Capita" para "Renda_unificada"
        df_renda_unificada_por_estado.rename(columns={'Renda_Per_Capita': 'Renda_unificada'}, inplace=True)
        

        return df_renda_unificada_por_estado[['SG_UF_PROVA', 'Renda_unificada']]

    except KeyError as e:
        raise ValueError(f"Erro ao acessar coluna: {str(e)}")

def media_internet(df):
    """
    Calcula a média de colunas específicas para linhas com "A" e "B" na coluna "Q025" e retorna um DataFrame com a média dessas médias.

    Parâmetros:
        df (pandas.DataFrame): O DataFrame que você deseja modificar.

    Retorna:
        pandas.DataFrame: Um DataFrame com a média das colunas "media_A" e "media_B".
    """
    try:
        # Verifica se a coluna "Q025" está presente no DataFrame
        if 'Q025' not in df.columns:
            raise ValueError("A coluna 'Q025' não está presente no DataFrame.")

        # Colunas a serem consideradas para o cálculo da média
        colunas_media = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]

        # Filtra as linhas com "A" na coluna "Q025" e calcula a média das colunas desejadas
        df['media_A'] = df[df['Q025'] == 'A'][colunas_media].mean(axis=1)

        # Filtra as linhas com "B" na coluna "Q025" e calcula a média das colunas desejadas
        df['media_B'] = df[df['Q025'] == 'B'][colunas_media].mean(axis=1)

        # Calcula a média das colunas "media_A" e "media_B"
        media_final = df[['media_A', 'media_B']].mean()

        # Cria um novo DataFrame com as médias
        df_resultado = pd.DataFrame({'media_sem_internet': [media_final['media_A']], 'media_com_internet': [media_final['media_B']]})

        return df_resultado

    except ValueError as e:
        print(f"Erro ao calcular médias por 'Q025': {str(e)}")

def media_por_estado(df, coluna_media):
    """
    Calcula a média das notas por estado e cria um DataFrame.

    Parameters
    ----------
    df : DataFrame
        Um DataFrame contendo as notas por estado.
    coluna_media : str
        O nome da coluna que contém as notas a serem usadas para o cálculo da média.

    Returns
    -------
    DataFrame
        Um DataFrame com a média das notas por estado.

    Description
    -----------
    Esta função calcula a média das notas por estado a partir de um DataFrame fornecido. Ela usa uma lista de siglas dos
    estados brasileiros para iterar e calcular a média das notas para cada estado. O resultado é um novo DataFrame com
    duas colunas: 'UF' (siglas dos estados) e 'media' (média das notas).

    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'UF': ['AC', 'AL', 'AP', 'AM', 'BA'],
    ...         'nota': [7.8, 6.5, 8.2, 7.1, 6.9]}
    >>> df = pd.DataFrame(data)
    >>> media_por_estado(df, 'nota')
       UF  media
    0  AC   7.8
    1  AL   6.5
    2  AP   8.2
    3  AM   7.1
    4  BA   6.9
    """
    list_uf = [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF',
        'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA',
        'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS',
        'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    ]

    # Define um índice no DataFrame com base nos anos e nas siglas dos estados
    df.set_index(['NU_ANO', 'SG_UF_PROVA'], inplace=True)

    data_dict = {}
    # Calcula a média de notas para cada estado e armazena em um dicionário
    for uf in list_uf:
        data_dict[uf] = df.xs(uf, level=1)[str(coluna_media)].mean(axis=0)

    data = {
        'UF': list(data_dict.keys()),
        'media': list(data_dict.values())
    }

    # Converte o dicionário em um DataFrame
    df_result = pd.DataFrame(data)

    return df_result

def media_por_area_de_conhecimento(df):
    """
    Calcula a média das notas por área de conhecimento e cria um DataFrame.

    Parameters
    ----------
    df : DataFrame
        Um DataFrame contendo as notas por área de conhecimento.

    Returns
    -------
    DataFrame
        Um DataFrame contendo a média das notas por área de conhecimento, com as seguintes colunas: "CN", "CH", "LC", "MT", "RD"
        (Ciências da Natureza, Ciências Humanas, Linguagens e Códigos, Matemática, Redação).

    Examples
    --------
    >>> import pandas as pd
    >>> data = {'NU_NOTA_CN': [650.0, 720.0, 680.0],
    ...         'NU_NOTA_CH': [700.0, 680.0, 720.0],
    ...         'NU_NOTA_LC': [710.0, 690.0, 730.0],
    ...         'NU_NOTA_MT': [720.0, 710.0, 690.0],
    ...         'NU_NOTA_REDACAO': [800, 750, 820]}
    >>> df = pd.DataFrame(data)
    >>> media_por_area_de_conhecimento(df)
          CN     CH     LC     MT   RD
    0  683.333333  700.0  710.0  710.0  790.0
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("O parâmetro 'df' deve ser um DataFrame.")
    
    # Lista de colunas que serão usadas para calcular a média
    colunas_media = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]

    for coluna in colunas_media:
        if coluna not in df.columns:
            raise ValueError(f"A coluna {coluna} não está presente no DataFrame.")
        
    # Calcula a média das notas em cada coluna e transforma o resultado em um DataFrame
    df = df[colunas_media].mean().to_frame().T
    df.columns = ["CN", "CH", "LC", "MT", "RD"]

    return df
