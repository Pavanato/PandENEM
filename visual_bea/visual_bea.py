import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def frequencia_estado(df, coluna_estado, titulo): 
    '''
    Cria um gráfico de barras com a frequência de estados a partir de uma coluna em um DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        
    coluna_estado : str
           Nome da coluna com os estados
    titulo : str
        

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

def grafico_barra(df, coluna_x, coluna_y, titulo, xlabel, ylabel, num_divisoes=10):
    '''
    Cria um gráfico de barras a partir de um DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
       
    coluna_x : str
        Nome da coluna para o eixo x.
    coluna_y : list
        Nome das colunas para o eixo y.

    titulo : str
        
    xlabel : str
        nome eixo x.
    ylabel : str
        nome eixo y.
    
    num_divisoes (int):
        Número de divisões no eixo y. O padrão é 10.

    Raises:
    ValueError: Se o DataFrame for nulo (None).

    Returns:
    None.
    '''
 
    try:
        # Verifica se a coluna_x está presente no DataFrame
        if coluna_x not in df.columns:
            raise KeyError(f"A coluna {coluna_x} para o eixo x não foi encontrada no DataFrame dado.")

        # Verifica se todas as colunas em coluna_y estão presentes no DataFrame
        for y_column in coluna_y:
            if y_column not in df.columns:
                raise KeyError(f"A coluna {y_column}  para o eixo y não foi encontrada no DataFrame dado.")

        categorias = df[coluna_x]
        bar_width = 0.35
        posicoes = np.arange(len(categorias))
        plt.figure(figsize=(10, 6))

        for i, y_column in enumerate(coluna_y):
            offset = i * bar_width
            plt.bar(posicoes + offset, df[y_column], width=bar_width, label=y_column)

        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(posicoes + bar_width * (len(coluna_y) - 1) / 2, categorias)
        plt.legend()
        plt.grid(True)
        plt.show()
    
    except KeyError as e:
        print(f"Erro: {e}")


def grafico_linha_barra(df, x_col, y_linha, y_col, titulo):
    '''
    Cria um gráfico que combina gráfico de linha com gráfico de barras a partir de um DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
     
    x_col : str
        
    y_linha : str
       
    y_col : str
        
    titulo : str
        

    Raises
    ------
    KeyError:
         Se uma ou mais colunas não forem encontradas no DataFrame.

    Returns
    -------
    None.

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
        
    titulo : str
  
    Raises
    ------
    KeyError
       Se a coluna selecionada não for encontrada no DataFrame.


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



def grafico_colunas_duplas_NUMERICA(df, colunas_duplas, título, num_divisoes=10):
    '''
    Gera um gráfico de colunas duplas com as colunas especificadas de um DataFrame.

    Parameters:
    ----------
    df (pd.DataFrame): 
        DataFrame contendo as colunas especificadas e uma coluna de categorias (p. ex., estados).

    colunas_duplas (list):
        Lista de nomes das colunas que você deseja incluir no gráfico de colunas duplas.
    
    título (str):
        título do gráfico

    num_divisoes (int):
        Número de divisões no eixo y. O padrão é 10.
        
    Returns:
    ----------
    None

    Raises:
    ValueError: Se a coluna de categorias não existir no DataFrame ou se alguma coluna especificada não existir.

    '''
    try:
        # Verifica se a coluna de categorias existe no DataFrame
        if 'NU_ANO' not in df.columns:
            raise ValueError("A coluna de categorias (p. ex., estados) não existe no DataFrame.")

        # Verifica se todas as colunas especificadas existem no DataFrame
        for col in colunas_duplas:
            if col not in df.columns:
                raise ValueError(f"A coluna '{col}' não existe no DataFrame.")

        # Calcula o valor máximo nas colunas selecionadas
        valor_maximo = max(df[colunas_duplas].max())

        # Calcula o próximo múltiplo de 10 maior ou igual ao valor máximo
        proximo_multiplo_10 = np.ceil(valor_maximo / 10) * 10

        # Calcula o intervalo igualmente espaçado
        intervalo_fixo = proximo_multiplo_10 / num_divisoes

        # Configurar as posições das barras no gráfico
        posicoes = range(len(df['NU_ANO']))

        # Largura das barras
        largura = 0.4

        # Criar o gráfico de colunas duplas
        for i, col in enumerate(colunas_duplas):
            plt.bar([pos + i * largura for pos in posicoes], df[col], largura, label=col)

        # Configurar rótulos das categorias no eixo x
        plt.xticks([pos + (len(colunas_duplas) - 1) * largura / 2 for pos in posicoes], df['NU_ANO'])

        # Limitar o eixo y a divisões igualmente espaçadas a partir do zero
        plt.yticks(np.arange(0, proximo_multiplo_10 + 1, intervalo_fixo))

        # Rotular os eixos
        plt.xlabel('anos')
        plt.ylabel('Valores')

        # Adicionar legenda
        plt.legend()
        plt.title(título)


        # Mostrar o gráfico
        plt.show()

    except ValueError as e:
        print(f"Erro ao gerar o gráfico: {str(e)}")



# Função para visualizar a distribuição das notas
def visualizar_distribuicao_notas(df, coluna_nota):
    '''
    Plota um gráfico de distribuição das notas de um determinado ano.

    Parameters
    ----------
    df : pd.DataFrame
        
    coluna_nota : str
        Nome da coluna de notas a ser visualizada.

    Returns
    -------
    None.

    '''
   
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[coluna_nota], kde=True)
        plt.title(f'Distribuição das Notas - {coluna_nota}')
        plt.xlabel(coluna_nota)
        plt.ylabel('Frequência')
        plt.show()
        
    except Exception as e:
        print(f"Erro ao visualizar a distribuição de notas: {str(e)}")



def graf_bar_par(df : pd.DataFrame, coluna_x : str, coluna_y : list, title : str, xlabel : str, ylabel : str):
    '''
    Recebe um DataFrame, nome e lista com colunas e retorna um gráfico
    
    Parâmetros
    ----------
    df : pd.DataFrame
    
    coluna_x : str
        Coluna que dita os objetos analisados
    
    colunas_y : list
        Lista com o nome das colunas do dataframe
    
    title : str
    
    xlabel : str

    ylabel : str
    
    Returns
    -------
    None.

    '''

    try:
        # Verifica se a coluna_x está presente no DataFrame
        if coluna_x not in df.columns:
            raise KeyError(f"A coluna {coluna_x} não foi encontrada no DataFrame dado.")

        # Verifica se todas as colunas em coluna_y estão presentes no DataFrame
        for y_column in coluna_y:
            if y_column not in df.columns:
                raise KeyError(f"A coluna {y_column} não foi encontrada no DataFrame dado.")

        categorias = df[coluna_x]
        bar_width = 0.35
        posicoes = np.arange(len(categorias))
        plt.figure(figsize=(10, 6))

        for i, y_column in enumerate(coluna_y):
            offset = i * bar_width
            plt.bar(posicoes + offset, df[y_column], width=bar_width, label=y_column)

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(posicoes + bar_width * (len(coluna_y) - 1) / 2, categorias)
        plt.legend()
        plt.grid(True)
        plt.show()
    
    except KeyError as e:
        print(f"Erro: {e}")
        

