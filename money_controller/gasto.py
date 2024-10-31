#¿Cómo podemos categorizar los gastos en fijos y variables?
#[HU1]

# money_controller/gasto.py
from dataclasses import dataclass

@dataclass
class Gasto:
    descripcion: str  # La descrizione della spesa
    monto: float      # L'importo della spesa
    fijo: bool = True # True per spese fisse, False per variabili