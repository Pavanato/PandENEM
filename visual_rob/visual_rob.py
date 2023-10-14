import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

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
    # Carrega o shapefile dos estados brasileiros usando geopandas
    estados_brasil = gpd.read_file('BR_UF_2022/BR_UF_2022.shp')

    estados_brasileiros = [
        'Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal',
        'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul',
        'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
        'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia',
        'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'
    ]

    # Cria um DataFrame com os estados
    df_estados = pd.DataFrame({'Estado': estados_brasileiros})

    # Realiza uma junção externa para incluir todos os estados no DataFrame 'Estado'
    df = df_estados.merge(df, on='Estado', how='left')

    # Verifica se os valores únicos correspondem
    unique_estados = df['Estado'].unique()
    unique_nm_uf = estados_brasil['NM_UF'].unique()

    if set(unique_estados) == set(unique_nm_uf):
        # Junta o DataFrame com o GeoDataFrame dos estados brasileiros usando 'NM_UF' como chave
        gdf = estados_brasil.merge(df, left_on='NM_UF', right_on='Estado', how='left')

        # Configura o plot do mapa
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        gdf.boundary.plot(ax=ax, linewidth=1, color='k')
        gdf.plot(column='Média_de_Notas', cmap='YlGnBu', ax=ax, legend=True)

        ax.set_title('Média de Notas por Estado no Brasil')
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

def plot_bar_chart(dataframe, column_names, title):
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

def criar_grafico_setores(df, coluna):
    """
    Cria um gráfico de pizza a partir de uma coluna de um DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        O DataFrame contendo os dados a serem usados para criar o gráfico de pizza.
    coluna : str
        O nome da coluna do DataFrame que será usada para criar o gráfico.

    Returns
    -------
    None
    """
    try:
        contagem = df[coluna].value_counts()

        if not contagem.empty:
            plt.figure(figsize=(8, 8))
            plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.title(f'Distribuição de {coluna}')
            plt.show()
        else:
            raise ValueError(f"A coluna '{coluna}' não contém dados para criar o gráfico de pizza.")

    except (KeyError, ValueError) as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
