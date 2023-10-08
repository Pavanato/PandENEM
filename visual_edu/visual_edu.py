import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def graf_pizza(df, column):
    """
    Toma uma coluna de um df e faz um gráfico em pizza com os dados

    Parâmetros
    ----------
    df : df
    
    column : df
        Coluna que será retirado os dados para fazer o gráfico em pizza    
    
    Returns
    -------
    None.

    """

    # Verifica se a coluna especificada está presente no df
    if column not in df.columns:
        print(f"A coluna '{column}' não foi encontrada no df.")
        return
    
    values = df[column].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=values.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Gráfico de Pizza para a Coluna {column}')
    plt.show()



def graf_hist_desvpad(df, coluna):
    """
    Faz um histograma com a curva de distribuiçao normal de uma coluna escolhida de um dataframe

    Parâmetros
    ----------
    df : dataframe
    
    column : df
        Coluna que será retirado os dados para fazer o histograma e a curva de distribuição normal
    
    Returns
    -------
    None.

    """

    # Verifica se a coluna especificada está presente no df
    if coluna not in df.columns:
        print(f"A coluna '{coluna}' não foi encontrada no df.")
        return

    data = df[coluna]

    mean, std = data.mean(), data.std()

    plt.hist(data, bins=20, density=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    plt.plot(x, p, 'k', linewidth=2)

    title = f'Distribuição Normal para a Coluna {coluna}'
    plt.title(title)
    plt.show()

