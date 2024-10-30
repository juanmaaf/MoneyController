#¿Cómo podemos calcular los ahorros disponibles cada mes?
#[HU1]
#¿Cómo podemos evaluar si un gasto adicional es viable? 
#[HU2]
from money_controller.gasto import Gasto

class Presupuesto:
    def __init__(self, monto_total):
        self.monto_total = monto_total
        self.gastos = []
        self.ingresos = []
