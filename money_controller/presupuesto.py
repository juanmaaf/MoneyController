from money_controller.gasto import Gasto
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from categoriaGasto import CategoriaGasto

@dataclass
class Presupuesto:
    monto_total: float
    gastos_fijos: List[Gasto] = field(default_factory=list)
    gastos_variables: List[Gasto] = field(default_factory=list)
    ingresos: List[float] = field(default_factory=list)
    gasto_no_planificado: Optional[float] = None
    
    def __post_init__(self):
        self.gastos_fijos = [gasto for gasto in self.gastos_fijos if isinstance(gasto, Gasto)]
        self.gastos_variables = [gasto for gasto in self.gastos_variables if isinstance(gasto, Gasto)]
    
def leer_archivo_csv(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                raise ValueError("El archivo está vacío.")
            return lineas
    except FileNotFoundError:
        raise ValueError(f"El archivo {ruta_archivo} no existe")
    except ValueError as e:
        raise e
    except Exception as e:
        raise RuntimeError(f"Error al leer el archivo: {e}")