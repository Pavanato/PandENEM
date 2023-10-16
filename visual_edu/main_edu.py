import sys
sys.path.append('/path/to/directory')
import pandas as pd
import analise
import visual_edu as visual

df_2019 = pd.read_csv("2019_filtrado.csv", encoding="unicode_escape", engine="python")
df_2020 = pd.read_csv("2020_filtrado.csv", encoding="unicode_escape", engine="python")
df_2021 = pd.read_csv("2021_filtrado.csv", encoding="unicode_escape", engine="python")
df_2022 = pd.read_csv("2022_filtrado.csv", encoding="unicode_escape", engine="python")

df = pd.concat([df_2019, df_2020, df_2021, df_2022], axis=0)



#   RELAÇÃO ENTRE OS ESTADOS DURANTE OS ANOS

anos = [2019, 2020, 2021, 2022]
for ano in anos:
    df_ano = globals()[f'df_{ano}']
    df_media_ano = analise.media(df_ano)
    df_media_estados_ano = analise.nota_unificada_por_estado_e_ano(df_media_ano)
    df_media_estados_ano = df_media_estados_ano.sort_values(by='Nota_unificada')
    visual.graf_bar_par(df_media_estados_ano, 'SG_UF_PROVA', ['Nota_unificada'], f'Comparação das médias entre os estados {ano} ', '', '')
    

#   ANÁLISE DA EVOLUÇÃO DAS MÉDIAS DE CADA ESTADO

def evolucao_UF(df, UF):
    df_UF = analise.separar_ufs_e_anos(df, [f'{UF}'], [2019,2020,2021,2022])
    df_UF_media = analise.media(df_UF)
    df_UF_final = analise.nota_unificada_por_estado_e_ano(df_UF_media)
    visual.graf_curvas(df_UF_final, 'NU_ANO', ['Nota_unificada'], f'Evolução das Médias do ENEM, {UF}', '', '')

UFS = ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO', 'DF']
for uf in UFS:
    evolucao_UF(df, uf)
#   ANÁLISE DO IMPACTO DA FALTA DE INTERNET

anos = ['2019', '2020', '2021', '2022']
df_internet_concatenado = pd.DataFrame()

for ano in anos:
    # Substitua df_XXXX pelo seu DataFrame real para cada ano
    df_ano = analise.media_internet(globals()[f"df_{ano}"])
    df_ano['anos'] = ano
    df_internet_concatenado = pd.concat([df_internet_concatenado, df_ano], axis=0)

print(df_internet_concatenado)
visual.graf_bar_par(df_internet_concatenado, 'anos', ['media_sem_internet', 'media_com_internet'], 'Diferença das Médias dos participantes com e sem acesso à internet', '', '')


#   PROPORÇÃO DOS ALUNOS COM E SEM INTERNET DURANTE OS ANOS

anos = [2019,2020,2021,2022]
for ano in anos:
    df_ano = globals()[f'df_{ano}']
    visual.graf_pizza(df_ano, 'Q025', f'Proporção dos alunos com e sem acesso à internet, {ano}')


#   ANÁLISE DO IMPACTO NA QUANTIDADE DE NOTAS 1000 NO ENEM


df_1000= analise.nota_1000_ano(df, [2019,2020,2021,2022])

visual.graf_bar_par(df_1000, 'NU_ANO', ['Quantidade de notas 1000'], 'Notas 1000', '', '')


#   RENDA POR ESTADO
anos = [2019, 2020, 2021, 2022]
for ano in anos:
    df_ano = globals()[f'df_{ano}']
    df_renda_familiar_ano = analise.renda_media_per_capita_familiar(df_ano, ['SG_UF_PROVA'])
    df_renda_ano = analise.renda_unificada_por_estado(df_renda_familiar_ano)
    df_renda_ano = df_renda_ano.sort_values(by='Renda_unificada')
    visual.graf_bar_par(df_renda_ano, 'SG_UF_PROVA', ['Renda_unificada'], f'Renda dos participantes em comparação com os estados, {ano}', '', '')

