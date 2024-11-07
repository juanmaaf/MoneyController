from money_controller.gasto import Gasto
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Presupuesto:
    
    """
    Representa el presupuesto mensual, que incluye tanto los gastos como los ingresos.

    Atributo:
        monto_total (float): El presupuesto total mensual.
        gastos_fijos (List[Gasto]): Lista de gastos fijos (ej. alquiler, internet).

        gastos_variables (List[Gasto]): Lista de gastos variables (ej.coomida, entretenimiento).

        ingresos (List[float]): Lista de ingresos.
        
    """
    monto_total: float
    gastos_fijos: List[Gasto] = field(default_factory=list)
    gastos_variables: List[Gasto] = field(default_factory=list)
    ingresos: List[float] = field(default_factory=list)
    gasto_no_planificado: Optional[float] = None