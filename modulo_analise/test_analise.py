import unittest
import analise
import pandas as pd

class TestAnalise(unittest.TestCase):

#   Função separar_ufs_e_anos
    def test_raises_ufs_invalidas(self):
        data = {'SG_UF_PROVA': ['SP', 'RJ', 'MG', 'SP', 'RJ'], 'NU_ANO': [2020, 2020, 2021, 2021, 2021], 'Nota': [70, 80, 90, 85, 95]}
        df = pd.DataFrame(data)
        estados_para_filtrar = ['SP', 'MG', 'BA']
        with self.assertRaises(ValueError):
            analise.separar_ufs_e_anos(df, estados_para_filtrar, [])
    
    def test_raises_anos_invalidos(self):
        data = {'SG_UF_PROVA': ['SP', 'RJ', 'MG', 'SP', 'RJ'], 'NU_ANO': [2020, 2020, 2021, 2021, 2021], 'Nota': [70, 80, 90, 85, 95]}
        df = pd.DataFrame(data)
        anos_para_filtrar = [2019, 2021]
        with self.assertRaises(ValueError):
            analise.separar_ufs_e_anos(df, [], anos_para_filtrar)


#   Função separar_região
    def test_raises_regiao_invalida(self):
        data = {'CO_UF_PROVA': ['AM', 'SP', 'BA', 'SC', 'GO', 'RS'], 'OutrosDados': [1, 2, 3, 4, 5, 6]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.separar_regiao(df, 'Leste')
    
    def test_raises_coluna_inexistente(self):
        data = {'estados': ['AM', 'SP', 'BA', 'SC', 'GO', 'RS'], 'OutrosDados': [1, 2, 3, 4, 5, 6]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.separar_regiao(df, "nordeste")


#   função media
    def test_raises_coluna_inexistente(self):
        data = {'NU_NOTA_CN': [75, 85, 90, 88, 92], 'NU_NOTA_CH': [80, 78, 92, 87, 88]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.media(df)


#   função nota_1000_ano
    def test_raises_coluna_inexistente(self):
        data = {'NU_ANO': [2020, 2020, 2020, 2021, 2021]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.nota_1000_ano(df, [2020, 2021])


#   função renda_media_per_capita_familiar
    def test_raises_tipo_errado(self):
        data = {'Q006': ['A', 'B', 'C', 'D'], 'Q005': ['1', '2', '3', '4'], 'Outra_Coluna': ['X', 'Y', 'Z', 'W']}
        df = pd.DataFrame(data)
        colunas_extras = ['Outra_Coluna']
        with self.assertRaises(TypeError):
            analise.renda_media_per_capita_familiar(df, colunas_extras)
        
    def test_raises_Q006_Q005_inexistente(self):
        data = {'Q005': [1, 2, 3, 4], 'Outra_Coluna': ['X', 'Y', 'Z', 'W']}
        df = pd.DataFrame(data)
        colunas_extras = ['Outra_Coluna']
        with self.assertRaises(ValueError):
            analise.renda_media_per_capita_familiar(df, colunas_extras)


#   função nota_unificada_por_estado_e_ano
    def test_raises_tipo_errado_de_valores(self):
        data = {'SG_UF_PROVA': ['MG', 'SP', 'RJ', 'MG', 'SP', 'MG'], 'NU_ANO': [2020, 2020, 2021, 2021, 2021, 2021], 'media': ['80', '85', '90', '78', '88', '92']}
        df = pd.DataFrame(data)
        with self.assertRaises(TypeError):
            analise.nota_unificada_por_estado_e_ano(df)
    
    def test_nota_unificada_por_estado_e_ano_coluna_faltante(self):
        data = {'SG_UF_PROVA': ['MG', 'SP', 'RJ', 'MG', 'SP', 'MG'], 'NU_ANO': [2020, 2020, 2021, 2021, 2021, 2021]}
        df = pd.DataFrame(data)
        with self.assertRaises(KeyError):
            analise.nota_unificada_por_estado_e_ano(df)


#   função renda_unificada_por_estado
    def test_raises_tipo_errado(self):
        data = {'SG_UF_PROVA': [1, 2, 1, 2], 'Renda_Per_Capita': ['500', '600', '700', '800'], 'Outra_Coluna': [10, 20, 30, 40]}
        df = pd.DataFrame(data)
        with self.assertRaises(TypeError):
            analise.renda_unificada_por_estado(df)

    def test_raises_coluna_inexistente(self):
        data = {'SG_UF_PROVA': [1, 2, 1, 2], 'Outra_Coluna': [10, 20, 30, 40]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.renda_unificada_por_estado(df)
            

#   função media_internet
    def test_raises_tipo_errado(self):
        data = {'SG_UF_PROVA': [1, 2, 1, 2], 'Renda_Per_Capita': ['500', '600', '700', '800'], 'Outra_Coluna': [10, 20, 30, 40]}
        df = pd.DataFrame(data)
        with self.assertRaises(TypeError):
            analise.renda_unificada_por_estado(df)

    def test_renda_unificada_por_estado_coluna_faltante(self):
        data = {'SG_UF_PROVA': [1, 2, 1, 2], 'Outra_Coluna': [10, 20, 30, 40]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.renda_unificada_por_estado(df)


#   função calcular_medias_regiao_ano
    def test_calculo_medias(self):
        data = {'NU_ANO': [2021, 2021, 2022, 2022, 2023],
                'SG_UF_PROVA': ['SP', 'RJ', 'SP', 'RJ', 'SP'],
                'media': [7.5, 8.0, 7.8, 8.2, 7.9]}
        df = pd.DataFrame(data)
        resultado = analise.calcular_medias_regiao_ano(df)
        self.assertEqual(resultado.loc[2021, 'Sudeste'], 7.75)
        self.assertEqual(resultado.loc[2022, 'Sudeste'], 8.00)
        self.assertEqual(resultado.loc[2023, 'Sudeste'], 7.90)
        self.assertEqual(resultado.loc[2021, 'Média Brasil'], 7.75)
        self.assertEqual(resultado.loc[2022, 'Média Brasil'], 8.00)
        self.assertEqual(resultado.loc[2023, 'Média Brasil'], 7.90)

    def test_excecao_colunas_faltando(self):
        data = {'NU_ANO': [2021, 2021, 2022, 2022, 2023],
                'media': [7.5, 8.0, 7.8, 8.2, 7.9]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.calcular_medias_regiao_ano(df)

#   função calcular_media_regiao_ano
    def test_raises_coluna_inexistente(self):
        data = {'NU_ANO': [2021, 2021, 2022, 2022, 2023], 'SG_UF_PROVA': ['SP', 'RJ', 'SP', 'RJ', 'SP']}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.calcular_medias_regiao_ano(df)
            
            
if __name__ == "__main__":
    unittest.main()