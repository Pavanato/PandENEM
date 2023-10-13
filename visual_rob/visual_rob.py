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
    estados_brasil = gpd.read_file('C:/Users/rober/Downloads/BR_UF_2022/BR_UF_2022.shp')

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
