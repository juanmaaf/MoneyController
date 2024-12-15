from money_controller.gasto import Gasto
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from money_controller.categoriaGasto import CategoriaGasto

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

def procesar_atributos(fecha_str, importe_str):
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    importe = float(importe_str)
    return fecha, importe

def procesar_gasto(presupuesto, gastos_vistos, concepto, categoria_str, importe, fecha):
    clave_gasto = (concepto, categoria_str, importe)
    
    if clave_gasto in gastos_vistos:
        for gasto in presupuesto.gastos_variables:
            if gasto.concepto == concepto and gasto.importe == importe and gasto.categoria == CategoriaGasto.VARIABLE:
                gasto.categoria=CategoriaGasto.FIJO
                presupuesto.gastos_variables.remove(gasto)
                presupuesto.gastos_fijos.append(gasto)
        gasto = Gasto(fecha=fecha, concepto=concepto, importe=importe, categoria=CategoriaGasto.FIJO)
        presupuesto.gastos_fijos.append(gasto)
    else:
        gasto = Gasto(fecha=fecha, concepto=concepto, importe=importe, categoria=CategoriaGasto.VARIABLE)
        presupuesto.gastos_variables.append(gasto)
        gastos_vistos[clave_gasto] = True

def actualizar_monto_total(presupuesto):
    total_gastos = sum(gasto.importe for gasto in presupuesto.gastos_fijos) + sum(gasto.importe for gasto in presupuesto.gastos_variables)
    presupuesto.monto_total = sum(presupuesto.ingresos) - total_gastos

def procesar_datos(ruta_archivo):
    lineas = leer_archivo_csv(ruta_archivo)
    presupuesto = Presupuesto(monto_total=0)
    gastos_vistos = {}

    for linea in lineas:
        atributos = linea.strip().split(",")
        if len(atributos) != 5:
            continue
        
        fecha_str, concepto, categoria_str, importe_str, tipo_movimiento = atributos
        
        try:
            fecha, importe = procesar_atributos(fecha_str, importe_str)
        except ValueError as e:
            raise ValueError(f"Error al procesar la línea: {linea}. Detalle del error: {e}")

        if tipo_movimiento == "Ingreso":
            presupuesto.ingresos.append(importe)
        elif tipo_movimiento == "Gasto":
            procesar_gasto(presupuesto, gastos_vistos, concepto, categoria_str, importe, fecha)

    actualizar_monto_total(presupuesto)
    return presupuesto