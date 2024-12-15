import unittest
from unittest.mock import mock_open, patch
from datetime import datetime 
from money_controller.presupuesto import Presupuesto
from money_controller.gasto import Gasto
from money_controller.categoriaGasto import CategoriaGasto
from money_controller.presupuesto import leer_archivo_csv
from money_controller.presupuesto import actualizar_monto_total
from money_controller.presupuesto import procesar_gasto
from money_controller.presupuesto import procesar_atributos
from money_controller.presupuesto import procesar_datos
from money_controller.presupuesto import puede_permitirse_gasto_adicional

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
        presupuesto.ingresos = [1000, 500]
        presupuesto.gastos_fijos = [Gasto(fecha=datetime(2024, 1, 1), concepto="Alquiler", importe=226.67, categoria=CategoriaGasto.FIJO)]
        presupuesto.gastos_variables = [Gasto(fecha=datetime(2024, 1, 1), concepto="Comida", importe=50, categoria=CategoriaGasto.VARIABLE)]
        
        actualizar_monto_total(presupuesto)
        
        self.assertEqual(presupuesto.monto_total, 1000 + 500 - 226.67 - 50)
    
    def test_procesar_gasto_variable(self):
        presupuesto = Presupuesto(monto_total=0)
        gastos_vistos = {}
    
        procesar_gasto(presupuesto, gastos_vistos, "Alquiler", "Vivienda", 226.67, datetime(2024, 1, 1))
        
        self.assertEqual(len(presupuesto.gastos_variables), 1)
        self.assertEqual(presupuesto.gastos_variables[0].concepto, "Alquiler")
        self.assertEqual(presupuesto.gastos_variables[0].categoria, CategoriaGasto.VARIABLE)
    
    def test_procesar_gasto_fijo(self):
        presupuesto = Presupuesto(monto_total=0)
        gastos_vistos = {}

        procesar_gasto(presupuesto, gastos_vistos, "Alquiler", "Vivienda", 226.67, datetime(2024, 1, 1))
        procesar_gasto(presupuesto, gastos_vistos, "Alquiler", "Vivienda", 226.67, datetime(2024, 1, 2))

        self.assertEqual(len(presupuesto.gastos_fijos), 2)
        self.assertEqual(presupuesto.gastos_fijos[0].concepto, "Alquiler")
        self.assertEqual(presupuesto.gastos_fijos[0].categoria, CategoriaGasto.FIJO)
        self.assertEqual(presupuesto.gastos_fijos[0].fecha, datetime(2024, 1, 1))

        self.assertEqual(presupuesto.gastos_fijos[1].concepto, "Alquiler")
        self.assertEqual(presupuesto.gastos_fijos[1].categoria, CategoriaGasto.FIJO)
        self.assertEqual(presupuesto.gastos_fijos[1].fecha, datetime(2024, 1, 2))

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
        self.assertEqual(presupuesto.gastos_variables[0].concepto, "Alquiler")
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
        self.assertEqual(presupuesto.gastos_fijos[0].concepto, "Alquiler")
        self.assertEqual(presupuesto.gastos_fijos[0].categoria, CategoriaGasto.FIJO)
        
        self.assertEqual(presupuesto.gastos_fijos[1].concepto, "Alquiler")
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
        
        total_gastos = sum(gasto.importe for gasto in presupuesto.gastos_fijos) + sum(gasto.importe for gasto in presupuesto.gastos_variables)
        self.assertEqual(presupuesto.monto_total, sum(presupuesto.ingresos) - total_gastos)
    
    def test_puede_permitirse_gasto_adicional(self):
        presupuesto = Presupuesto(monto_total=0)
        presupuesto.ingresos = [3000, 500]
        presupuesto.gastos_fijos = [Gasto(fecha=datetime(2024, 1, 1), concepto="Alquiler", importe=226.67, categoria=CategoriaGasto.FIJO)]
        presupuesto.gastos_variables = [Gasto(fecha=datetime(2024, 1, 1), concepto="Comida", importe=50, categoria=CategoriaGasto.VARIABLE)]
        presupuesto.meta_ahorro = 500
        
        actualizar_monto_total(presupuesto)
        
        gasto_adicional = 100
        puede_permitirse = puede_permitirse_gasto_adicional(presupuesto, gasto_adicional)
        
        self.assertTrue(puede_permitirse)
        self.assertEqual(presupuesto.gasto_no_planificado, 100)
        
    def test_no_permitir_gasto_adicional(self):
        presupuesto = Presupuesto(monto_total=0)
        presupuesto.ingresos = [1000, 200]
        presupuesto.gastos_fijos = [Gasto(fecha=datetime(2024, 1, 1), concepto="Alquiler", importe=800, categoria=CategoriaGasto.FIJO)]
        presupuesto.gastos_variables = [Gasto(fecha=datetime(2024, 1, 1), concepto="Comida", importe=300, categoria=CategoriaGasto.VARIABLE)]
        presupuesto.meta_ahorro = 500
        
        actualizar_monto_total(presupuesto)

        gasto_adicional = 100
        puede_permitirse = puede_permitirse_gasto_adicional(presupuesto, gasto_adicional)
        
        self.assertFalse(puede_permitirse)
        self.assertIsNone(presupuesto.gasto_no_planificado)

if __name__ == "__main__":
    unittest.main()