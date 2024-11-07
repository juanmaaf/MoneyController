from dataclasses import dataclass
from money_controller.categoriaGasto import CategoriaGasto
@dataclass
class Gasto:
    """
    Representa un gasto en el presupuesto mensual.

    Atributos:
        descripcion (str): La descripción del gasto.
        monto (float): La cantidad del gasto.
        categoria (CategoriaGasto): La categoría del gasto, fija o variable.
    """
    descripcion: str
    monto: float
    categoria: CategoriaGasto = CategoriaGasto
