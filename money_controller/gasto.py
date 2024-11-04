# money_controller/gasto.py
from dataclasses import dataclass

@dataclass
class Gasto:
    """
    Representa un gasto en el presupuesto mensual.

    Atributos:
        descripcion (str): La descripción del gasto.
        monto (float): La cantidad del gasto.
        fijo (bool): Indica si el gasto es fijo (True) o variable (False).
    """
    descripcion: str
    monto: float
    fijo: bool = True
