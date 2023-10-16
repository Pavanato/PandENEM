import unittest
import pandas as pd
import filter

class TestFilter(unittest.TestCase):

    def test_checa_entradas_value_error(self):
        data = {
            'Coluna1': ['A', 'B', 'C', 'D'],
            'Coluna2': [1.5, 2.0, 3.7, 999.9]
        }
        df = pd.DataFrame(data)
        
        column_entry_dict = {
            'Coluna1': ['A', 'B', 'C', 'D'],
            'Coluna2': "InvalidRange"
        }
        
        with self.assertRaises(ValueError):
            filter.checa_entradas(df, column_entry_dict)

    def test_checa_entradas_invalid_entries(self):
        data = {'Coluna1': ['A', 'B', 'C', 'X', 'E'], 'Coluna2': [1.5, 2.0, 3.7, 999.9, 5.5]}
        df = pd.DataFrame(data)
        entradas_validas = {'Coluna1': ['A', 'B', 'C', 'D'], 'Coluna2': (0.0, 1000.0)}
        with self.assertRaises(filter.InvalidEntryError) as context:
            filter.checa_entradas(df, entradas_validas)
        self.assertEqual(str(context.exception), "Entradas inválidas encontradas na coluna 'Coluna1': ['X', 'E']")

if __name__ == '__main__':
    unittest.main()
