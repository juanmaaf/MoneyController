#¿Cómo podemos categorizar los gastos en fijos y variables?
#[HU1]

class Gasto:
    def __init__(self, descripcion, monto, fijo=True):

        if monto <= 0:
            raise ValueError("El monto del gasto debe ser un valor positivo")
        
        self.descripcion = descripcion
        self.monto = monto
        self.fijo = fijo
