#¿Cómo podemos calcular los ahorros disponibles cada mes?
#[HU1]
#¿Cómo podemos evaluar si un gasto adicional es viable? 
#[HU2]
from money_controller.gasto import Gasto

class Presupuesto:
    def __init__(self, monto_total):

        if monto_total <= 0:
            raise ValueError("El presupuesto total debe ser un valor positivo")
        
        self.monto_total = monto_total
        self.gastos = []
        self.ingresos = []