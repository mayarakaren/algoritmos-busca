# Definindo o grafo como um dicionário de conjuntos de vértices vizinhos
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def busca_profundidade(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == objetivo:
        return [inicio]
    for proximo in grafo[inicio] - visitados:
        caminho = busca_profundidade(grafo, proximo, objetivo, visitados)
        if caminho:
            return [inicio] + caminho
    return None

# Exemplo de utilização da função de busca em profundidade
inicio = 'A'
objetivo = 'F'
caminho = busca_profundidade(grafo, inicio, objetivo)

if caminho is not None:
    print(f"Caminho encontrado: {' -> '.join(caminho)}")
else:
    print(f"Não foi possível encontrar um caminho de {inicio} até {objetivo} no grafo")


#       A
#      / \
#     B   C
#    / \   \
#   D   E   F
