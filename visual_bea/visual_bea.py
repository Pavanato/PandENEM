import pandas as pd
import matplotlib.pyplot as plt

def grafico_barra(df, coluna_x, coluna_y, titulo, xlabel, ylabel):
    '''
        Parameters
    ----------
    df : pd.DataFrame 
        arquivo usado.
    coluna_x : str
        eixo x.
    coluna_y : str
        eixo y.
    titulo : str
        tìtulo do gráfico.
    xlabel : str
        nome do eixo x.
    ylabel : str
        nome do eixo y.

    Raises
    ------
    KeyError
        caso as chaves não sejam encontradas no DataFrame

    Returns
    -------
    None.

    '''
    try:
        # Verifica se as colunas especificadas existem no DataFrame
        if coluna_x not in df.columns or coluna_y not in df.columns:
            raise KeyError("As colunas especificadas não existem no DataFrame.")

        # Extração dos dados do DataFrame
        x_data = df[coluna_x]
        y_data = df[coluna_y]

        # detalhes do gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(x_data, y_data, color='skyblue')
        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        # Rotaciona os rótulos do eixo x para melhor legibilidade, se necessário
        plt.xticks(rotation=45)

        # Exibe o gráfico
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Erro ao criar o gráfico de barras: {str(e)}")


def grafico_linha_barra(df, x_col, y1_col, y2_col, titulo):
    '''
    Cria um gráfico que combina gráfico de linha com gráfico de barras a partir de um DataFrame.

    Parameters:
    ----------
    df (pd.DataFrame): 
        O DataFrame de onde os dados serão extraídos.
    x_col (str):
        Nome da coluna para o eixo x.
    y1_col (str):  
        Nome da coluna para o eixo y do gráfico de linha.
    y2_col (str): 
        Nome da coluna para o eixo y do gráfico de barras.
    titulo (str): 
        Título do gráfico.

    Returns:
    None

    Example:
    >>> data = {'Ano': [2010, 2011, 2012, 2013, 2014],
    ...         'Vendas': [100, 120, 150, 140, 180],
    ...         'Lucro': [20, 30, 35, 25, 40]}
    >>> df = pd.DataFrame(data)
    >>> x_col = 'Ano'
    >>> y1_col = 'Vendas'
    >>> y2_col = 'Lucro'
    >>> titulo = 'Vendas e Lucro Anuais'
    >>> grafico_linha_barra(df, x_col, y1_col, y2_col, titulo)  # Este comando deve exibir o gráfico
    '''
    try:
        # Verifica se as colunas especificadas existem no DataFrame
        if not all(coluna in df.columns for coluna in [x_col, y1_col, y2_col]):
            raise ValueError("Uma ou mais colunas não foram encontradas no DataFrame.")

        # Cria um gráfico de linha
        plt.figure(figsize=(10, 5))
        plt.plot(df[x_col], df[y1_col], marker='o', color='b', label=y1_col)

        # Cria um gráfico de barras
        plt.bar(df[x_col], df[y2_col], color='g', alpha=0.5, label=y2_col)

        # Configurações do gráfico
        plt.title(titulo)
        plt.xlabel(x_col)
        plt.ylabel("Valores")
        plt.legend(loc='best')
        plt.grid(True)

        # Exibe o gráfico
        plt.show()

    except Exception as e:
        print(f"Erro ao criar o gráfico combinado: {e}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

def grafico_pizza(df, colunas, titulo):
    '''
    Cria um gráfico de pizza a partir de um DataFrame.

    Parameters:
    ----------
    df (pd.DataFrame): 
        O DataFrame de onde os dados serão extraídos.
    colunas (list): 
        Lista das colunas específicas a serem usadas para o gráfico de pizza.
    titulo (str): 
        Título do gráfico.

    Returns:
    None

    Example:
    >>> data = {'Categoria': ['A', 'B', 'C', 'D'],
    ...         'Valores': [30, 20, 15, 35]}
    >>> df = pd.DataFrame(data)
    >>> colunas = ['Categoria', 'Valores']
    >>> titulo = 'Distribuição de Valores por Categoria'
    >>> plot_pie_chart(df, colunas, titulo)  # Este comando deve exibir o gráfico
    '''
    try:
        # Seleciona as colunas específicas do DataFrame
        dados = df[colunas]

        # Verifica se as colunas selecionadas existem no DataFrame
        if not all(coluna in df.columns for coluna in colunas):
            raise ValueError("Uma ou mais colunas não foram encontradas no DataFrame.")

        # Cria um gráfico de pizza com base nos dados
        plt.figure(figsize=(6, 6))
        plt.pie(dados['Valores'], labels=dados['Categoria'], autopct='%1.1f%%', startangle=90)
        plt.title(titulo)
        plt.axis('equal')  # Aspecto igual para que o gráfico seja uma pizza

        # Exibe o gráfico
        plt.show()

    except Exception as e:
        print(f"Erro ao criar o gráfico de pizza: {e}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()




