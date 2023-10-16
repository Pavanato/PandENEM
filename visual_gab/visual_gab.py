import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot_a_partir_de_dataframe(df, coluna_x, coluna_y, titulo):
    """
    Crie um gráfico de dispersão a partir de um DataFrame com as colunas x e y especificadas.

    Parâmetros
    ----------
    df (pd.DataFrame): O DataFrame contendo os dados.
    coluna_x (str): O nome da coluna para o eixo x.
    coluna_y (str): O nome da coluna para o eixo y.
    titulo (str): Título para o gráfico de dispersão (o padrão é "Gráfico de Dispersão").
    """
    # Verifique se as colunas especificadas existem no DataFrame
    if coluna_x not in df.columns or coluna_y not in df.columns:
        raise ValueError("As colunas especificadas não existem no DataFrame.")

    # Crie um gráfico de dispersão
    plt.figure(figsize=(8, 6))
    plt.scatter(df[coluna_x], df[coluna_y], label=f'{coluna_x} vs {coluna_y}')

    # Defina rótulos e título
    plt.xlabel(coluna_x)
    plt.ylabel(coluna_y)
    plt.title(titulo)

    # Exiba o gráfico
    plt.legend()
    plt.grid()
    plt.show()

def plot_grafico_de_pizza(dataframe, colunas, title):
    """
    Cria e exibe um gráfico de pizza a partir de um DataFrame.

    Parâmetros
    ----------
    dataframe : pd.DataFrame
        O DataFrame contendo os dados para o gráfico de pizza.
    
    colunas : list
        Uma lista de nomes de colunas no DataFrame que contêm os valores a serem combinados no gráfico de pizza.
    
    title : str
        O título do gráfico de pizza.
    """
    # Somar os valores das colunas especificadas
    valores = dataframe[colunas].sum()
    
    # Cria um gráfico de pizza com a soma total
    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=valores.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Assegura que o gráfico seja um círculo.
    plt.title(title)
    plt.show()

def plot_grafico_de_linha(dataframe, column_names, x_axis_label, y_axis_label, title):
    """
    Cria um gráfico de linhas com marcadores nos pontos a partir de um DataFrame e uma lista de nomes de colunas para as linhas.

    Parâmetros
    ----------
    - dataframe: DataFrame
        O DataFrame contendo os dados.
    - column_names: list
        Uma lista de nomes de colunas para as linhas do gráfico.
    - x_axis_label: str
        Rótulo do eixo X.
    - y_axis_label: str
        Rótulo do eixo Y.
    - title: str
        Título do gráfico.
    """
    for column_name in column_names:
        plt.plot(dataframe[x_axis_label], dataframe[column_name], marker='o', label=column_name)

    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

