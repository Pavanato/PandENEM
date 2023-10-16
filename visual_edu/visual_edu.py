import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def graf_pizza(df : pd.DataFrame, coluna : str, titulo : str):
    """
    Toma uma coluna do df escolhido, cria e plota um gráfico em pizza com os dados

    Parâmetros
    ----------
    df : pd.DataFrame
    
    coluna : str
        Coluna que será retirado os dados para fazer o gráfico em pizza    
    
    Retorna
    -------
    None.

    """
    try:
        if coluna not in df.columns:
            raise KeyError(f"A coluna '{coluna}' não foi encontrada no DataFrame dado.")

        values = df[coluna].value_counts()

        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=values.index, autopct='%1.1f%%', startangle=140)
        plt.title(titulo)
        plt.show()

    except Exception as e:
        print(f"Erro: {str(e)}")



def graf_hist_desvpad(df : pd.DataFrame, coluna : str, titulo : str):
    """
    Toma uma coluna do df escolhido, cria e plota um histograma com a curva de distribuição normal

    Parâmetros
    ----------
    df : pd.DataFrame
    
    coluna : str
        Coluna que será retirado os dados para fazer o histograma e a curva de distribuição normal
    
    Retorna
    -------
    None.

    """


    try:
        # Verifica se a coluna especificada está presente no DataFrame
        if coluna not in df.columns:
            raise KeyError(f"A coluna '{coluna}' não foi encontrada no DataFrame dado.")

        data = df[coluna]

        mean, std = data.mean(), data.std()

        plt.hist(data, bins=20, density=True, alpha=0.6, color='g')

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, std)
        plt.plot(x, p, 'k', linewidth=2)

        plt.title(titulo)
        plt.show()

    except Exception as e:
        print(f"Erro: {str(e)}")


def graf_bar_par(df : pd.DataFrame, coluna_x : str, coluna_y : list, title : str, xlabel : str, ylabel : str):
    """
    Toma um dataframe e uma quantidade de colunas quista, cria e plota um grafico em barras com os dados das colunas escolhidas

    Parâmetros
    ----------
    df : pd.DataFrame
    
    coluna_x : str
        Coluna que dita os objetos analisados
    
    colunas_y : list
        Lista com o nome das colunas do dataframe
    
    title : str
    
    xlabel : str

    ylabel : str
    
    Retorna
    -------
    None.

    """    

    try:
        # Verifica se a coluna_x está presente no DataFrame
        if coluna_x not in df.columns:
            raise KeyError(f"A coluna {coluna_x} não foi encontrada no DataFrame dado.")

        # Verifica se todas as colunas em coluna_y estão presentes no DataFrame
        for y_column in coluna_y:
            if y_column not in df.columns:
                raise KeyError(f"A coluna {y_column} não foi encontrada no DataFrame dado.")

        categorias = df[coluna_x]
        bar_width = 0.35
        posicoes = np.arange(len(categorias))
        plt.figure(figsize=(10, 6))

        for i, y_column in enumerate(coluna_y):
            offset = i * bar_width
            plt.bar(posicoes + offset, df[y_column], width=bar_width, label=y_column)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(posicoes + bar_width * (len(coluna_y) - 1) / 2, categorias)
        plt.legend()
        plt.grid(True)
        plt.show()
    
    except KeyError as e:
        print(f"Erro: {e}")


def graf_curvas(df : pd.DataFrame, coluna_x: str, coluna_y: list, title : str, xlabel : str, ylabel : str):
    """
    Toma um dataframe e uma quantidade de colunas quista, cria e plota as curvas com os valores dados pelas colunas

    Parâmetros
    ----------
    df : pd.DataFrame
    
    coluna_x : str
        Coluna que dita os objetos analisados
    
    colunas_y : list
        Lista com o nome das colunas do dataframe
    
    title : str
    
    xlabel : str

    ylabel : str
    
    Retorna
    -------
    None.

    """

    try:
        # Verifica se a coluna_x está presente no DataFrame
        if coluna_x not in df.columns:
            raise KeyError(f"A coluna {coluna_x} não foi encontrada no DataFrame dado.")

        # Verifica se todas as colunas em coluna_y estão presentes no DataFrame
        for y_column in coluna_y:
            if y_column not in df.columns:
                raise KeyError(f"A coluna {y_column} não foi encontrada no DataFrame dado.")

        plt.figure(figsize=(10, 6))

        for y_column in coluna_y:
            plt.plot(df[coluna_x], df[y_column], label=f'{y_column}')

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(True)
        plt.show()

    except KeyError as e:
        print(f"Erro: {e}")