from dataclasses import dataclass
from money_controller.categoriaGasto import CategoriaGasto
from datetime import datetime

@dataclass
class Gasto:
    """
    Representa un gasto en el presupuesto mensual.

    Atributos:
        descripcion (str): La descripción del gasto.
        monto (float): La cantidad del gasto.
        fecha (datetime): La fecha registrada del gasto
        categoria (CategoriaGasto): La categoría del gasto, fija o variable.
    """
    descripcion: str
    monto: float
    fecha: datetime
    categoria: CategoriaGasto = CategoriaGasto
    
    def __post_init__(self):
        if isinstance(self.fecha, str):
            try:
                self.fecha = datetime.strptime(self.fecha, '%Y-%m-%d')
            except ValueError:
                raise ValueError(f"La fecha {self.fecha} no está en el formato correcto (YYYY-MM-DD).")