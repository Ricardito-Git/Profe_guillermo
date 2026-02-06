cd = []
DURACION_MAX = 80

def duracion_total():
    return sum(cancion["duracion"] for cancion in cd)

while True:
    print("\n--- CD DE AUDIO ---")
    print("1. Agregar canción")
    print("2. Ver canciones")
    print("3. Ver duración total")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")
        duracion = float(input("Duración (minutos): "))

        if duracion_total() + duracion <= DURACION_MAX:
            cd.append({
                "nombre": nombre,
                "artista": artista,
                "duracion": duracion
            })
            print("Canción agregada al CD")
        else:
            print("No cabe en el CD (máximo 80 minutos)")

    elif opcion == "2":
        print("\nCanciones en el CD:")
        for c in cd:
            print(f"{c['nombre']} - {c['artista']} ({c['duracion']} min)")

    elif opcion == "3":
        print("Duración total:", duracion_total(), "min")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
