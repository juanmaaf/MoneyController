from money_controller.gasto import Gasto
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from money_controller.categoriaGasto import CategoriaGasto

@dataclass
class Presupuesto:
    
    """
    Representa el presupuesto mensual, que incluye tanto los gastos como los ingresos.

    Atributo:
        monto_total (float): El presupuesto total mensual.
        gastos_fijos (List[Gasto]): Lista de gastos fijos (ej. alquiler, internet).

        gastos_variables (List[Gasto]): Lista de gastos variables (ej.coomida, entretenimiento).

        ingresos (List[float]): Lista de ingresos.
        
        meta_ahorro (float): Ahorro deseado por el usuario
        
    """
    monto_total: float
    gastos_fijos: List[Gasto] = field(default_factory=list)
    gastos_variables: List[Gasto] = field(default_factory=list)
    ingresos: List[float] = field(default_factory=list)
    meta_ahorro: float = None
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
    
def procesar_atributos(fecha_str, monto_str):
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    monto = float(monto_str)
    return fecha, monto

def procesar_gasto(presupuesto, gastos_vistos, descripcion, categoria_str, monto, fecha):
    clave_gasto = (descripcion, categoria_str, monto)
    
    if clave_gasto in gastos_vistos:
        for gasto in presupuesto.gastos_variables:
            if gasto.descripcion == descripcion and gasto.monto == monto and gasto.categoria == CategoriaGasto.VARIABLE:
                gasto.categoria=CategoriaGasto.FIJO
                presupuesto.gastos_variables.remove(gasto)
                presupuesto.gastos_fijos.append(gasto)
        gasto = Gasto(descripcion=descripcion, monto=monto, fecha=fecha, categoria=CategoriaGasto.FIJO)
        presupuesto.gastos_fijos.append(gasto)
    else:
        gasto = Gasto(descripcion=descripcion, monto=monto, fecha=fecha, categoria=CategoriaGasto.VARIABLE)
        presupuesto.gastos_variables.append(gasto)
        gastos_vistos[clave_gasto] = True

def actualizar_monto_total(presupuesto):
    total_gastos = sum(gasto.monto for gasto in presupuesto.gastos_fijos) + sum(gasto.monto for gasto in presupuesto.gastos_variables)
    presupuesto.monto_total = sum(presupuesto.ingresos) - total_gastos

def procesar_datos(ruta_archivo):
    lineas = leer_archivo_csv(ruta_archivo)
    presupuesto = Presupuesto(monto_total=0)
    gastos_vistos = {}

    for i, linea in enumerate(lineas):
        if i == 0: 
            continue
        atributos = linea.strip().split(",")
        if len(atributos) != 5:
            continue
        
        fecha_str, descripcion, categoria_str, monto_str, tipo_movimiento = atributos
        
        try:
            fecha, monto = procesar_atributos(fecha_str, monto_str)
        except ValueError as e:
            raise ValueError(f"Error al procesar la línea: {linea}. Detalle del error: {e}")

        if tipo_movimiento == "Ingreso":
            presupuesto.ingresos.append(monto)
        elif tipo_movimiento == "Gasto":
            procesar_gasto(presupuesto, gastos_vistos, descripcion, categoria_str, monto, fecha)

    actualizar_monto_total(presupuesto)
    return presupuesto