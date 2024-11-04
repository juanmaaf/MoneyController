from money_controller.gasto import Gasto
from dataclasses import dataclass, field
from typing import List

@dataclass
class Presupuesto:
    """
    Representa el presupuesto mensual, que incluye tanto los gastos como los ingresos.

    Atributos:
        monto_total (float): El presupuesto total mensual.
        gastos (List[Gasto]): Lista de gastos realizados.
        ingresos (List[float]): Lista de ingresos.
    """
    monto_total: float
    gastos: List[Gasto] = field(default_factory=list)
    ingresos: List[float] = field(default_factory=list)
