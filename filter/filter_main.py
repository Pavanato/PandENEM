import pandas as pd
import filter
import time



def filtragem(df, name, dict = None, lista = None):
    inicio = time.time()
    df = df[lista]
    print(df['NU_NOTA_CN'])
    df = filter.remover_linhas(df, dict)
    # df = check_entry(df, list)
    # df = df.dropna()
    novos_nomes_colunas = {'Q005': 'NU_RESIDENTES', 'Q006': 'RENDA', 'Q022': 'NU_CELULARES','Q024': 'NU_COMPUTADORES', 'Q025': 'INTERNET'}
    df.rename(columns=novos_nomes_colunas, inplace=True)
    print(df['NU_NOTA_CN'])
    df = df.head(2000)
    df = df.drop(columns=['TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT'])
    df.to_csv(f'{name}_filtrado.csv', index=False)
    df = df.dropna()
    print(df.head())
    fim = time.time()
    print(fim - inicio)



columns_to_maintain = ['NU_ANO', 'TP_SEXO', 'TP_COR_RACA','TP_ESCOLA', 'TP_ENSINO', 
                    'IN_TREINEIRO', 'CO_UF_PROVA', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 
                    'TP_PRESENCA_LC', 'TP_PRESENCA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 
                    'NU_NOTA_LC', 'NU_NOTA_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_REDACAO', 
                    'Q005', 'Q006', 'Q022', 'Q024', 'Q025']


column_value_dict = {
    'IN_TREINEIRO': 1,
    'TP_PRESENCA_CN': 0,
    'TP_PRESENCA_CH': 0,
    'TP_PRESENCA_LC': 0,
    'TP_PRESENCA_MT': 0
    }



df_2019 = pd.read_csv(r"filter\DADOS\MICRODADOS_ENEM_2019.csv", encoding='unicode_escape', engine='python', sep=';')

filtragem(df_2019, '2019', column_value_dict, columns_to_maintain)

df_2020 = pd.read_csv(r"filter\DADOS\MICRODADOS_ENEM_2020.csv", encoding='unicode_escape', engine='python', sep=';')

filtragem(df_2020, '2020', column_value_dict, columns_to_maintain)

df_2021 = pd.read_csv(r"filter\DADOS\MICRODADOS_ENEM_2021.csv", encoding='unicode_escape', engine='python', sep=';')

filtragem(df_2021, '2021', column_value_dict, columns_to_maintain)

df_2022 = pd.read_csv(r"filter\DADOS\MICRODADOS_ENEM_2022.csv", encoding='unicode_escape', engine='python', sep=';')

filtragem(df_2022, '2022', column_value_dict, columns_to_maintain)

# columns_entries = ['MF', '0123456', '123', '12', '01', 'PULA', '012', '012', '012', '012', float, float, float, float, '123456789', float, int, 'ABCDEFGHIJKLMNOPQ', 'ABCDE', 'ABCDE', 'AB']
