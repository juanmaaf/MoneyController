import unittest
from unittest.mock import mock_open, patch
from datetime import datetime
from money_controller.presupuesto import leer_archivo_csv
from money_controller.presupuesto import Presupuesto
from money_controller.gasto import Gasto
from money_controller.categoriaGasto import CategoriaGasto
from money_controller.presupuesto import leer_archivo_csv
from money_controller.presupuesto import actualizar_monto_total
from money_controller.presupuesto import procesar_gasto
from money_controller.presupuesto import procesar_atributos
from money_controller.presupuesto import procesar_datos

INGRESO_1 = 1000
INGRESO_2 = 500
ALQUILER_IMPORTE = 226.67
COMIDA_IMPORTE = 50
FECHA_ALQUILER = datetime(2024, 1, 1)
FECHA_COMIDA = datetime(2024, 1, 1)
FECHA_ALQUILER_2 = datetime(2024, 1, 2)

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
    
    def test_actualizar_monto_total(self):
        presupuesto = Presupuesto(monto_total=0)
        presupuesto.ingresos = [INGRESO_1, INGRESO_2]
        presupuesto.gastos_fijos = [Gasto(descripcion="Alquiler", monto=ALQUILER_IMPORTE, categoria=CategoriaGasto.FIJO, fecha=FECHA_ALQUILER, )]
        presupuesto.gastos_variables = [Gasto(descripcion="Comida", monto=COMIDA_IMPORTE, categoria=CategoriaGasto.VARIABLE, fecha=FECHA_COMIDA)]
        
        actualizar_monto_total(presupuesto)
        
        self.assertEqual(presupuesto.monto_total, INGRESO_1 + INGRESO_2 - ALQUILER_IMPORTE - COMIDA_IMPORTE)
    
    def test_procesar_gasto_variable(self):
        presupuesto = Presupuesto(monto_total=0)
        gastos_vistos = {}
    
        procesar_gasto(presupuesto, gastos_vistos, "Alquiler", "Vivienda", ALQUILER_IMPORTE, FECHA_ALQUILER)
        
        self.assertEqual(len(presupuesto.gastos_variables), 1)
        self.assertEqual(presupuesto.gastos_variables[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto.gastos_variables[0].categoria, CategoriaGasto.VARIABLE)
    
    def test_procesar_gasto_fijo(self):
        presupuesto = Presupuesto(monto_total=0)
        gastos_vistos = {}

        procesar_gasto(presupuesto, gastos_vistos, "Alquiler", "Vivienda", ALQUILER_IMPORTE, FECHA_ALQUILER)
        procesar_gasto(presupuesto, gastos_vistos, "Alquiler", "Vivienda", ALQUILER_IMPORTE, FECHA_ALQUILER_2)

        self.assertEqual(len(presupuesto.gastos_fijos), 2)
        self.assertEqual(presupuesto.gastos_fijos[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto.gastos_fijos[0].categoria, CategoriaGasto.FIJO)
        self.assertEqual(presupuesto.gastos_fijos[0].fecha, FECHA_ALQUILER)

        self.assertEqual(presupuesto.gastos_fijos[1].descripcion, "Alquiler")
        self.assertEqual(presupuesto.gastos_fijos[1].categoria, CategoriaGasto.FIJO)
        self.assertEqual(presupuesto.gastos_fijos[1].fecha, FECHA_ALQUILER_2)

        self.assertEqual(len(presupuesto.gastos_variables), 0)
        
    def test_procesar_atributos_correctos(self):
        fecha_str = "2024-01-01"
        importe_str = "226.67"
        
        fecha, importe = procesar_atributos(fecha_str, importe_str)
        
        self.assertEqual(fecha, datetime(2024, 1, 1))
        self.assertEqual(importe, 226.67)
    
    def test_procesar_atributos_importe_invalido(self):
        fecha_str = "2024-01-01"
        importe_str = "abc"
        
        with self.assertRaises(ValueError):
            procesar_atributos(fecha_str, importe_str)
    
    def test_procesar_atributos_fecha_invalida(self):
        fecha_str = "01-01-2024" 
        importe_str = "226.67"
        
        with self.assertRaises(ValueError): 
            procesar_atributos(fecha_str, importe_str)
    
    @patch("money_controller.presupuesto.leer_archivo_csv")
    def test_procesar_datos_gasto_variable(self, mock_leer_archivo_csv):
        mock_leer_archivo_csv.return_value = [
            "Fecha,Concepto,Categoría,Importe,Tipo Movimiento",
            "2024-01-01,Alquiler,Vivienda,226.67,Gasto"
        ]
        
        presupuesto = procesar_datos("archivo.csv")
        
        self.assertEqual(len(presupuesto.gastos_variables), 1)
        self.assertEqual(presupuesto.gastos_variables[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto.gastos_variables[0].categoria, CategoriaGasto.VARIABLE)
    
    @patch("money_controller.presupuesto.leer_archivo_csv")
    def test_procesar_datos_gasto_repetido(self, mock_leer_archivo_csv):
        mock_leer_archivo_csv.return_value = [
            "Fecha,Concepto,Categoría,Importe,Tipo Movimiento",
            "2024-01-01,Alquiler,Vivienda,226.67,Gasto",
            "2024-01-02,Alquiler,Vivienda,226.67,Gasto"
        ]
        
        presupuesto = procesar_datos("archivo.csv")
        
        self.assertEqual(len(presupuesto.gastos_fijos), 2)
        self.assertEqual(presupuesto.gastos_fijos[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto.gastos_fijos[0].categoria, CategoriaGasto.FIJO)
        
        self.assertEqual(presupuesto.gastos_fijos[1].descripcion, "Alquiler")
        self.assertEqual(presupuesto.gastos_fijos[1].categoria, CategoriaGasto.FIJO)
        self.assertEqual(len(presupuesto.gastos_variables), 0)
    
    @patch('money_controller.presupuesto.leer_archivo_csv')
    def test_procesar_datos_ingresos_y_gastos(self, mock_leer_archivo_csv):
        mock_leer_archivo_csv.return_value = [
            "Fecha,Concepto,Categoría,Importe,Tipo Movimiento",
            "2024-01-01,Alquiler,Vivienda,226.67,Gasto",
            "2024-01-01,Gimnasio,Ocio,25,Gasto",
            "2024-01-01,Sueldo,Trabajo,3000,Ingreso",
            "2024-01-02,Alquiler,Vivienda,226.67,Gasto"
        ]
        
        presupuesto = procesar_datos("archivo.csv")
    
        self.assertEqual(presupuesto.ingresos, [3000])
        self.assertEqual(len(presupuesto.gastos_fijos), 2)
        self.assertEqual(len(presupuesto.gastos_variables), 1)
        
        total_gastos = sum(gasto.monto for gasto in presupuesto.gastos_fijos) + sum(gasto.monto for gasto in presupuesto.gastos_variables)
        self.assertEqual(presupuesto.monto_total, sum(presupuesto.ingresos) - total_gastos)

if __name__ == "__main__":
    unittest.main()  