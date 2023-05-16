from collections import deque

# Definindo o grafo como um dicionário de conjuntos de vértices vizinhos
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def busca_largura(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])
    while fila:
        (vertice, caminho) = fila.popleft()
        for proximo in grafo[vertice] - set(caminho):
            if proximo == objetivo:
                return caminho + [proximo]
            else:
                fila.append((proximo, caminho + [proximo]))
    return None

# Exemplo de utilização da função de busca em largura
inicio = 'A'
objetivo = 'F'
caminho = busca_largura(grafo, inicio, objetivo)

if caminho is not None:
    print(f"Caminho encontrado: {' -> '.join(caminho)}")
else:
    print(f"Não foi possível encontrar um caminho de {inicio} até {objetivo} no grafo")

#Grafo utilizado:

#       A
#      / \
#     B   C
#    / \   \
#   D   E   F