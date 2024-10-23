from src.gasto import Gasto  # Importa la clase Gasto desde la carpeta src
from src.presupuesto import Presupuesto  # Importa la clase Presupuesto desde la carpeta src

def main():
    # Crear el presupuesto (Presupuesto)
    presupuesto = Presupuesto(1200)  # El presupuesto total es 1200

    # Crear algunos gastos como se indica en el problema
    gasto1 = Gasto("Alquiler", 400, "fijo")  # Alquiler
    gasto2 = Gasto("Comunidad de vecinos", 50, "fijo")  # Comunidad de vecinos
    gasto3 = Gasto("Internet", 50, "fijo")  # Internet
    gasto4 = Gasto("Electricidad", 60, "variable")  # Electricidad
    gasto5 = Gasto("Agua", 30, "variable")  # Agua
    gasto6 = Gasto("Gas", 40, "variable")  # Gas
    gasto7 = Gasto("Compras", 150, "variable")  # Otros gastos

    # Agregar los gastos al presupuesto
    presupuesto.agregar_gasto(gasto1)
    presupuesto.agregar_gasto(gasto2)
    presupuesto.agregar_gasto(gasto3)
    presupuesto.agregar_gasto(gasto4)
    presupuesto.agregar_gasto(gasto5)
    presupuesto.agregar_gasto(gasto6)
    presupuesto.agregar_gasto(gasto7)

    # Mostrar todos los gastos
    print("\nLista de gastos:")
    presupuesto.mostrar_gastos()

    # Calcular los ahorros
    ahorros = presupuesto.calcular_ahorros()
    print(f"\nAhorros disponibles: {ahorros}")  # Output: Ahorros disponibles: 420 (1200 - 780)

    # Verificar si un gasto adicional es viable
    viable = presupuesto.es_gasto_adicional_viable(100)
    print(f"Gasto adicional de 100 es viable: {viable}")  # Output: True

    # Calcular y mostrar los gastos por tipo
    total_fijo, total_variable = presupuesto.calcular_gastos_por_tipo()
    print(f"\nTotal gastos fijos: {total_fijo}")  # Output: Total gastos fijos: 500
    print(f"Total gastos variables: {total_variable}")  # Output: Total gastos variables: 280

if __name__ == "__main__":
    main()
