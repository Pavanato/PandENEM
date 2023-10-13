import unittest
import analise
import pandas as pd

class TestAnalise(unittest.TestCase):
#FUNÇÃO MÉDIA  
    def test_valores(self):
        data = {'NU_NOTA_CN': [70, 80, 90], 'NU_NOTA_CH': [75, 85, 95], 'NU_NOTA_LC': [72, 82, 92], 'NU_NOTA_MT': [68, 78, 88], 'NU_NOTA_REDACAO': [80, 85, 90]}
        df = pd.DataFrame(data)

        resultado = analise.media(df)
        self.assertEqual(resultado, 82.0)

    def test_raises(self):
        data = {'NU_NOTA_CH': [75, 85, 95], 'NU_NOTA_LC': [72, 82, 92], 'NU_NOTA_MT': [68, 78, 88], 'NU_NOTA_REDACAO': [80, 85, 90]}
        df = pd.DataFrame(data)        
        with self.assertRaises(ValueError):
            analise.media(df)

#FUNÇÃO SEPARAR_UFS
    def test_raises_coluna_nao_existe(self):
        data ={'Nota': [70, 80, 90, 85, 95]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.separar_ufs(df, ["RJ, SP"])

    def test_estado_nao_existe(self):
        data = {'Nota': [70,80,90,85,95], 'SG_UF_PROVA': ['RJ','RJ','SP','CE','BA']}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.separar_ufs(df, ['PP', 'DD'])


#FUNÇÃO SEPARAR_REGIAO
    def test_raises_regiao_invalida(self):
        data = {'CO_UF_PROVA': ['AM', 'SP', 'BA', 'SC', 'GO', 'RS'], 'OutrosDados': [1, 2, 3, 4, 5, 6]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.separar_regiao(df, 'Leste')
    
    def test_raises_coluna_nao_existe(self):
        data = {'estados': ['AM', 'SP', 'BA', 'SC', 'GO', 'RS'], 'OutrosDados': [1, 2, 3, 4, 5, 6]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.separar_regiao(df, "nordeste")

#FUNÇAÕ NOTA_1000_ANO
    def test_raises_coluna_redacao_nao_existe(self):
        data = {"NU_ANO": [2020,2020,2021]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.nota_1000_ano(df, [2020])

    def test_raises_coluna_ano_nao_existe(self):       
        data = {"NU_NOTA_REDACAO": [770,900,1000]}
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            analise.nota_1000_ano(df, [2020])


if __name__ == "__main__":
    unittest.main(verbosity = 3)