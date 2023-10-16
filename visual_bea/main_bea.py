import pandas as pd 
import visual_bea as visual
import analise as analise 


df_2019 = pd.read_csv("2019_filtrado.csv", encoding = "unicode_escape", engine = "python")
df_2020 = pd.read_csv("2020_filtrado.csv", encoding = "unicode_escape", engine = "python")
df_2021 = pd.read_csv("2021_filtrado.csv", encoding = "unicode_escape", engine = "python")
df_2022 = pd.read_csv("2022_filtrado.csv", encoding = "unicode_escape", engine = "python")

todos_anos = pd.concat([df_2019, df_2020, df_2021, df_2022], axis=0)

# RENDIMENTO MEDIO ANUAL DO BRASIL

# média das notas e da renda
media_participante = analise.media(todos_anos)
renda_e_nota_media = analise.renda_media_per_capita_familiar(media_participante, ['media', 'NU_ANO'])
medias_Brasil_anual = analise.calcular_media_por_ano(renda_e_nota_media, ['Renda_Per_Capita', 'media'])
visual_medias_do_Brasil_por_ano = visual.grafico_barras_NUMERICA(medias_Brasil_anual, ['Renda_Per_Capita', 'media'], 'renda e notas medias do Brasil')

# apenas a média das notas
media_nota_Brasil_anual = analise.calcular_media_por_ano(media_participante, ['media'])
visual_medias_notas_do_Brasil_por_ano = visual.grafico_barra(media_nota_Brasil_anual, 'NU_ANO', ['media'], 'media das notas do Brasil por ano', 'anos', 'media')



df_internet_concatenado = pd.DataFrame()
lista_dfs = [df_2019, df_2020, df_2021, df_2022]

for index, df in enumerate(lista_dfs):
    # DISTRIBUIÇÃO DAS MÉDIAS GRÁFICO 
    visual.visualizar_distribuicao_notas(analise.media(df), 'media')

    # INTERNET
    # proporção dos participantes que tem acesso à internet 
    df_media = analise.media_internet(df)
    df_media['anos'] = 2019 + index
    df_internet_concatenado = pd.concat([df_internet_concatenado, df_media], axis=0)
    visual.grafico_pizza(df, 'Q025', f'Proporção de pessoas à internet - {2019 + index}')


# proporção dos participantes com as maiores e menores notas que tem acesso à internet 
for index, df in enumerate(lista_dfs):
    # maiores
    df_maiores_ano = analise.media(df).sort_values(by='media', ascending=False)
    top_ano = df_maiores_ano.head(1000)
    visual.frequencia_estado(top_ano, 'SG_UF_PROVA', f"melhores participantes - Estado, {2019 + index}")
    visual.grafico_pizza(top_ano, 'Q025', f' Participantes com melhores desempenhos com ou sem internet - {2019 + index}')
    
    # menores 
    df_menores_ano = analise.media(df).sort_values(by='media', ascending=True)
    piores_ano = df_menores_ano.head(1000)
    visual.frequencia_estado(piores_ano, 'SG_UF_PROVA', f"piores participantes - Estado, {2019 + index}")
    visual.grafico_pizza(piores_ano, 'Q025', f'Participantes com piores desempenhos com ou sem internet - {2019 + index}')
    
visual.graf_bar_par(df_internet_concatenado, 'anos', ['media_sem_internet', 'media_com_internet'], 'Médias dos participantes com e sem acesso à internet', '', '')







