#¿Cómo podemos calcular los ahorros disponibles cada mes?
#[HU1]
#¿Cómo podemos evaluar si un gasto adicional es viable? 
# money_controller/presupuesto.py
from money_controller.gasto import Gasto
from dataclasses import dataclass, field
from typing import List

@dataclass
class Presupuesto:

    monto_total: float                                   # Budget totale mensile
    gastos: List[Gasto] = field(default_factory=list)    # Lista di spese
    ingresos: List[float] = field(default_factory=list)  # Lista di entrate
