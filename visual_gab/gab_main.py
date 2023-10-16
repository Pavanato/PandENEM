import pandas as pd
import matplotlib.pyplot as plt
import visual_gab as visual
import sys
sys.path.append(r'\modulo_analise')
import analise

df_2019 = pd.read_csv(r"\PandENEM\2019_filtrado.csv", encoding='unicode_escape', engine='python')
df_2020 = pd.read_csv(r"\PandENEM\2020_filtrado.csv", encoding='unicode_escape', engine='python')
df_2021 = pd.read_csv(r"\PandENEM\2021_filtrado.csv", encoding='unicode_escape', engine='python')
df_2022 = pd.read_csv(r"\PandENEM\2022_filtrado.csv", encoding='unicode_escape', engine='python')

lista_dfs = [df_2019, df_2020, df_2021, df_2022]

# Visualização que ilustra média de participantes com e sem internet
for index, df in enumerate(lista_dfs):
    df_pizza = analise.media_internet(df)
    visual.plot_grafico_de_pizza(df_pizza, ['media_sem_internet', 'media_com_internet'], f'Relação acesso a internet {2019 + index}')


# Visualização média x matéria nos quatro anos
colunas = ['CN', 'CH', 'LC', 'MT', 'RD']
df_concat = pd.DataFrame()
for index, df in enumerate(lista_dfs):
    df = analise.media_por_area_de_conhecimento(df)
    df_concat = pd.concat([df_concat, df])

df_concat['anos'] = [2019, 2020, 2021, 2022]
visual.plot_grafico_de_linha(df_concat, colunas, 'anos', 'notas', "Média por matéria em cada ano")

# Visualização renda per capita x média
for index, df in enumerate(lista_dfs):
    df = analise.media(df)
    df = analise.renda_media_per_capita_familiar(df, ['media'])
    visual.scatter_plot_a_partir_de_dataframe(df, 'Renda_Per_Capita', 'media', f'Gráfico de dispersão de {2019 + index}')
