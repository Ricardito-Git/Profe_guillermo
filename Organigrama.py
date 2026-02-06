class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subordinados = []

def mostrar(empleado, nivel=0):
    print("  " * nivel + "- " + empleado.nombre)
    for sub in empleado.subordinados:
        mostrar(sub, nivel + 1)

# Crear director
director = Empleado(input("Nombre del Director General: "))
empleados = {director.nombre: director}

while True:
    print("\n--- ORGANIGRAMA ---")
    print("1. Agregar empleado")
    print("2. Mostrar organigrama")
    print("3. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        jefe = input("Nombre del jefe: ")
        nombre = input("Nombre del empleado: ")

        if jefe in empleados:
            nuevo = Empleado(nombre)
            empleados[jefe].subordinados.append(nuevo)
            empleados[nombre] = nuevo
            print("Empleado agregado")
        else:
            print("Jefe no encontrado")

    elif opcion == "2":
        print("\nOrganigrama:")
        mostrar(director)

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
