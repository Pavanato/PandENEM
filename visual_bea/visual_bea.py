import matplotlib.pyplot as plt

def grafico_barra(df, coluna_x, coluna_y, titulo, xlabel, ylabel):
    
    '''
        Parameters
    ----------
    df : pd.DataFrame 
        arquivo usado.
    coluna_x : str
        eixo x.
    coluna_y : str
        eixo y.
    titulo : str
        tìtulo do gráfico.
    xlabel : str
        nome do eixo x.
    ylabel : str
        nome do eixo y.

    Raises
    ------
    KeyError
        caso as chaves não sejam encontradas no DataFrame

    Returns
    -------
    None.

    '''
    try:
        # Verifica se as colunas especificadas existem no DataFrame
        if coluna_x not in df.columns or coluna_y not in df.columns:
            raise KeyError("As colunas especificadas não existem no DataFrame.")

        # Extração dos dados do DataFrame
        x_data = df[coluna_x]
        y_data = df[coluna_y]

        # detalhes do gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(x_data, y_data, color='skyblue')
        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        # Rotaciona os rótulos do eixo x para melhor legibilidade, se necessário
        plt.xticks(rotation=45)

        # Exibe o gráfico
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Erro ao criar o gráfico de barras: {str(e)}")