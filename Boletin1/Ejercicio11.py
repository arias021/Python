# Modificar el programa anterior para que tu programa tire dos dados de forma continuada
# hasta que el número que salga en ambos sea el mismo. En ese momento debería de parar la
# ejecución e informarnos de cuantas tiradas ha tenido que hacer para llegar a ese resultado

import random

tiradas = 0  # Inicializar el contador de tiradas
while True:
    tiradas += 1  # Incrementar el contador de tiradas
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print (dado1, dado2)
    if dado1 == dado2:
        # Mostrar el resultado final (sin mostrar las tiradas intermedias)
        print(f"Número de tiradas: {tiradas}")
        break
