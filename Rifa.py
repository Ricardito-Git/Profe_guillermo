import random

boletos = {}

while True:
    print("\n--- RIFA DE BOLETOS ---")
    print("1. Agregar boleto")
    print("2. Mostrar boletos")
    print("3. Elegir ganadores")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        numero = input("Número de boleto: ")
        nombre = input("Nombre del participante: ")
        boletos[numero] = nombre
        print("Boleto agregado")

    elif opcion == "2":
        print("\nBoletos registrados:")
        for num, nom in boletos.items():
            print(f"Boleto {num}: {nom}")

    elif opcion == "3":
        participantes_unicos = list(set(boletos.values()))

        if len(participantes_unicos) < 3:
            print("No hay suficientes participantes")
        else:
            ganadores = random.sample(participantes_unicos, 3)
            print("\n🎉 GANADORES 🎉")
            for g in ganadores:
                print(g)

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
