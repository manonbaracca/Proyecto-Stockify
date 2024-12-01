# Definimos las capacidades de los jarros
CAPACITIES = (12, 8, 3)

# Función para generar los estados vecinos
def generar_vecinos(estado_actual):
    jarro_12, jarro_8, jarro_3 = estado_actual
    vecinos = []

    # Llenar los jarros
    vecinos.append((CAPACITIES[0], jarro_8, jarro_3))  # Llenar jarro de 12
    vecinos.append((jarro_12, CAPACITIES[1], jarro_3))  # Llenar jarro de 8
    vecinos.append((jarro_12, jarro_8, CAPACITIES[2]))  # Llenar jarro de 3

    # Vaciar los jarros
    vecinos.append((0, jarro_8, jarro_3))  # Vaciar jarro de 12
    vecinos.append((jarro_12, 0, jarro_3))  # Vaciar jarro de 8
    vecinos.append((jarro_12, jarro_8, 0))  # Vaciar jarro de 3

    # Transferir entre jarros
    transfer = min(jarro_12, CAPACITIES[1] - jarro_8)  # De 12 a 8
    vecinos.append((jarro_12 - transfer, jarro_8 + transfer, jarro_3))

    transfer = min(jarro_12, CAPACITIES[2] - jarro_3)  # De 12 a 3
    vecinos.append((jarro_12 - transfer, jarro_8, jarro_3 + transfer))

    transfer = min(jarro_8, CAPACITIES[0] - jarro_12)  # De 8 a 12
    vecinos.append((jarro_12 + transfer, jarro_8 - transfer, jarro_3))

    transfer = min(jarro_8, CAPACITIES[2] - jarro_3)  # De 8 a 3
    vecinos.append((jarro_12, jarro_8 - transfer, jarro_3 + transfer))

    transfer = min(jarro_3, CAPACITIES[0] - jarro_12)  # De 3 a 12
    vecinos.append((jarro_12 + transfer, jarro_8, jarro_3 - transfer))

    transfer = min(jarro_3, CAPACITIES[1] - jarro_8)  # De 3 a 8
    vecinos.append((jarro_12, jarro_8 + transfer, jarro_3 - transfer))

    return vecinos

# Algoritmo de búsqueda por anchura (BFS)
def busqueda_por_anchura(estado_inicial, objetivo):
    cola = [(estado_inicial, [])]  # Estados por explorar, con su camino
    visitados = []  # Lista de estados ya explorados

    while cola:
        estado_actual, camino = cola.pop(0)  # Tomamos el primer estado de la cola

        # Verificar si el objetivo ya se alcanzó
        if objetivo in estado_actual:
            return camino + [estado_actual]

        # Evitar estados ya visitados
        if estado_actual in visitados:
            continue

        # Marcar estado como visitado
        visitados.append(estado_actual)

        # Generar vecinos y agregarlos a la cola
        for vecino in generar_vecinos(estado_actual):
            if vecino not in visitados:
                cola.append((vecino, camino + [estado_actual]))

    return None  # No se encontró solución

# Estado inicial y objetivo
estado_inicial = (0, 0, 0)  # Los jarros están vacíos al inicio
objetivo = 1  # Queremos 1 galón en algún jarro

# Ejecutar la búsqueda por anchura
solucion = busqueda_por_anchura(estado_inicial, objetivo)

# Mostrar la solución encontrada
if solucion:
    print("Solución encontrada:")
    for paso in solucion:
        print(paso)
else:
    print("No se encontró solución.")
