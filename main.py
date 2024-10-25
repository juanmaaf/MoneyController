from src.gasto import Gasto
from src.presupuesto import Presupuesto

def obtener_tipo_gasto():
    while True:
        tipo_gasto = input("¿Es un gasto fijo? (s/n): ").lower()
        if tipo_gasto == 's':
            return True
        elif tipo_gasto == 'n':
            return False
        else:
            print("Respuesta no válida. Por favor, responde con 's' para sí o 'n' para no.")

def main():
    presupuesto = float(input("Introduce el monto total del presupuesto mensual: "))
    presupuesto_mensual = Presupuesto(presupuesto)
    
    while True:
        descripcion = input("\nIntroduce la descripción del gasto (o escribe 'salir' para terminar): ")
        if descripcion.lower() == 'salir':
            break
        monto = float(input("Introduce el monto del gasto: "))
        
        tipo_gasto = input("¿Es un gasto fijo? (s/n): ").lower()
        fijo = obtener_tipo_gasto()
        
        nuevo_gasto = Gasto(descripcion, monto, fijo)
        presupuesto_mensual.agregar_gasto(nuevo_gasto)
        
        presupuesto_mensual.mostrar_gastos()

if __name__ == "__main__":
    main()
