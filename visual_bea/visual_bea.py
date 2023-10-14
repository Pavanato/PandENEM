import pandas as pd
import matplotlib.pyplot as plt

def grafico_barra(df, coluna_x, coluna_y, titulo, xlabel, ylabel):
    '''
    Cria um gráfico de barras a partir de um DataFrame.

    Parameters:
    df (pd.DataFrame): O DataFrame de onde os dados serão extraídos.
    coluna_x (str): Nome da coluna para o eixo x.
    coluna_y (str): Nome da coluna para o eixo y.
    titulo (str): Título do gráfico.
    xlabel (str): Nome do eixo x.
    ylabel (str): Nome do eixo y.

    Raises:
    ValueError: Se o DataFrame for nulo (None).
    KeyError: Se as colunas especificadas não forem encontradas no DataFrame.

    Returns:
    None.

    Example:
    >>> data = {'Ano': [2010, 2011, 2012, 2013, 2014],
    ...         'Vendas': [100, 120, 150, 140, 180]}
    >>> df = pd.DataFrame(data)
    >>> coluna_x = 'Ano'
    >>> coluna_y = 'Vendas'
    >>> titulo = 'Gráfico de Vendas Anuais'
    >>> xlabel = 'Ano'
    >>> ylabel = 'Vendas'
    >>> grafico_barra(df, coluna_x, coluna_y, titulo, xlabel, ylabel)  # Este comando deve exibir o gráfico
    '''
    try:
        # Verifica se o DataFrame não é nulo (None)
        if df is None:
            raise ValueError("O DataFrame 'df' não pode ser nulo.")

        # Verifica se as colunas especificadas existem no DataFrame
        if coluna_x not in df.columns or coluna_y not in df.columns:
            raise KeyError("As colunas especificadas não existem no DataFrame.")

        # Extração dos dados do DataFrame
        x_data = df[coluna_x]
        y_data = df[coluna_y]

        # Detalhes do gráfico de barras
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

    except ValueError as e:
        print(f"Erro ao criar o gráfico de barras: {str(e)}")
    except KeyError as e:
        print(f"Erro ao criar o gráfico de barras: {str(e)}")


def grafico_linha_barra(df, x_col, y_linha, y_col, titulo):
    '''
    Cria um gráfico que combina gráfico de linha com gráfico de barras a partir de um DataFrame.

    Parameters:
    df (pd.DataFrame): O DataFrame de onde os dados serão extraídos.
    x_col (str): Nome da coluna para o eixo x.
    y_linha (str): Nome da coluna para o eixo y do gráfico de linha.
    y_col (str): Nome da coluna para o eixo y do gráfico de barras.
    titulo (str): Título do gráfico.

    Raises:
    KeyError: Se uma ou mais colunas não forem encontradas no DataFrame.

    Returns:
    None.

    Example:
    >>> data = {'Ano': [2010, 2011, 2012, 2013, 2014],
    ...         'Vendas': [100, 120, 150, 140, 180],
    ...         'Lucro': [20, 30, 35, 25, 40]}
    >>> df = pd.DataFrame(data)
    >>> x_col = 'Ano'
    >>> y_linha = 'Vendas'
    >>> y_col = 'Lucro'
    >>> titulo = 'Vendas e Lucro Anuais'
    >>> grafico_linha_barra(df, x_col, y_linha, y_col, titulo)  # Este comando deve exibir o gráfico
    '''
    try:
        # Verifica se as colunas especificadas existem no DataFrame
        if not all(coluna in df.columns for coluna in [x_col, y_linha, y_col]):
            raise KeyError("Uma ou mais colunas não foram encontradas no DataFrame.")

        # Cria um gráfico de linha
        plt.figure(figsize=(10, 5))
        plt.plot(df[x_col], df[y_linha], marker='o', color='b', label=y_linha)

        # Cria um gráfico de barras
        plt.bar(df[x_col], df[y_col], color='g', alpha=0.5, label=y_col)

        # Configurações do gráfico
        plt.title(titulo)
        plt.xlabel(x_col)
        plt.ylabel("Valores")
        plt.legend(loc='best')
        plt.grid(True)

        # Exibe o gráfico
        plt.show()

    except KeyError as e:
        print(f"Erro ao criar o gráfico combinado: {str(e)}")

def grafico_pizza(df, coluna, titulo):
    '''
    Cria um gráfico de pizza que mostra a distribuição das frequências dos elementos na coluna.

    Parameters:
    df (pd.DataFrame): O DataFrame de onde os dados serão extraídos.
    coluna (str): Nome da coluna específica a ser usada para o gráfico de pizza (coluna dos estados).
    titulo (str): Título do gráfico.

    Raises:
    KeyError: Se a coluna selecionada não for encontrada no DataFrame.

    Returns:
    None.

    Example:
    >>> data = {'Estados': ['MG', 'SP', 'RJ', 'MG', 'SP', 'MG'],
    ...         'Valores': [30, 11, 12, 22, 22222, 22]}
    >>> df = pd.DataFrame(data)
    >>> titulo = 'Distribuição de Estados'
    >>> grafico_pizza(df, 'Estados', titulo)  # Este comando deve exibir o gráfico
    '''
    try:
        # Verifica se a coluna selecionada existe no DataFrame
        if coluna not in df.columns:
            raise KeyError("A coluna não foi encontrada no DataFrame.")

        # Conta as frequências dos estados na coluna
        frequencias = df[coluna].value_counts()

        # Cria um gráfico de pizza com base nas frequências
        plt.figure(figsize=(6, 6))
        plt.pie(frequencias, labels=frequencias.index, autopct='%1.1f%%', startangle=90)
        plt.title(titulo)
        plt.axis('equal')  # Aspecto igual para que o gráfico seja uma pizza

        # Exibe o gráfico
        plt.show()

    except KeyError as e:
        print(f"Erro ao criar o gráfico de pizza: {str(e)}")
        
def grafico_colunas_duplas(df_renda, df_notas):
    '''
    Gera um gráfico de colunas duplas com as médias unificadas de renda e notas por estado.

    Parameters:
    ----------
    df_renda (pd.DataFrame): 
        DataFrame contendo as médias unificadas de renda por estado e a coluna 'CO_UF_PROVA'.

    df_notas (pd.DataFrame):
        DataFrame contendo as médias unificadas de notas por estado e a coluna 'CO_UF_PROVA'.

    Returns:
    ----------
    None

    Raises:
    ValueError: Se as colunas 'CO_UF_PROVA' não existirem nos DataFrames.

    Example:
    >>> df_renda = pd.DataFrame({
    ...     'CO_UF_PROVA': ['MG', 'RJ', 'SP'],
    ...     'Renda_unificada': [500, 600, 700]
    ... })
    >>> df_notas = pd.DataFrame({
    ...     'CO_UF_PROVA': ['RJ', 'SP', 'MG'],
    ...     'Nota_unificada': [85, 90, 80]
    ... })
    >>> grafico_colunas_duplas(df_renda, df_notas)  # Isso irá gerar o gráfico
    '''
    try:
        # Verifica se as colunas 'CO_UF_PROVA' existem nos DataFrames
        if 'CO_UF_PROVA' not in df_renda.columns or 'CO_UF_PROVA' not in df_notas.columns:
            raise ValueError("As colunas 'CO_UF_PROVA' não existem nos DataFrames.")

        # Mesclar os DataFrames com base na coluna 'CO_UF_PROVA' independentemente da ordem
        df_merged = df_renda.merge(df_notas, on='CO_UF_PROVA', how='outer')

        # Configurar as posições das barras no gráfico
        posicoes = range(len(df_merged['CO_UF_PROVA']))

        # Largura das barras
        largura = 0.4

        # Criar o gráfico de colunas duplas
        plt.bar(posicoes, df_merged['Renda_unificada'], largura, label='Renda unificada')
        plt.bar([pos + largura for pos in posicoes], df_merged['Nota_unificada'], largura, label='Nota unificada')

        # Configurar rótulos dos estados no eixo x
        plt.xticks([pos + largura / 2 for pos in posicoes], df_merged['CO_UF_PROVA'])

        # Rotular os eixos
        plt.xlabel('Estados')
        plt.ylabel('Valores')

        # Adicionar legenda
        plt.legend()

        # Mostrar o gráfico
        plt.show()

    except ValueError as e:
        print(f"Erro ao gerar o gráfico: {str(e)}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
