from collections import deque 

def agregarAristas(G):
    E = G[1]
    V = G[0]
    lista_adyacencia = {v: [] for v in V}
    
    for (a, b) in E:
        lista_adyacencia[a].append(b)
        lista_adyacencia[b].append(a)
    
    cola = deque([V[0]])  
    paridad = [-1] * (n + 1) 
    paridad[V[0]] = 0  
    

    while cola:
        actual = cola.pop()
        for v in lista_adyacencia[actual]:
            if paridad[v] == -1: 
                paridad[v] = 1 - paridad[actual] 
                cola.append(v)
    
    Pares = paridad.count(0)
    Impares = paridad.count(1)
    
    Posibles_aristas = Pares * Impares
    return Posibles_aristas - (n - 1)  
# Lectura de la entrada
n = int(input())
E = []  
for _ in range(n - 1):
    cola_arista, punta_arista = map(int, input().split())
    E.append((cola_arista, punta_arista))

V = [i + 1 for i in range(n)]
G = (V, E)

print(agregarAristas(G))




