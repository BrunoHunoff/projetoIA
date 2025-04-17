import heapq

def buscar(grafo, inicio, objetivo, heuristica=None):
    fila = [(0, [inicio])]
    visitados = set()
    iteracoes = []

    while fila:
        custo, caminho = heapq.heappop(fila)
        atual = caminho[-1]
        iteracoes.append((caminho, custo))

        if atual == objetivo:
            return caminho, iteracoes, custo

        if atual in visitados:
            continue
        visitados.add(atual)

        for vizinho, peso in grafo.get(atual, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, caminho + [vizinho]))

    return None, iteracoes, float('inf')
