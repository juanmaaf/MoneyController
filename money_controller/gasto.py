class Gasto:
    def __init__(self, descripcion, monto, fijo=True):
        self.descripcion = descripcion
        self.monto = monto
        self.fijo = fijo
    
    def es_fijo(self):
        return self.fijo
