class Gasto:
    def __init__(self, descripcion, monto, tipo):
        """
        Inicializa un objeto Gasto con la descripción, el monto y el tipo (fijo o variable).
        
        :param descripcion: Descripción del gasto (ej. Alquiler, Internet)
        :param monto: Monto del gasto en formato numérico.
        :param tipo: Tipo de gasto - 'fijo' o 'variable'
        """
        self.descripcion = descripcion  # Descripción del gasto (ej. Alquiler)
        self.monto = monto  # Monto del gasto
        self.tipo = tipo  # Tipo de gasto: 'fijo' (fijo) o 'variable' (variable)
    
    def es_fijo(self):
        """
        Verifica si el gasto es de tipo fijo.
        :return: True si el tipo es 'fijo', False en caso contrario.
        """
        return self.tipo == 'fijo'
    
    def es_variable(self):
        """
        Verifica si el gasto es de tipo variable.
        :return: True si el tipo es 'variable', False en caso contrario.
        """
        return self.tipo == 'variable'
