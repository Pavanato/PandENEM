import pandas as pd

def merge_dataframes(*dfs):
    """
    Mescla vários dataframes em um único dataframe com um índice múltiplo.

    Parameters
    ----------
        *dfs: Número variável de dataframes para mesclar.
    
    Returns
    -------
        pd.DataFrame: Dataframe mesclado com um índice múltiplo.

    Example
    -------
    >>> df1 = pd.DataFrame({'NU_ANO': [2019, 2019], 'A': [1, 2], 'B': [3, 4]})
    >>> df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    >>> df3 = pd.DataFrame({'NU_ANO': [2021, 2021], 'C': [9, 10], 'D': [11, 12]})
    >>> merge_dataframes(df1, df2, df3)
            NU_ANO    A    B     C     D
    Ano
    2019 0  2019.0  1.0  3.0   NaN   NaN
         1  2019.0  2.0  4.0   NaN   NaN
    1    0     NaN  5.0  7.0   NaN   NaN
         1     NaN  6.0  8.0   NaN   NaN
    2021 0  2021.0  NaN  NaN   9.0  11.0
         1  2021.0  NaN  NaN  10.0  12.0
    """

    if not dfs:
        raise ValueError("Pelo menos um dataframe deve ser fornecido.")

    years = []

    for index, df in enumerate(dfs):
        if 'NU_ANO' in df.columns:
            years.append(df['NU_ANO'].iloc[0])
        else:
            years.append(index)

    if len(years) != len(dfs):
        raise ValueError("O número de anos deve corresponder ao número de dataframes.")

    multi_index = pd.MultiIndex.from_tuples([(ano,) for ano in years])
    merged_dataframe = pd.concat(dfs, keys=multi_index)
    
    return merged_dataframe


import pandas as pd

def remover_linhas(df, dict_remover):
    """
    Remove linhas de um DataFrame onde as colunas especificadas coincidem com os valores fornecidos.

    Args:
        df (pd.DataFrame): O DataFrame a ser processado.
        dict_remover (dict): Um dicionário com os nomes das colunas como chaves e valores para coincidir.

    Returns:
        pd.DataFrame: Um novo DataFrame com as linhas removidas conforme especificado.

    Exemplos:
        >>> dados = {
        ...     'IN_TREINEIRO': [0, 1, 0, 0, 2, 0],
        ...     'TP_PRESENCA_CN': [0, 0, 1, 0, 0, 0],
        ...     'TP_PRESENCA_CH': [0, 1, 0, 0, 0, 0],
        ...     'TP_PRESENCA_LC': [0, 0, 1, 0, 0, 0],
        ...     'TP_PRESENCA_MT': [0, 1, 0, 0, 0, 0]
        ... }
        >>> df = pd.DataFrame(dados)
        >>> dict_remover = {
        ...     'IN_TREINEIRO': 1,
        ...     'TP_PRESENCA_CN': 1,
        ...     'TP_PRESENCA_CH': 1,
        ...     'TP_PRESENCA_LC': 1,
        ...     'TP_PRESENCA_MT': 1
        ... }
        >>> resultado_df = remover_linhas(df, dict_remover)
        >>> resultado_df
           IN_TREINEIRO  TP_PRESENCA_CN  TP_PRESENCA_CH  TP_PRESENCA_LC  TP_PRESENCA_MT
        0              0              0              0              0              0
        4              2              0              0              0              0

    Nota:
        A função remove as linhas onde qualquer par coluna-valor especificado coincide.
    """
    for coluna, valor in dict_remover.items():
        df = df[df[coluna] != valor]
    return df



# class InvalidEntryError(Exception):
#     pass

# def check_entry(df, column_name, entry_list):
#     """
#     Check if all values in a DataFrame column are in the specified list of valid entries.

#     Parameters:
#     - df: DataFrame
#         The input DataFrame.
#     - column_name: str
#         The name of the column to check.
#     - entry_list: list
#         The list of valid entries.

#     Raises:
#     - InvalidEntryError: If any value in the column is not in the entry_list.
#     """
#     column = df[column_name]
#     invalid_entries = column[~column.isin(entry_list)]
    
#     if not invalid_entries.empty:
#         raise InvalidEntryError(f"Invalid entries found in column '{column_name}': {invalid_entries.tolist()}")

# # Example usage:
# import pandas as pd

# data = {'Column1': ['A', 'B', 'C', 'D', 'E']}
# df = pd.DataFrame(data)

# valid_entries = ['A', 'B', 'C', 'D']

# try:
#     check_entry(df, 'Column1', valid_entries)
#     print("All entries are valid.")
# except InvalidEntryError as e:
#     print(e)

