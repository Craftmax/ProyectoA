# test_main_module.py

import unittest
from unittest.mock import patch
from main import user_input, main
from io import StringIO

class TestMainModule(unittest.TestCase):

    @patch('builtins.input', return_value='John')
    def test_user_input(self, mock_input):
        result = user_input()
        self.assertEqual(result, 'John')

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value='John')
    def test_main(self, mock_input, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()

        # Verifica que el saludo se imprima correctamente
        self.assertIn("Bienvenido al ProyectoA", output)
        self.assertIn("Hola, John.", output)

        # Puedes agregar más aserciones según la salida esperada en la consola

if __name__ == '__main__':
    unittest.main()