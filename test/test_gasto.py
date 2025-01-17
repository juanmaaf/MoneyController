import unittest
from unittest.mock import mock_open, patch
from datetime import datetime
from money_controller import presupuesto
from money_controller.gasto import Gasto
from money_controller.categoriaGasto import CategoriaGasto

INGRESO_1 = 1000
INGRESO_2 = 500
INGRESO_3 = 3000
INGRESO_4 = 200
ALQUILER_IMPORTE = 226.67
COMIDA_IMPORTE = 50
FECHA_ALQUILER = datetime(2024, 1, 1)
FECHA_COMIDA = datetime(2024, 1, 1)
FECHA_ALQUILER_2 = datetime(2024, 1, 2)
META_AHORRO = 500
GASTO_ADICIONAL = 100

class TestGasto(unittest.TestCase):
    def test_leer_archivo_correcto(self):
        contenido = """Fecha,Concepto,Importe,Tipo Movimiento
        2024-01-01,Alquiler,226.67,Gasto
        2024-01-01,Gimnasio,25,Gasto"""
        
        with patch("builtins.open", mock_open(read_data=contenido)):
            resultado = presupuesto.leer_archivo_csv("archivo_correcto.csv")
            self.assertEqual(len(resultado), 3)
            self.assertEqual(resultado[0].strip(), "Fecha,Concepto,Importe,Tipo Movimiento")
            self.assertEqual(resultado[1].strip(), "2024-01-01,Alquiler,226.67,Gasto")
            self.assertEqual(resultado[2].strip(), "2024-01-01,Gimnasio,25,Gasto")
    
    def test_procesar_gasto_variable(self):
        presupuesto_test = presupuesto.Presupuesto(monto_total=0)
        gastos_vistos = {}
        gasto_variable_convertido = {}
    
        presupuesto.procesar_gasto(presupuesto_test, gasto_variable_convertido, gastos_vistos, "Alquiler", ALQUILER_IMPORTE, FECHA_ALQUILER)
        
        self.assertEqual(len(presupuesto_test.gastos_variables), 1)
        self.assertEqual(presupuesto_test.gastos_variables[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto_test.gastos_variables[0].categoria, CategoriaGasto.VARIABLE)
    
    def test_procesar_gasto_fijo(self):
        presupuesto_test = presupuesto.Presupuesto(monto_total=0)
        gastos_vistos = {}
        gasto_variable_convertido = {}

        presupuesto.procesar_gasto(presupuesto_test, gasto_variable_convertido, gastos_vistos, "Alquiler", ALQUILER_IMPORTE, FECHA_ALQUILER)
        presupuesto.procesar_gasto(presupuesto_test, gasto_variable_convertido, gastos_vistos, "Alquiler", ALQUILER_IMPORTE, FECHA_ALQUILER_2)

        self.assertEqual(len(presupuesto_test.gastos_fijos), 2)
        self.assertEqual(presupuesto_test.gastos_fijos[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto_test.gastos_fijos[0].categoria, CategoriaGasto.FIJO)
        self.assertEqual(presupuesto_test.gastos_fijos[0].fecha, FECHA_ALQUILER_2)

        self.assertEqual(presupuesto_test.gastos_fijos[1].descripcion, "Alquiler")
        self.assertEqual(presupuesto_test.gastos_fijos[1].categoria, CategoriaGasto.FIJO)
        self.assertEqual(presupuesto_test.gastos_fijos[1].fecha, FECHA_ALQUILER)

        self.assertEqual(len(presupuesto_test.gastos_variables), 0)
        
    def test_procesar_atributos_correctos(self):
        fecha_str = "2024-01-01"
        importe_str = "226.67"
        
        fecha, importe = presupuesto.procesar_atributos(fecha_str, importe_str)
        
        self.assertEqual(fecha, FECHA_ALQUILER)
        self.assertEqual(importe, ALQUILER_IMPORTE)
    
    def test_procesar_atributos_importe_invalido(self):
        fecha_str = "2024-01-01"
        importe_str = "abc"
        
        with self.assertRaises(ValueError):
            presupuesto.procesar_atributos(fecha_str, importe_str)
    
    def test_procesar_atributos_fecha_invalida(self):
        fecha_str = "01-01-2024" 
        importe_str = "226.67"
        
        with self.assertRaises(ValueError): 
            presupuesto.procesar_atributos(fecha_str, importe_str)
    
    @patch("money_controller.presupuesto.leer_archivo_csv")
    def test_procesar_presupuesto_gasto_variable(self, mock_leer_archivo_csv):
        mock_leer_archivo_csv.return_value = [
            "Fecha,Concepto,Importe,Tipo Movimiento",
            "2024-01-01,Alquiler,226.67,Gasto"
        ]
        
        presupuesto_test = presupuesto.procesar_presupuesto("archivo.csv")
        
        self.assertEqual(len(presupuesto_test.gastos_variables), 1)
        self.assertEqual(presupuesto_test.gastos_variables[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto_test.gastos_variables[0].categoria, CategoriaGasto.VARIABLE)
    
    @patch("money_controller.presupuesto.leer_archivo_csv")
    def test_procesar_presupuesto_gasto_repetido(self, mock_leer_archivo_csv):
        mock_leer_archivo_csv.return_value = [
            "Fecha,Concepto,Importe,Tipo Movimiento",
            "2024-01-01,Alquiler,226.67,Gasto",
            "2024-01-02,Alquiler,226.67,Gasto"
        ]
        
        presupuesto_test = presupuesto.procesar_presupuesto("archivo.csv")
        
        self.assertEqual(len(presupuesto_test.gastos_fijos), 2)
        self.assertEqual(presupuesto_test.gastos_fijos[0].descripcion, "Alquiler")
        self.assertEqual(presupuesto_test.gastos_fijos[0].categoria, CategoriaGasto.FIJO)
        
        self.assertEqual(presupuesto_test.gastos_fijos[1].descripcion, "Alquiler")
        self.assertEqual(presupuesto_test.gastos_fijos[1].categoria, CategoriaGasto.FIJO)
        self.assertEqual(len(presupuesto_test.gastos_variables), 0)
    
    @patch('money_controller.presupuesto.leer_archivo_csv')
    def test_procesar_presupuesto_ingresos_y_gastos(self, mock_leer_archivo_csv):
        mock_leer_archivo_csv.return_value = [
            "Fecha,Concepto,Importe,Tipo Movimiento",
            "2024-01-01,Alquiler,226.67,Gasto",
            "2024-01-01,Gimnasio,25,Gasto",
            "2024-01-01,Sueldo,3000,Ingreso",
            "2024-01-02,Alquiler,226.67,Gasto"
        ]
        
        presupuesto_test = presupuesto.procesar_presupuesto("archivo.csv")
    
        self.assertEqual(presupuesto_test.ingresos, [3000])
        self.assertEqual(len(presupuesto_test.gastos_fijos), 2)
        self.assertEqual(len(presupuesto_test.gastos_variables), 1)
        
        total_gastos = sum(gasto.monto for gasto in presupuesto_test.gastos_fijos) + sum(gasto.monto for gasto in presupuesto_test.gastos_variables)
        self.assertEqual(presupuesto_test.monto_total, sum(presupuesto_test.ingresos) - total_gastos)
        
    def test_puede_permitirse_gasto_adicional(self):
        presupuesto_test = presupuesto.Presupuesto(monto_total=0)
        presupuesto_test.ingresos = [INGRESO_3, INGRESO_2]
        presupuesto_test.gastos_fijos = [Gasto(descripcion="Alquiler", monto=ALQUILER_IMPORTE, fecha=FECHA_ALQUILER,  categoria=CategoriaGasto.FIJO)]
        presupuesto_test.gastos_variables = [Gasto(descripcion="Comida", monto=COMIDA_IMPORTE, fecha=FECHA_COMIDA, categoria=CategoriaGasto.VARIABLE)]
        presupuesto_test.meta_ahorro =META_AHORRO
        
        presupuesto.actualizar_monto_total(presupuesto_test)
        
        gasto_adicional = GASTO_ADICIONAL
        puede_permitirse = presupuesto.puede_permitirse_gasto_adicional(presupuesto_test, gasto_adicional)
        
        self.assertTrue(puede_permitirse)
        self.assertEqual(presupuesto_test.gasto_no_planificado, GASTO_ADICIONAL)
        
    def test_no_permitir_gasto_adicional(self):
        presupuesto_test = presupuesto.Presupuesto(monto_total=0)
        presupuesto_test.ingresos = [INGRESO_4, INGRESO_4]
        presupuesto_test.gastos_fijos = [Gasto(descripcion="Alquiler", monto=ALQUILER_IMPORTE, fecha=FECHA_ALQUILER,  categoria=CategoriaGasto.FIJO)]
        presupuesto_test.gastos_variables = [Gasto(descripcion="Comida", monto=COMIDA_IMPORTE, fecha=FECHA_COMIDA, categoria=CategoriaGasto.VARIABLE)]
        presupuesto_test.meta_ahorro = META_AHORRO
        
        presupuesto.actualizar_monto_total(presupuesto_test)

        gasto_adicional = GASTO_ADICIONAL
        puede_permitirse = presupuesto.puede_permitirse_gasto_adicional(presupuesto_test, gasto_adicional)
        
        self.assertFalse(puede_permitirse)
        self.assertIsNone(presupuesto_test.gasto_no_planificado)

if __name__ == "__main__":
    unittest.main()  