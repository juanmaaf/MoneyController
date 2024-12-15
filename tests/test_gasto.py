import unittest
from unittest.mock import mock_open, patch
from money_controller.presupuesto import leer_archivo_csv

class TestGasto(unittest.TestCase):
    def test_leer_archivo_inexistente(self):
        ruta_archivo = "archivo_inexistente.csv"
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(ValueError) as contexto:
                leer_archivo_csv(ruta_archivo)
            self.assertEqual(str(contexto.exception), f"El archivo {ruta_archivo} no existe")

    def test_leer_archivo_vacio(self):
        with patch("builtins.open", mock_open(read_data="")):
            with self.assertRaises(ValueError) as contexto:
                leer_archivo_csv("archivo_vacio.csv")
            self.assertEqual(str(contexto.exception), "El archivo está vacío.")
        
    def test_leer_archivo_correcto(self):
        contenido = """Fecha,Concepto,Categoría,Importe,Tipo Movimiento
        2024-01-01,Alquiler,Vivienda,226.67,Gasto
        2024-01-01,Gimnasio,Ocio,25,Gasto"""
        
        with patch("builtins.open", mock_open(read_data=contenido)):
            resultado = leer_archivo_csv("archivo_correcto.csv")
            self.assertEqual(len(resultado), 3)
            self.assertEqual(resultado[0].strip(), "Fecha,Concepto,Categoría,Importe,Tipo Movimiento")
            self.assertEqual(resultado[1].strip(), "2024-01-01,Alquiler,Vivienda,226.67,Gasto")
            self.assertEqual(resultado[2].strip(), "2024-01-01,Gimnasio,Ocio,25,Gasto")
    
    def test_leer_archivo_error(self):
        ruta_archivo = "archivo_error.csv"
        with patch("builtins.open", side_effect=OSError("Error inesperado al abrir el archivo")):
            with self.assertRaises(RuntimeError) as contexto:
                leer_archivo_csv(ruta_archivo)
            self.assertEqual(str(contexto.exception), "Error al leer el archivo: Error inesperado al abrir el archivo")


if __name__ == "__main__":
    unittest.main()