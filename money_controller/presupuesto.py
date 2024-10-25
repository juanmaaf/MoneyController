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
    
    def agregar_ingreso(self, ingreso):
        self.ingresos.append(ingreso)
        print(f"Ingreso agregado: {ingreso.descripcion}, Monto: {ingreso.monto}")
    
    def agregar_gasto(self, gasto):
        if self.validar_gasto(gasto):
            self.gastos.append(gasto)
            tipo = "Fijo" if gasto.es_fijo() else "Variable"
            print(f"Gasto agregado: {gasto.descripcion}, Tipo: {tipo}, Monto: {gasto.monto}")
        else:
            print(f"No puedes realizar el gasto: {gasto.descripcion}, Monto: {gasto.monto}")
    
    def validar_gasto(self, gasto):
        total_gastos = sum(g.monto for g in self.gastos)
        total_ingresos = sum(i.monto for i in self.ingresos)
        saldo_disponible = total_ingresos - total_gastos
        if saldo_disponible >= gasto.monto:
            return True
        return False
    
    def mostrar_presupuesto(self):
        total_gastos = sum(g.monto for g in self.gastos)
        total_ingresos = sum(i.monto for i in self.ingresos)
        saldo_disponible = total_ingresos - total_gastos
        print(f"Total ingresos: {total_ingresos}")
        print(f"Total gastado: {total_gastos}")
        print(f"Presupuesto restante: {saldo_disponible}")
