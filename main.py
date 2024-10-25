from src.gasto import Gasto
from src.presupuesto import Presupuesto

def main():
    presupuesto = float(input("Introduce el monto total del presupuesto mensual: "))
    presupuesto_mensual = Presupuesto(presupuesto)
    
    while True:
        descripcion = input("\nIntroduce la descripción del gasto (o escribe 'salir' para terminar): ")
        if descripcion.lower() == 'salir':
            break
        monto = float(input("Introduce el monto del gasto: "))
        
        tipo_gasto = input("¿Es un gasto fijo? (s/n): ").lower()
        fijo = tipo_gasto == 's'
        
        nuevo_gasto = Gasto(descripcion, monto, fijo)
        presupuesto_mensual.agregar_gasto(nuevo_gasto)
        
        presupuesto_mensual.mostrar_gastos()

if __name__ == "__main__":
    main()
