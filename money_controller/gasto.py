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
        categoria (CategoriaGasto): La categoría del gasto, fija o variable.
        fecha (datetime): La fecha registrada del gasto
    """
    descripcion: str
    monto: float
    categoria: CategoriaGasto = CategoriaGasto
    fecha: datetime
    
    def __post_init__(self):
        if isinstance(self.fecha, str):
            try:
                self.fecha = datetime.strptime(self.fecha, '%Y-%m-%d')
            except ValueError:
                raise ValueError(f"La fecha {self.fecha} no está en el formato correcto (YYYY-MM-DD).")