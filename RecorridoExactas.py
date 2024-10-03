import heapq

# Función para construir el grafo desde las aristas
def construir_grafo(n, aristas):
    grafo = {i: [] for i in range(1, n+1)}
    
    # Añadir aristas al grafo
    for u, v, w in aristas:
        grafo[u].append((v, w))
    
    return grafo

# Algoritmo de Dijkstra
def dijkstra(grafo, n, inicio):
    # Distancia inicial infinita a todos los nodos
    distancias = {i: float('inf') for i in range(1, n+1)}
    distancias[inicio] = 0  # Distancia a la sala inicial es 0

    # Cola de prioridad para Dijkstra (min-heap)
    heap = [(0, inicio)]  # (costo, nodo)
    
    while heap:
        distancia_actual, nodo_actual = heapq.heappop(heap)
        
        # Si la distancia actual es mayor que la conocida, continuamos
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        # Revisar los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual]:
            distancia_nueva = distancia_actual + peso
            
            # Si encontramos una distancia más corta, la actualizamos
            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                heapq.heappush(heap, (distancia_nueva, vecino))
    
    return distancias




n = int(input())  # Cantidad de aulas
atajos = list(map(int, input().split()))  # Lista de atajos

# Lista para almacenar las aristas
aristas = []

# Agregar las aristas por atajos
for i in range(n):
    arista = (i + 1, atajos[i], 1)  # arista desde aula i+1 a atajo[i] con costo 1
    aristas.append(arista)

# Agregar las aristas por caminar entre aulas consecutivas
for i in range(1, n):
    aristas.append((i, i + 1, 1))  # caminar de aula i a aula i+1
    aristas.append((i + 1, i, 1))  # caminar de aula i+1 a aula i

grafo=construir_grafo(n,aristas)
resultado=dijkstra(grafo,n,1)

print(' '.join(str(resultado[aula]) for aula in range(1, n+1)))