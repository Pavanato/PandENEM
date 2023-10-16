import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def plot_notas_por_estado(df):
    """
    Plota um mapa das médias de notas dos estados brasileiros usando um DataFrame de dados.

    Parameters
    ----------
    df : DataFrame
        Um DataFrame contendo a média de notas dos estados brasileiros.

    Returns
    -------
    None

    Description
    -----------
    Esta função carrega um shapefile dos estados brasileiros usando a biblioteca GeoPandas e cria um mapa das médias
    de notas por estado. Ela realiza uma junção entre o DataFrame fornecido e os dados dos estados, garantindo que
    todos os estados estejam representados no DataFrame antes de criar o mapa.

    O resultado é um mapa colorido dos estados brasileiros, onde a intensidade da cor representa a média de notas
    de cada estado. Além disso, a função verifica se os valores únicos nos DataFrames correspondem, a fim de evitar
    erros na junção.
    """
    try:
        # Carrega o shapefile dos estados brasileiros usando geopandas
        estados_brasil = gpd.read_file('BR_UF_2022/BR_UF_2022.shp')
    except FileNotFoundError:
        print("Erro: O arquivo shapefile dos estados brasileiros não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao carregar o shapefile dos estados brasileiros: {str(e)}")
        return

    # Define replacements para UFs
    replacements = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins'
    }

    df['SG_UF_PROVA'] = df['SG_UF_PROVA'].replace(replacements)

    estados_brasileiros = replacements.values()
    
    # Cria um DataFrame com os estados
    df_estados = pd.DataFrame({'SG_UF_PROVA': estados_brasileiros})

    # Realiza uma junção externa para incluir todos os estados no DataFrame 'Estado'
    df = df_estados.merge(df, on='SG_UF_PROVA', how='left')

    # Verifica se os valores únicos correspondem
    unique_estados = df['SG_UF_PROVA'].unique()
    unique_nm_uf = estados_brasil['NM_UF'].unique()

    if set(unique_estados) == set(unique_nm_uf):
        # Junta o DataFrame com o GeoDataFrame dos estados brasileiros usando 'NM_UF' como chave
        gdf = estados_brasil.merge(df, left_on='NM_UF', right_on='SG_UF_PROVA', how='left')

        # Mapeia os valores da coluna 'Nota_unificada' para o novo intervalo de cores (450 a 600)
        vmin = 490
        vmax = 580
        norm = plt.Normalize(vmin, vmax)

        # Configura o plot do mapa
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        gdf.boundary.plot(ax=ax, linewidth=1, color='k')
        gdf.plot(column='Nota_unificada', cmap='Blues', norm=norm, ax=ax, legend=True)

        ano = df['NU_ANO'].iloc[0] # Obtém o ano a partir do DataFrame

        ax.set_title(f'Média de Notas por Estado no Brasil em {ano}')
        ax.set_axis_off()

        plt.show()
    else:
        print("Os valores na coluna 'Estado' não correspondem aos valores na coluna 'NM_UF'.")

def plot_grafico_linhas(dataframe, coluna_x, coluna_y, titulo):
    """
    Gera um gráfico de linhas usando dados de um DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        O DataFrame que contém os dados a serem plotados.
    coluna_x : str
        O nome da coluna a ser usada como eixo X.
    coluna_y : str
        O nome da coluna a ser usada como eixo Y.
    titulo : str
        O título do gráfico.

    Returns
    -------
    None
    """
    try:
        if coluna_x not in dataframe.columns or coluna_y not in dataframe.columns:
            raise ValueError("As colunas especificadas não existem no DataFrame.")
        
        # Tamanho da figura
        plt.figure(figsize=(8, 6))
        plt.plot(dataframe[coluna_x], dataframe[coluna_y], marker='o', linestyle='-', color='b', label=coluna_y)

        # Adiciona rótulos e título ao gráfico
        plt.xlabel(coluna_x)
        plt.ylabel(coluna_y)
        plt.title(titulo)

        plt.legend()

        plt.grid(True)
        plt.show()
    
    except ValueError as e:
        print(f"Erro: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")

def plot_bar_chart(dataframe, column_names, title):
    """
    Plota um gráfico de barras com duas colunas de um DataFrame em barras separadas.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        O DataFrame contendo os dados.
    column_names : list
        Uma lista com os nomes das duas colunas a serem plotadas.
    title : str
        Título do gráfico.

    Returns
    -------
    None
    """
    # Verifica se as colunas estão presentes no DataFrame
    if not all(col in dataframe.columns for col in column_names):
        print("Uma ou mais colunas não estão presentes no DataFrame.")
        return

    # Seleciona as colunas desejadas
    data = dataframe[column_names]

    # Cria um gráfico de barras
    data.plot(kind='bar')

    plt.title(title)
    
    plt.show()

def plot_multi_grafico_linha(*dataframes):
    """
    Plota um gráfico de linha a partir de um número variável de DataFrames.
    Cada DataFrame deve ter uma única linha com os mesmos nomes de coluna.

    Parameters
    ----------
    *dataframes : DataFrame(s)
        Número variável de DataFrames. Cada DataFrame deve conter uma única linha com os mesmos nomes de coluna.

    Returns
    -------
    None
    """

    plt.figure()

    for idx, df in enumerate(dataframes):
        if not isinstance(df, pd.DataFrame):
            print(f"DataFrame {idx + 1} não é um DataFrame válido. Pulando.")
            continue

        # Verifica se o DataFrame possui apenas uma linha
        if df.shape[0] != 1:
            print(f"DataFrame {idx + 1} não possui uma única linha. Pulando.")
            continue

        # Extrai a linha como uma Série
        dados_da_linha = df.iloc[0]

        # Plota os dados como um gráfico de linha
        plt.plot(dados_da_linha.index, dados_da_linha.values, marker='o', label=f'DF {idx + 1}')

    # Adiciona rótulos, legenda e título
    plt.xlabel('Áreas de conhecimento')
    plt.ylabel('Médias')
    plt.legend(['2019', '2020', '2021', '2022'])
    plt.title('Média por área de conhecimento')

    plt.show()


    # Mostra o gráfico
    plt.show()

def plot_scatter(df, x_column, y_column, title="Gráfico de Dispersão", x_label=None, y_label=None):
    """
    Cria um gráfico de dispersão a partir de um DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        O DataFrame contendo os dados.
    x_column : str
        Nome da coluna a ser usada no eixo x.
    y_column : str
        Nome da coluna a ser usada no eixo y.
    title : str, optional
        Título do gráfico (opcional).
    x_label : str, optional
        Rótulo do eixo x (opcional).
    y_label : str, optional
        Rótulo do eixo y (opcional).

    Returns
    -------
    None
    """
    try:
        plt.figure(figsize=(10, 6))  # Define o tamanho da figura

        if x_column not in df.columns or y_column not in df.columns:
            raise ValueError("As colunas especificadas não existem no DataFrame.")

        # Obtém os valores das colunas do DataFrame
        x = df[x_column]
        y = df[y_column]

        # Cria o gráfico de dispersão, alpha controla a transparência dos pontos
        plt.scatter(x, y, alpha=0.5)

        # Define rótulos dos eixos
        plt.xlabel(x_label if x_label else x_column)
        plt.ylabel(y_label if y_label else y_column)

        plt.title(title)

        plt.show()
    except Exception as e:
        print(f"Erro ao plotar gráfico de dispersão: {str(e)}")