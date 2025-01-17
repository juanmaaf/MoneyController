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
    @patch("builtins.open", new_callable=mock_open, read_data="""Fecha,Concepto,Importe,Tipo Movimiento
        2024-01-01,Alquiler,226.67,Gasto
        2024-01-01,Gimnasio,25,Gasto""")
    def test_leer_archivo_correcto(self, mock_file):
        resultado = presupuesto.leer_archivo_csv("archivo_correcto.csv")
        esperado = [
            "Fecha,Concepto,Importe,Tipo Movimiento",
            "2024-01-01,Alquiler,226.67,Gasto",
            "2024-01-01,Gimnasio,25,Gasto"
        ]
        self.assertEqual(len(resultado), len(esperado))
        resultado_limpio = [line.strip() for line in resultado]
        esperado_limpio = [line.strip() for line in esperado]
        self.assertListEqual(resultado_limpio, esperado_limpio)
    
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
        
    def test_procesar_atributos(self):
        casos = [
            {"fecha_str": "2024-01-01", "importe_str": "226.67", "esperado": (FECHA_ALQUILER, ALQUILER_IMPORTE)},
            {"fecha_str": "2024-01-01", "importe_str": "abc", "espera_error": ValueError},
            {"fecha_str": "01-01-2024", "importe_str": "226.67", "espera_error": ValueError},
        ]
        for caso in casos:
            with self.subTest(caso=caso):
                if "espera_error" in caso:
                    with self.assertRaises(caso["espera_error"]):
                        presupuesto.procesar_atributos(caso["fecha_str"], caso["importe_str"])
                else:
                    resultado = presupuesto.procesar_atributos(caso["fecha_str"], caso["importe_str"])
                    self.assertEqual(resultado, caso["esperado"])
    
    @patch("money_controller.presupuesto.leer_archivo_csv")
    def test_procesar_presupuesto(self, mock_leer_archivo_csv):
        casos = [
            {
                "input": [
                    "Fecha,Concepto,Importe,Tipo Movimiento",
                    "2024-01-01,Alquiler,226.67,Gasto"
                ],
                "fijos_esperados": 0,
                "variables_esperados": 1,
                "ingresos_esperados": [],
            },
            {
                "input": [
                    "Fecha,Concepto,Importe,Tipo Movimiento",
                    "2024-01-01,Alquiler,226.67,Gasto",
                    "2024-01-02,Alquiler,226.67,Gasto"
                ],
                "fijos_esperados": 2,
                "variables_esperados": 0,
                "ingresos_esperados": [],
            },
            {
                "input": [
                    "Fecha,Concepto,Importe,Tipo Movimiento",
                    "2024-01-01,Sueldo,3000,Ingreso",
                    "2024-01-01,Alquiler,226.67,Gasto",
                    "2024-01-02,Alquiler,226.67,Gasto"
                ],
                "fijos_esperados": 2,
                "variables_esperados": 0,
                "ingresos_esperados": [INGRESO_3],
            },
        ]

        for caso in casos:
            with self.subTest(caso=caso):
                mock_leer_archivo_csv.return_value = caso["input"]
                presupuesto_test = presupuesto.procesar_presupuesto("archivo.csv")

                self.assertEqual(len(presupuesto_test.gastos_fijos), caso["fijos_esperados"])
                self.assertEqual(len(presupuesto_test.gastos_variables), caso["variables_esperados"])
                self.assertEqual(presupuesto_test.ingresos, caso["ingresos_esperados"])
        
    def test_puede_permitirse_gasto_adicional(self):
        casos = [
            {
                "ingresos": [INGRESO_3, INGRESO_2],
                "fijos": [Gasto(descripcion="Alquiler", monto=ALQUILER_IMPORTE, fecha=FECHA_ALQUILER, categoria=CategoriaGasto.FIJO)],
                "variables": [Gasto(descripcion="Comida", monto=COMIDA_IMPORTE, fecha=FECHA_COMIDA, categoria=CategoriaGasto.VARIABLE)],
                "meta_ahorro": META_AHORRO,
                "gasto_adicional": GASTO_ADICIONAL,
                "esperado": True,
                "gasto_no_planificado": GASTO_ADICIONAL,
            },
            {
                "ingresos": [INGRESO_4, INGRESO_4],
                "fijos": [Gasto(descripcion="Alquiler", monto=ALQUILER_IMPORTE, fecha=FECHA_ALQUILER, categoria=CategoriaGasto.FIJO)],
                "variables": [Gasto(descripcion="Comida", monto=COMIDA_IMPORTE, fecha=FECHA_COMIDA, categoria=CategoriaGasto.VARIABLE)],
                "meta_ahorro": META_AHORRO,
                "gasto_adicional": GASTO_ADICIONAL,
                "esperado": False,
                "gasto_no_planificado": None,
            },
        ]

        for caso in casos:
            with self.subTest(caso=caso):
                presupuesto_test = presupuesto.Presupuesto(monto_total=0)
                presupuesto_test.ingresos = caso["ingresos"]
                presupuesto_test.gastos_fijos = caso["fijos"]
                presupuesto_test.gastos_variables = caso["variables"]
                presupuesto_test.meta_ahorro = caso["meta_ahorro"]

                presupuesto.actualizar_monto_total(presupuesto_test)
                puede_permitirse = presupuesto.puede_permitirse_gasto_adicional(presupuesto_test, caso["gasto_adicional"])

                self.assertEqual(puede_permitirse, caso["esperado"])
                self.assertEqual(presupuesto_test.gasto_no_planificado, caso["gasto_no_planificado"])

if __name__ == "__main__":
    unittest.main()  