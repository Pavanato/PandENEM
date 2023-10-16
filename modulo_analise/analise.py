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
    
    Retorna
    -------
    pd.DataFrame
        DataFrame filtrado pelos estados e anos escolhidos.

    Raises
    ------
    ValueError
        Se a entrada fornecida não tiver estados ou anos válidos.

    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'SG_UF_PROVA': ['SP', 'RJ', 'MG', 'SP', 'RJ'],
    ...         'NU_ANO': [2020, 2020, 2021, 2021, 2021],
    ...         'Nota': [70, 80, 90, 85, 95]}
    >>> df = pd.DataFrame(data)
    >>> estados_para_filtrar = ['SP', 'MG']
    >>> anos_para_filtrar = [2021]
    >>> separar_ufs_e_anos(df, estados_para_filtrar, anos_para_filtrar)
      SG_UF_PROVA  NU_ANO  Nota
    2          MG    2021    90
    3          SP    2021    85
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
    
    Retorna
    -------
    pd.DataFrame
        DataFrame filtrado pela região escolhida

    Raises
    ------
    ValueError
        Se a entrada fornecida não for uma região válida

    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'SG_UF_PROVA': ['AM', 'SP', 'BA', 'SC', 'GO', 'RS'],
    ...         'OutrosDados': [1, 2, 3, 4, 5, 6]}
    >>> df = pd.DataFrame(data)
    >>> separar_regiao(df, 'sudeste')
      SG_UF_PROVA  OutrosDados
    1          SP            2
    """
    
    regiao = regiao.lower()
    # Dicionário para mapear as UFs de cada região
    regioes = {"norte": ["AM", "RR", "AP", "PA", "TO", "RO", "AC"],
               "nordeste": ["MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA"],
               "centro_oeste": ["MT", "MS", "GO"],
               "sudeste": ["SP", "RJ", "ES", "MG"],
               "sul": ["PR", "SC", "RS"]}

    if "SG_UF_PROVA" not in df.columns:
        raise ValueError("A DataFrame fornecido não é tem a coluna 'SG_UF_PROVA'")
    if regiao not in regioes:
        raise ValueError("A entrada fornecida não é uma região válida")
    
    filtro = df["SG_UF_PROVA"].isin(regioes[regiao])

    return df.loc[filtro]

def media(df : pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a média de colunas específicas e adiciona-a ao DataFrame.

    Parâmetros
    ----------
    df: pd.DataFrame
        O DataFrame que você deseja modificar.

    Retorna
    -------
    pd.DataFrame: 
        O DataFrame modificado com a nova coluna de médias.

    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'NU_NOTA_CN': [75, 85, 90, 88, 92],
    ...         'NU_NOTA_CH': [80, 78, 92, 87, 88],
    ...         'NU_NOTA_LC': [92, 89, 78, 90, 85],
    ...         'NU_NOTA_MT': [87, 90, 85, 88, 92],
    ...         'NU_NOTA_REDACAO': [88, 92, 85, 90, 87]}
    >>> df = pd.DataFrame(data)
    >>> media(df)
       NU_NOTA_CN  NU_NOTA_CH  NU_NOTA_LC  NU_NOTA_MT  NU_NOTA_REDACAO  media
    0          75          80          92          87               88   84.4
    1          85          78          89          90               92   86.8
    2          90          92          78          85               85   86.0
    3          88          87          90          88               90   88.6
    4          92          88          85          92               87   88.8
    """
    colunas_media = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
    if not set(colunas_media).issubset(df.columns):
        raise ValueError("O DataFrame deve conter as colunas necessárias para o cálculo da média.")
        
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
    
    Retorna
    -------
    pd.DataFrame
        As linhas do DataFrame são os anos escolhidos e a única coluna a quantidade de notas 1000 neste ano

    Raises
    ------
    ValueError
        Se as colunas 'NU_NOTA_REDACAO' e 'NU_ANO' não estiverem presentes no DataFrame.

    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'NU_ANO': [2020, 2020, 2020, 2021, 2021],
    ...         'NU_NOTA_REDACAO': [1000, 900, 1000, 1000, 950]}
    >>> df = pd.DataFrame(data)
    >>> anos_para_verificar = [2020, 2021]
    >>> nota_1000_ano(df, anos_para_verificar)
       NU_ANO  Quantidade de notas 1000
    0    2020                         2
    1    2021                         1

    """
    if 'NU_NOTA_REDACAO' not in df.columns or 'NU_ANO' not in df.columns:
        raise ValueError("As colunas 'NU_NOTA_REDACAO' e 'NU_ANO' devem estar presentes no DataFrame.")
    
    resultados = []
    for ano in anos:
        ocorrencias = (df[df['NU_ANO'] == ano]['NU_NOTA_REDACAO'] == 1000).sum()
        resultados.append({'NU_ANO': ano, 'Quantidade de notas 1000': ocorrencias})

    return pd.DataFrame(resultados)

def renda_media_per_capita_familiar(df : pd.DataFrame, colunas_extras : list) -> pd.DataFrame:
    '''
    Calcula a renda média per capita familiar de cada participante.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo a coluna "Q006" (letras) e a coluna "Q005" (números).
    colunas_extras : list
        Lista com o nome das colunas que você quer que permaneçam no novo DataFrame.

    Retorna
    -------
    pd.DataFrame
        Retorna um novo DataFrame com a coluna de renda per capita e as colunas citadas em colunas_extras.

    Raises
    ------
    ValueError
        Se o DataFrame não contiver as colunas "Q006" e "Q005".
    KeyError
        Se os nomes das colunas não existirem no DataFrame
    TypeError
        se o tipo de argumento dado for errado7

    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'Q006': ['A', 'B', 'C', 'D'],
    ...         'Q005': [1, 2, 3, 4],
    ...         'Outra_Coluna': ['X', 'Y', 'Z', 'W']}
    >>> df = pd.DataFrame(data)
    >>> colunas_extras = ['Outra_Coluna']
    >>> renda_media_per_capita_familiar(df, colunas_extras)
       Renda_Per_Capita Outra_Coluna
    0          0.000000            X
    1        249.500000            Y
    2        415.833333            Z
    3        436.625000            W
    
    '''
    try:
        if 'Q006' not in df.columns or 'Q005' not in df.columns:
            raise ValueError("O DataFrame deve conter as colunas 'Q006' e 'Q005'.")

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
            'Q': (19961.00, 50000.00)
        }
    
        valores_medios = {letra: sum(valores) / 2 for letra, valores in valores_minimos_maximos.items()}
        df['Q006'] = df['Q006'].map(valores_medios.get)
        df['Renda_Per_Capita'] = df['Q006'] / df['Q005']
        df_renda_e_colunas_específicas = df[['Renda_Per_Capita'] + colunas_extras]
    
        return df_renda_e_colunas_específicas

    except KeyError as e:
        raise ValueError(f"Erro ao acessar coluna: {str(e)}")
    except TypeError as typeerro:
        raise TypeError(f"Erro ao acessar coluna: {str(typeerro)}")
                  
def nota_unificada_por_estado_e_ano(df : pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a média das notas por estado em um DataFrame, também separado por ano.

    Parâmetros
    ----------
    df : pd.DataFrame 
        O DataFrame contendo colunas de estados, anos e as médias de cada participante.

    Retorna
    -------
    pd.DataFrame
        Um novo DataFrame que contém as médias das notas, os estados correspondentes e, opcionalmente, os anos.


    Exemplo
    -------
    >>> data = {'SG_UF_PROVA': ['MG', 'SP', 'RJ', 'MG', 'SP', 'MG'],
    ...         'NU_ANO': [2020, 2020, 2021, 2021, 2021, 2021],
    ...         'media': [80, 85, 90, 78, 88, 92]}
    >>> df = pd.DataFrame(data)
    >>> medias_df = nota_unificada_por_estado_e_ano(df)
    >>> print(medias_df)
      SG_UF_PROVA  NU_ANO  Nota_unificada
    0          MG    2020            80.0
    1          MG    2021            85.0
    2          RJ    2021            90.0
    3          SP    2020            85.0
    4          SP    2021            88.0
    """
    try:
        if all(item not in ['SG_UF_PROVA', 'media', 'NU_ANO'] for item in df.columns):
            raise KeyError("Colunas 'SG_UF_PROVA', 'NU_ANO' e 'media' não encontradas no DataFrame.")

        medias = df.groupby(['SG_UF_PROVA', 'NU_ANO'])['media'].mean().reset_index()
        medias.columns = ['SG_UF_PROVA', 'NU_ANO', 'Nota_unificada']

        return medias

    except ValueError as e:
        print(f"Erro ao calcular a média unificada das notas por estado e ano: {str(e)}")

def renda_unificada_por_estado(df : pd.DataFrame) -> pd.DataFrame:
    '''
    Calcula a média unificada das rendas per capita familiar por estado.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo as colunas "SG_UF_PROVA" (código do estado) e "Renda_Per_Capita" (média da renda per capita).

    Retorna
    -------
    pd.DataFrame
        Retorna um novo DataFrame com a coluna "SG_UF_PROVA" e a média unificada de renda por estado (coluna "Renda_Unificada").

    Raises
    ------
    ValueError
        Se o DataFrame não contiver as colunas "SG_UF_PROVA" e "Renda_Per_Capita."

    Exemplo
    -------
    >>> df_exemplo = pd.DataFrame({
    ...     'SG_UF_PROVA': [1, 2, 1, 2],
    ...     'Renda_Per_Capita': [500, 600, 700, 800],
    ...     'Outra_Coluna': [10, 20, 30, 40]
    ... })
    >>> resultado = renda_unificada_por_estado(df_exemplo)
    >>> print(resultado)
       SG_UF_PROVA  Renda_unificada
    0            1            600.0
    1            2            700.0
    '''
    try:
        if 'SG_UF_PROVA' not in df.columns or 'Renda_Per_Capita' not in df.columns:
            raise ValueError("O DataFrame deve conter as colunas 'SG_UF_PROVA' e 'Renda_Per_Capita'.")

        df_renda_unificada_por_estado = df.groupby('SG_UF_PROVA').agg({'Renda_Per_Capita': 'mean'}).reset_index()

        df_renda_unificada_por_estado.rename(columns={'Renda_Per_Capita': 'Renda_unificada'}, inplace=True)
        
        return df_renda_unificada_por_estado[['SG_UF_PROVA', 'Renda_unificada']]

    except KeyError as e:
        raise ValueError(f"Erro ao acessar coluna: {str(e)}")

def media_internet(df : pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a média de colunas específicas para linhas com "A" e "B" na coluna "Q025" e retorna um DataFrame com a média dessas médias.

    Parâmetros
    ----------
    df : pd.DataFrame 
        O DataFrame que você deseja modificar.

    Retorna
    -------
    pd.DataFrame    
        Um DataFrame com a média das colunas "media_A" e "media_B".

    Raises
    ------
    ValueError
        Se a coluna Q025 não pertence ao DataFrame dado.
        
    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'Q025': ['A', 'A', 'B', 'A', 'B'],
    ...         'NU_NOTA_CN': [75, 85, 90, 88, 92],
    ...         'NU_NOTA_CH': [80, 78, 92, 87, 88],
    ...         'NU_NOTA_LC': [92, 89, 78, 90, 85],
    ...         'NU_NOTA_MT': [87, 90, 85, 88, 92],
    ...         'NU_NOTA_REDACAO': [88, 92, 85, 90, 87]}
    >>> df = pd.DataFrame(data)
    >>> media_internet(df)
       media_sem_internet  media_com_internet
    0                86.6                87.4
    """
    try:
        if 'Q025' not in df.columns:
            raise ValueError("A coluna 'Q025' não está presente no DataFrame.")
        
        colunas_media = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
        df['media_A'] = df[df['Q025'] == 'A'][colunas_media].mean(axis=1)
        df['media_B'] = df[df['Q025'] == 'B'][colunas_media].mean(axis=1)
        media_final = df[['media_A', 'media_B']].mean()
        df_resultado = pd.DataFrame({'media_sem_internet': [media_final['media_A']], 'media_com_internet': [media_final['media_B']]})

        return df_resultado

    except ValueError as e:
        print(f"Erro ao calcular médias por 'Q025': {str(e)}")
        
def calcular_medias_regiao_ano(df : pd.DataFrame) -> pd.DataFrame:
    """
    Calcula as médias das notas por ano e região.

    Parâmetros
    ----------
    df : pd.DataFrame 
        DataFrame contendo os dados das notas.

    Retorna
    -------
    pd.DataFrame    
        DataFrame com as médias por ano e região.
    
    Raises
    ------
    ValueError
        Se o DataFrame não tem todas as colunas necessárias

    Exemplo
    -------
    >>> data = {'NU_ANO': [2021, 2021, 2022, 2022, 2023],
    ...         'SG_UF_PROVA': ['SP', 'RJ', 'SP', 'RJ', 'SP'],
    ...         'media': [7.5, 8.0, 7.8, 8.2, 7.9]}
    >>> df = pd.DataFrame(data)
    >>> calcular_medias_regiao_ano(df)
            Sudeste  Média Brasil
    NU_ANO                       
    2021       7.75          7.75
    2022       8.00          8.00
    2023       7.90          7.90
    """

    try:
        required_columns = ['NU_ANO', 'SG_UF_PROVA', 'media']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("O DataFrame de entrada não contém todas as colunas necessárias.")
        
        mapeamento_regioes = {
            'Norte': ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO'],
            'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
            'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
            'Sul': ['PR', 'RS', 'SC'],
            'Centro-Oeste': ['DF', 'GO', 'MT', 'MS']
        }
        df['Região'] = df['SG_UF_PROVA'].map({estado: regiao for regiao, estados in mapeamento_regioes.items() for estado in estados})

        # Calcular a média do Brasil por ano
        media_brasil_ano = df.groupby(['NU_ANO', 'SG_UF_PROVA'])['media'].mean().groupby('NU_ANO').mean()
        media_brasil_ano = media_brasil_ano.reset_index()
        media_brasil_ano.rename(columns={'media': 'Média Brasil'}, inplace=True)
        media_regiao_ano = df.groupby(['NU_ANO', 'Região'])['media'].mean().unstack()
        result_df = pd.concat([media_regiao_ano, media_brasil_ano.set_index('NU_ANO')['Média Brasil']], axis=1)

        return result_df
    
    except ValueError as e:
        raise ValueError(f"Erro ao calcular as médias por ano e região: {str(e)}")
    
def media_por_area_de_conhecimento(df : pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a média das notas por área de conhecimento e cria um DataFrame.

    Parâmetros
    ----------
    df : pd.DataFrame
        Um DataFrame contendo as notas por área de conhecimento.

    Retorna
    -------
    pd.DataFrame
        Um DataFrame contendo a média das notas por área de conhecimento, com as seguintes colunas: "CN", "CH", "LC", "MT", "RD"
        (Ciências da Natureza, Ciências Humanas, Linguagens e Códigos, Matemática, Redação).

    Exemplo
    -------
    >>> import pandas as pd
    >>> data = {'NU_NOTA_CN': [650.0, 720.0, 680.0],
    ...         'NU_NOTA_CH': [700.0, 680.0, 720.0],
    ...         'NU_NOTA_LC': [710.0, 690.0, 730.0],
    ...         'NU_NOTA_MT': [720.0, 710.0, 690.0],
    ...         'NU_NOTA_REDACAO': [800, 750, 820]}
    >>> df = pd.DataFrame(data)
    >>> media_por_area_de_conhecimento(df)
               CN     CH     LC          MT     RD
    0  683.333333  700.0  710.0  706.666667  790.0
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("O parâmetro 'df' deve ser um DataFrame.")
    
    colunas_media = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]

    for coluna in colunas_media:
        if coluna not in df.columns:
            raise ValueError(f"A coluna {coluna} não está presente no DataFrame.")

    df = df[colunas_media].mean().to_frame().T
    df.columns = ["CN", "CH", "LC", "MT", "RD"]

    return df
