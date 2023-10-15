import pandas as pd
import filter

# Função que executa a filtragem em cada DataFrame
def filtragem(df, name, remove_dict, check_dict):
    # Remove colunas indesejadas
    maintain_list = check_dict.keys()
    df = df[maintain_list]

    # Remove linhas com valores indesejados, por exemplo, treineiros do ENEM
    df = filter.remover_linhas(df, remove_dict)

    # Verifica se as colunas têm a entrada correta
    filter.checa_entradas(df, check_dict)

    # Remove colunas que não serão mais usadas
    df = df.drop(columns=['IN_TREINEIRO', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT'])
    
    # Cria arquivo CSV com o DataFrame filtrado
    df.to_csv(f'{name}_filtrado.csv', index=False)

# Cria variáveis de controle
columns_to_maintain = ['NU_ANO', 'TP_ESCOLA', 'IN_TREINEIRO', 'SG_UF_PROVA', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 
                       'TP_PRESENCA_LC', 'TP_PRESENCA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 
                       'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'Q005', 'Q006', 'Q025']

ufs_brasil = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", 
              "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", 
              "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

# Crie um dicionário combinando as duas listas
check_entries_dict = dict(zip(columns_to_maintain, columns_entries))

columns_entries = [list(range(2019, 2023)), [1, 2, 3], [0, 1], ufs_brasil, 
                   [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], (0.0, 1000.0), (0.0, 1000.0), 
                   (0.0, 1000.0), (0.0, 1000.0), (0.0, 1000.0), list(range(1, 21)), 
                   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'], ['A', 'B']]

rows_to_remove = {
    'IN_TREINEIRO': 1,
    'TP_PRESENCA_CN': [0, 2],
    'TP_PRESENCA_CH': [0, 2],
    'TP_PRESENCA_LC': [0, 2],
    'TP_PRESENCA_MT': [0, 2]
}

# Lê os DataFrames a partir dos arquivos CSV e aplica operações de filtragem
for year in range(2019, 2023):
    df = pd.read_csv(fr"filter\DADOS\MICRODADOS_ENEM_{str(year)}.csv", encoding='unicode_escape', engine='python', sep=';')
    filtragem(df, str(year), rows_to_remove, check_entries_dict)
