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
        
def procesar_gasto(presupuesto, gasto_variable_convertido, gastos_vistos, descripcion, monto, fecha):
    """
    Procesa un gasto y lo clasifica como fijo o variable. Lógica de negocio. 

    Se catalogará como gasto FIJO si es recurrente "visto". 
    Todo gasto cuya clave no aparezca en el array gastos_vistos se registrará como VARIABLE.
    Al procesar un gasto cuya clave aparezca en el array gastos_vistos, este gasto se registrará como FIJO. 
        - No obstante, el primer gasto procesado con esta clave se registró como VARIABLE. No es coherente. Aquí entra el array gasto_variable_convertido.
        - Si la clave del gasto NO aparece en el array gasto_variable_convertido, se deberá convertir ese gasto VARIABLE a FIJO para mantener la coherencia entre los gastos con misma clave.
        - Si la clave del gasto SÍ aparece en el array gasto_variable_convertido, no se hará nada pues ya hay coherencia en los datos.
        - Por tanto, solo se aplicará esta conversión cuando se procese el segundo gasto con una clave determinada.  

    Parámetros:
    - presupuesto: Objeto Presupuesto que contiene gastos fijos y variables.
    - gastos_variable_convertido: Diccionario para rastrear los gastos variables convertidos a fijos. 
    - gastos_vistos: Diccionario para rastrear gastos ya procesados.
    - descripcion: Descripción del gasto.
    - monto: Monto del gasto.
    - fecha: Fecha del gasto.
    """
    clave_gasto = (descripcion, monto)

    if clave_gasto in gastos_vistos:
        agregar_gasto_fijo(presupuesto, descripcion, monto, fecha)
        
        if clave_gasto not in gasto_variable_convertido:
            convertir_gasto_variable_a_fijo(presupuesto, gasto_variable_convertido, clave_gasto)
    else:
        agregar_gasto_variable(presupuesto, gastos_vistos, clave_gasto, descripcion, monto, fecha)
    
def agregar_gasto_fijo(presupuesto, descripcion, monto, fecha):
    """
    Agrega un nuevo gasto a la categoría FIJO.
    Parámetros:
    - presupuesto: Objeto Presupuesto que contiene gastos fijos y variables.
    - descripcion: Descripción del gasto.
    - monto: Monto del gasto.
    - fecha: Fecha del gasto.
    """
    gasto = Gasto(descripcion=descripcion, monto=monto, fecha=fecha, categoria=CategoriaGasto.FIJO)
    presupuesto.gastos_fijos.append(gasto)    
    
def convertir_gasto_variable_a_fijo(presupuesto, gasto_variable_convertido, clave_gasto):
    """
    Busca en el array gastos_variables del presupuesto un gasto que tenga la clave_gasto pasada como parámetro. 
    Este gasto presenta una incoherencia en los datos dado que el resto de gastos con la misma clave están registrados como FIJOS.
    Debe eliminarse del array gastos_variables, actualizarse a FIJO e incluirse en el array gastos_fijos.
    La comprobación que permite ejecutar este método se realiza en el método principal procesar_gasto.  
    
    Parámetros:
    - presupuesto: Objeto Presupuesto que contiene gastos fijos y variables.
    - gastos_variable_convertido: Diccionario para rastrear los gastos variables convertidos a fijos.
    - clave_gasto: Clave del gasto (descripcion, monto).  
    """
    gasto_variable_existente = next(
        (g for g in presupuesto.gastos_variables if g.descripcion == clave_gasto[0] and g.monto == clave_gasto[1] and g.categoria == CategoriaGasto.VARIABLE),
        None
    )
    presupuesto.gastos_variables.remove(gasto_variable_existente)
    gasto_variable_existente.categoria = CategoriaGasto.FIJO
    presupuesto.gastos_fijos.append(gasto_variable_existente)
    
    gasto_variable_convertido[clave_gasto] = True

def agregar_gasto_variable(presupuesto, gastos_vistos, clave_gasto, descripcion, monto, fecha):
    """
    Agrega un nuevo gasto a la categoría VARIABLE y lo marca como visto.
    Parámetros:
    - presupuesto: Objeto Presupuesto que contiene gastos fijos y variables.
    - gastos_vistos: Diccionario para rastrear gastos ya procesados.
    - clave_gasto: Clave del gasto (descripcion, monto).
    - descripcion: Descripción del gasto.
    - monto: Monto del gasto.
    - fecha: Fecha del gasto.
    """
    gasto = Gasto(descripcion=descripcion, monto=monto, fecha=fecha, categoria=CategoriaGasto.VARIABLE)
    presupuesto.gastos_variables.append(gasto)
    gastos_vistos[clave_gasto] = True

def actualizar_monto_total(presupuesto):
    total_gastos = sum(gasto.monto for gasto in presupuesto.gastos_fijos) + sum(gasto.monto for gasto in presupuesto.gastos_variables)
    presupuesto.monto_total = sum(presupuesto.ingresos) - total_gastos

def procesar_presupuesto(ruta_archivo):
    lineas = leer_archivo_csv(ruta_archivo)
    presupuesto = Presupuesto(monto_total=0)
    gastos_vistos = {}
    gasto_variable_convertido = {}

    for i, linea in enumerate(lineas):
        if i == 0: 
            continue
        atributos = linea.strip().split(",")
        if len(atributos) != 4:
            continue
        
        fecha_str, descripcion, monto_str, tipo_movimiento = atributos
        
        try:
            fecha, monto = procesar_atributos(fecha_str, monto_str)
        except ValueError as e:
            raise ValueError(f"Error al procesar la línea: {linea}. Detalle del error: {e}")

        if tipo_movimiento == "Ingreso":
            presupuesto.ingresos.append(monto)
        elif tipo_movimiento == "Gasto":
            procesar_gasto(presupuesto, gasto_variable_convertido, gastos_vistos, descripcion, monto, fecha)

    actualizar_monto_total(presupuesto)
    return presupuesto

def puede_permitirse_gasto_adicional(presupuesto, importe_adicional: float) -> bool:
    total_gastos = sum(gasto.monto for gasto in presupuesto.gastos_fijos) + sum(gasto.monto for gasto in presupuesto.gastos_variables)
    
    ingreso_disponible = sum(presupuesto.ingresos) - total_gastos - presupuesto.meta_ahorro
    
    if ingreso_disponible >= importe_adicional:
        presupuesto.gasto_no_planificado = importe_adicional
        return True
    else:
        return False