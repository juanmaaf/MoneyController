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