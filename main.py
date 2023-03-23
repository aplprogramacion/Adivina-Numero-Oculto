import random

def adivina_el_numero():
    numero_oculto = random.randint(1, 50)
    intentos = 0

    while True:
        intentos += 1
        numero_elegido = input("Elige un número entre 1 y 50: ")

        # Comprobar si el número elegido es un número válido
        if not numero_elegido.isdigit() or int(numero_elegido) < 1 or int(numero_elegido) > 50:
            print("Por favor, elige un número válido entre 1 y 50.")
            continue

        # Convertir la entrada a un número entero
        numero_elegido = int(numero_elegido)

        # Comparar el número elegido con el número oculto
        if numero_elegido < numero_oculto:
            print("El número es mayor.")
        elif numero_elegido > numero_oculto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número oculto en {intentos} intentos.")
            break

        # Preguntar si se quiere seguir jugando
        seguir_jugando = input("¿Quieres seguir jugando? (S/N): ")
        if seguir_jugando.upper() == "N":
            print(f"El número oculto era {numero_oculto}. Gracias por jugar.")
            break

# Llamar a la función para empezar el juego
adivina_el_numero()

