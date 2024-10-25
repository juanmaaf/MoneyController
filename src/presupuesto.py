class Presupuesto:
    def __init__(self, monto_total):
        self.monto_total = monto_total
        self.gastos = []
    
    def agregar_gasto(self, gasto):
        if self.validar_gasto(gasto):
            self.gastos.append(gasto)
            tipo = "Fijo" if gasto.es_fijo() else "Variable"
            print(f"Gasto agregado: {gasto.descripcion}, Tipo: {tipo}, Monto: {gasto.monto}")
        else:
            print(f"No puedes realizar el gasto: {gasto.descripcion}, Monto: {gasto.monto}")
    
    def validar_gasto(self, gasto):
        total_gastos = sum(g.monto for g in self.gastos)
        if total_gastos + gasto.monto > self.monto_total:
            return False
        return True
    
    def mostrar_gastos(self):
        print("\nGastos actuales:")
        for gasto in self.gastos:
            tipo = "Fijo" if gasto.es_fijo() else "Variable"
            print(f"Descripción: {gasto.descripcion}, Tipo: {tipo}, Monto: {gasto.monto}")
        total_gastos = sum(g.monto for g in self.gastos)
        print(f"Total gastado: {total_gastos}, Presupuesto restante: {self.monto_total - total_gastos}")
