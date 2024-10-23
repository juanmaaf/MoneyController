from src.gasto import Gasto 

class Presupuesto:
    def __init__(self, monto_total):
        """
        Inicializa un objeto Presupuesto con un monto total (el presupuesto).
        
        :param monto_total: El presupuesto total mensual.
        """
        self.monto_total = monto_total  # El presupuesto total disponible
        self.gastos = []  # Lista vacía que almacenará todos los gastos

    def agregar_gasto(self, gasto):
        """
        Agrega un objeto Gasto a la lista de gastos del presupuesto.
        :param gasto: Un objeto de tipo Gasto.
        """
        self.gastos.append(gasto)

    def calcular_ahorros(self):
        """
        Calcula los ahorros disponibles restando los gastos del presupuesto total.
        :return: El valor de los ahorros disponibles.
        """
        total_gastos = sum(gasto.monto for gasto in self.gastos)  # Suma todos los montos de los gastos
        ahorros = self.monto_total - total_gastos  # Calcula los ahorros (presupuesto - gastos)
        return ahorros

    def es_gasto_adicional_viable(self, monto_adicional):
        """
        Verifica si un gasto adicional se puede realizar sin exceder el presupuesto.
        :param monto_adicional: El monto del gasto adicional.
        :return: True si es posible realizar el gasto sin exceder el presupuesto, False en caso contrario.
        """
        total_gastos = sum(gasto.monto for gasto in self.gastos)  # Suma los montos de todos los gastos
        nuevo_total = total_gastos + monto_adicional  # Nuevo total con el gasto adicional
        if nuevo_total <= self.monto_total:
            print(f"El gasto adicional de {monto_adicional} es viable. Presupuesto restante: {self.monto_total - nuevo_total}")
            return True
        else:
            print(f"El gasto adicional de {monto_adicional} NO es viable. Excederá el presupuesto por {nuevo_total - self.monto_total}")
            return False

    def calcular_gastos_por_tipo(self):
        """
        Retorna la suma de los gastos fijos y variables por separado.
        :return: Tuple (total_fijo, total_variable)
        """
        total_fijo = sum(gasto.monto for gasto in self.gastos if gasto.es_fijo())
        total_variable = sum(gasto.monto for gasto in self.gastos if gasto.es_variable())
        return total_fijo, total_variable

    def mostrar_gastos(self):
        """
        Muestra una lista detallada de todos los gastos con la descripción, el tipo y el monto.
        """
        for gasto in self.gastos:
            tipo = "Fijo" if gasto.es_fijo() else "Variable"
            print(f"Descripción: {gasto.descripcion}, Tipo: {tipo}, Monto: {gasto.monto}")
