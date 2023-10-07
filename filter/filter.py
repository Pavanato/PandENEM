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


df1 = pd.DataFrame({'NU_ANO': [2019, 2019], 'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'NU_ANO': [2021, 2021], 'C': [9, 10], 'D': [11, 12]})

mesclado = merge_dataframes(df1, df2, df3)
print(mesclado)