import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import analise
import visual_rob as visual

df_2019 = pd.read_csv('C:/Users/rober/Downloads/Dados PandENEM/csv certos/2019_filtrado.csv')
df_2020 = pd.read_csv('C:/Users/rober/Downloads/Dados PandENEM/csv certos/2020_filtrado.csv')
df_2021 = pd.read_csv('C:/Users/rober/Downloads/Dados PandENEM/csv certos/2021_filtrado.csv')
df_2022 = pd.read_csv('C:/Users/rober/Downloads/Dados PandENEM/csv certos/2022_filtrado.csv')

lista_df = [df_2019, df_2020, df_2021, df_2022]

df_concat = pd.concat([df_2019, df_2020, df_2021, df_2022])

# Plotando gráfico de mapa da média dos estados em 2019, 2020, 2021 e 2022
for df in lista_df:
    df_media = analise.media(df)
    df_media_por_estado = analise.nota_unificada_por_estado_e_ano(df_media)

    visual.plot_notas_por_estado(df_media_por_estado)

# Plotando gráfico de várias linhas da média por área de conhecimento
df_med_2019 = analise.media_por_area_de_conhecimento(df_2019)
df_med_2020 = analise.media_por_area_de_conhecimento(df_2020)
df_med_2021 = analise.media_por_area_de_conhecimento(df_2021)
df_med_2022 = analise.media_por_area_de_conhecimento(df_2022)

visual.plot_multi_grafico_linha(df_med_2019, df_med_2020, df_med_2021, df_med_2022)

# Plotando gráfico de linhas da média por área de conhecimento
years = [2019, 2020, 2021, 2022]
df_notas_mil = analise.nota_1000_ano(df_concat, years)

visual.plot_grafico_linhas(df_notas_mil, 'NU_ANO', 'Quantidade de notas 1000', 'Quantidade de notas 1000 por ano')

# Plotando gráfico de dispersão da renda média per capita de cada participante X a média de nota 
for df in lista_df:
    df_media = analise.media(df)
    df_renda_per_cap = analise.renda_media_per_capita_familiar(df_media, ['NU_ANO', 'media'])
    ano = df_renda_per_cap['NU_ANO'].iloc[0] # Obtém o ano a partir do DataFrame de Renda Per Capita

    visual.plot_scatter(df_renda_per_cap, 'media', 'Renda_Per_Capita', f'Gráfico de Dispersão Média vs. Renda em {ano}', 'Média', 'Renda')


# Plotando gráfico de setores da média de notas em relação ao acesso à internet
for df in lista_df:
    ano = df['NU_ANO'].iloc[0] # Obtém o ano a partir do DataFrame da lista
    df_media_internet = analise.media_internet(df)
    
    visual.plot_bar_chart(df_media_internet, ['media_sem_internet', 'media_com_internet'], f'Média dos alunos sem internet vs. com internet em {ano}')



# Plotando gráfico de linha da média de notas de participantes com e sem internet em relação aos anos
for df in lista_df:
    ano = df['NU_ANO'].iloc[0] # Obtém o ano a partir do DataFrame da lista
    df_media_internet = analise.media_internet(df)
    
    visual.plot_bar_chart(df_media_internet, ['media_sem_internet', 'media_com_internet'], f'Média dos alunos sem internet vs. com internet em {ano}')
