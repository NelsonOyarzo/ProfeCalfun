import random

# Definir las opciones de "Me quiere mucho, poquito, nada"
opciones = ["mucho", "poquito", "nada" , "felicidades te quieren: MUCHO MUCHO MUCHO"]

# Tomar una ramita con hojas o una flor (representada por una lista)
flor = ["hoja"] * 5  # Por ejemplo, una ramita con 5 hojas

# Iterar sobre cada hoja de la ramita
for hoja in flor:
    # Generar un índice aleatorio para seleccionar una opción
    indice_opcion = random.randint(0, 2)
    
    # Imprimir la opción elegida para la hoja actual
    print("Me quiere", opciones[indice_opcion])

# Mensaje de despedida
print("¡Fin del juego!")

"""
Matias Caileo
Diego Benitez
Nelson Oyarzo
"""