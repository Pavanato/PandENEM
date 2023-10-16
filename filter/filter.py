import pandas as pd

def remover_linhas(df, dict_remover):
    """
    Remove linhas de um DataFrame onde as colunas especificadas coincidem com os valores fornecidos.

    Parameters
    ----------
    df : pd.DataFrame 
        O DataFrame a ser processado.
            
    dict_remover : dict
        Um dicionário com os nomes das colunas como chaves e valores para coincidir.
        
    Returns
    -------
    pd.DataFrame
        Um novo DataFrame com as linhas removidas conforme especificado.

    Examples
    --------
        >>> dados = {
        ...     'IN_TREINEIRO': [0, 1, 0, 0, 2, 0],
        ...     'TP_PRESENCA_CN': [0, 0, 1, 0, 0, 0],
        ...     'TP_PRESENCA_CH': [0, 1, 0, 0, 0, 0],
        ...     'TP_PRESENCA_LC': [0, 0, 1, 0, 0, 0],
        ...     'TP_PRESENCA_MT': [0, 1, 0, 0, 0, 0]
        ... }
        >>> df = pd.DataFrame(dados)
        >>> dict_remover = {
        ...     'IN_TREINEIRO': [1, 2],
        ...     'TP_PRESENCA_CN': 1,
        ...     'TP_PRESENCA_CH': 1,
        ...     'TP_PRESENCA_LC': 1,
        ...     'TP_PRESENCA_MT': 1
        ... }
        >>> resultado_df = remover_linhas(df, dict_remover)
        >>> resultado_df
           IN_TREINEIRO  TP_PRESENCA_CN  TP_PRESENCA_CH  TP_PRESENCA_LC  TP_PRESENCA_MT
        0             0               0               0               0               0
        3             0               0               0               0               0
        5             0               0               0               0               0

    Note
    ----
    A função remove as linhas onde qualquer par coluna-valor especificado coincide.
    """
    for coluna, valores in dict_remover.items():
        if not isinstance(valores, list):
            valores = [valores]
        df = df[~df[coluna].isin(valores)]
    return df

class InvalidEntryError(Exception):
    pass

def checa_entradas(df, column_entry_dict):
    """
    Verifica se todos os valores não-NaN nas colunas especificadas de um DataFrame estão dentro do respectivo intervalo de entradas válidas.

    Parameters
    ----------
    df : pd.DataFrame
        O DataFrame de entrada.
    column_entry_dict : dict
        Um dicionário em que as chaves são os nomes das colunas e os valores são:
            - uma lista de entradas válidas, ou
            - uma tupla de (min_value, max_value) para definir o intervalo de entradas válidas.

    Raises
    ------
    InvalidEntryError
        Se algum valor não-NaN em uma coluna estiver fora do intervalo de entradas válidas.

    Examples
    --------
    >>> import pandas as pd
    >>> data = {'Coluna1': ['A', 'B', 'C', 'D', 'E'], 'Coluna2': [1.5, 2.0, 3.7, 999.9, 5.5]}
    >>> df = pd.DataFrame(data)
    >>> entradas_validas = {'Coluna1': ['A', 'B', 'C', 'D'], 'Coluna2': (0.0, 1000.0)}
    >>> check_entries(df, entradas_validas)  # Nenhuma exceção deve ser lançada
    >>> entradas_validas = {'Coluna1': ['A', 'B', 'C', 'X'], 'Coluna2': (0.0, 1000.0)}
    >>> try:
    ...     check_entries(df, entradas_validas)  # Entradas inválidas na 'Coluna1'
    ... except InvalidEntryError as e:
    ...     str(e)
    "Entradas inválidas encontradas na coluna 'Coluna1': ['X']"
    >>> entradas_validas = {'Coluna1': ['A', 'B', 'C', 'D'], 'Coluna2': (0.0, 10.0)}
    >>> try:
    ...     check_entries(df, entradas_validas)  # Entradas inválidas na 'Coluna2'
    ... except InvalidEntryError as e:
    ...     str(e)
    "Entradas inválidas encontradas na coluna 'Coluna2': [999.9, 5.5]"
    """
    for column_name, entry_range in column_entry_dict.items():
        column = df[column_name]
        
        if isinstance(entry_range, list):
            # Verifica uma lista de entradas válidas
            entradas_validas = column[pd.notna(column)]
            entradas_invalidas = entradas_validas[~entradas_validas.isin(entry_range)]
        elif isinstance(entry_range, tuple) and len(entry_range) == 2:
            # Verifica um intervalo de entradas válidas
            min_value, max_value = entry_range
            entradas_validas = column[pd.notna(column)]
            entradas_invalidas = entradas_validas[(entradas_validas < min_value) | (entradas_validas > max_value)]
        else:
            raise ValueError(f"Tipo de entrada inválido para a coluna '{column_name}'")
    
        if not entradas_invalidas.empty:
            raise InvalidEntryError(f"Entradas inválidas encontradas na coluna '{column_name}': {entradas_invalidas.tolist()}")
