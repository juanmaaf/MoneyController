from dataclasses import dataclass
from money_controller.categoriaGasto import CategoriaGasto
from datetime import datetime

@dataclass
class Gasto:
    fecha: datetime
    concepto: str
    importe: float
    categoria: CategoriaGasto = CategoriaGasto

    def __post_init__(self):
        if isinstance(self.fecha, str):
            try:
                self.fecha = datetime.strptime(self.fecha, '%Y-%m-%d')
            except ValueError:
                raise ValueError(f"La fecha {self.fecha} no está en el formato correcto (YYYY-MM-DD).")