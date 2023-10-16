import pandas as pd
import matplotlib.pyplot as plt

def plot_grafico_de_barras(dataframe, coluna_x, coluna_y, titulo, rotulo_x, rotulo_y):
    """
    Cria e exibe um gráfico de barras a partir de um DataFrame.

    Parâmetros:
    - dataframe: pd.DataFrame
        O DataFrame contendo os dados para o gráfico.
    - coluna_x: str
        A coluna a ser usada no eixo x.
    - coluna_y: str
        A coluna a ser usada no eixo y.
    - titulo: str
        O título do gráfico.
    - rotulo_x: str
        O rótulo do eixo x.
    - rotulo_y: str
        O rótulo do eixo y.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(dataframe[coluna_x], dataframe[coluna_y])
    plt.title(titulo)
    plt.xlabel(rotulo_x)
    plt.ylabel(rotulo_y)
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x, se necessário
    plt.show()


def plot_grafico_de_pizza(dataframe, coluna, title):
    """
    Cria e exibe um gráfico de pizza a partir de um DataFrame.

    Parâmetros:
    ----------
    dataframe : pd.DataFrame
        O DataFrame contendo os dados para o gráfico de pizza.
    
    coluna : str
        O nome da coluna no DataFrame que contém os valores a serem representados no gráfico de pizza.
    
    title : str
        O título do gráfico de pizza.
    """
    # Extrai os valores da coluna especificada
    valores = dataframe[coluna]

    # Extrai os rótulos da coluna de índices
    rotulos = dataframe.index

    # Cria um gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=rotulos, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Assegura que o gráfico seja um círculo.
    plt.title(title)
    plt.show()

import matplotlib.pyplot as plt

def plot_grafico_de_linha(dataframe, column_names, x_axis_label, y_axis_label, title):
    """
    Cria um gráfico de linhas com marcadores nos pontos a partir de um DataFrame e uma lista de nomes de colunas para as linhas.

    Parâmetros:
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

    Exemplo:
    >>> import pandas as pd
    >>> data = {'Ano': [2010, 2011, 2012, 2013, 2014],
    ...         'Vendas_A': [100, 120, 140, 160, 180],
    ...         'Vendas_B': [80, 90, 110, 120, 130]}
    >>> df = pd.DataFrame(data)
    >>> column_names = ['Vendas_A', 'Vendas_B']
    >>> plot_line_chart_with_markers(df, column_names, 'Ano', 'Vendas', 'Vendas por Ano')
    """
    for column_name in column_names:
        plt.plot(dataframe[x_axis_label], dataframe[column_name], marker='o', label=column_name)

    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso:
if __name__ == "__main__":
    import pandas as pd

    data = {'Ano': [2010, 2011, 2012, 2013, 2014],
            'Vendas_A': [100, 120, 140, 160, 180],
            'Vendas_B': [80, 90, 110, 120, 130]}
    df = pd.DataFrame(data)
    column_names = ['Vendas_A', 'Vendas_B']
    plot_grafico_de_linha(df, column_names, 'Ano', 'Vendas', 'Vendas por Ano')

