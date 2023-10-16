import pandas as pd
import matplotlib.pyplot as plt



def frequencia_estado(df, coluna_estado, titulo):
    '''
    Cria gráfico de barras com todos os estados do Brasil com sua frequencia no DataFrame
    Parameters
    ----------
    df : pd.DataFrame
        
    coluna_estado : str
        Nome da coluna com os estados.
    titulo : str
        Título do gráfico.

    Returns
    -------
    None.

    '''
    
    # Contagem da frequência dos estados
    frequencia_estados = df[coluna_estado].value_counts()

    # Crie o gráfico de barras
    plt.figure(figsize=(10, 6))
    frequencia_estados.plot(kind='bar', color='skyblue')
    plt.title(titulo)
    plt.xlabel('Estado')
    plt.ylabel('Frequência')
    plt.xticks(rotation=0)  # Para não girar os rótulos dos estados

    # Exibir o gráfico
    plt.show()

# Exemplo de uso
data = {'Estado': ['SP', 'RJ', 'MG', 'SP', 'MG', 'SP', 'RJ', 'MG', 'RJ']}
df = pd.DataFrame(data)

frequencia_estado(df, 'Estado', 'Frequência dos Estados do Brasil')

def grafico_linha(dataframe, column_names, x_axis_label, y_axis_label, title):
    '''
    Parameters
    ----------
    dataframe : pd.DataFrame
        
    column_names : list
        lista com as colunas que você quer usar.
    x_axis_label : str
        nome para eixo x.
    y_axis_label : str
        nome para eixo y.
    title : str
        

    Returns
    -------
    None.

    '''
    for column_name in column_names:
        plt.plot(dataframe[x_axis_label], dataframe[column_name], marker='o', label=column_name)

    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_barra(df, coluna_x, coluna_y, titulo, xlabel, ylabel):
    '''
    Cria um gráfico de barras a partir de um DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        
    coluna_x : str
        Nome da coluna para o eixo x
    coluna_y : str
        Nome da coluna para o eixo y.
    titulo : str
        
    xlabel : str
        Nome do eixo x.
    ylabel : str
        Nome do eixo y.

    Raises
    ------
    ValueError
        DESCRIPTION.
    KeyError
        DESCRIPTION.

    Returns
    -------
    None.

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

    Parameters
    ----------
    df : pd.DataFrame
        
    coluna : str
       Nome da coluna específica a ser usada para o gráfico de pizza
    titulo : str
    

    Raises
    ------
    KeyError
        DESCRIPTION.

    Returns
    -------
    None.

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
        
        
# colunas específicas
def grafico_colunas_duplas(df_renda, df_notas):
    '''
    Gera um gráfico de colunas duplas com as médias unificadas de renda e notas por estado.

    Parameters
    ----------
    df_renda : pd.DataFrame
        DataFrame contendo as médias unificadas de renda por estado e a coluna 'CO_UF_PROVA'.
    df_notas : pd.DataFrame
        DataFrame contendo as médias unificadas de notas por estado e a coluna 'CO_UF_PROVA'.

    Raises
    ------
    ValueError
        Se as colunas 'CO_UF_PROVA' não existirem nos DataFrames..

    Returns
    -------
    None.

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
