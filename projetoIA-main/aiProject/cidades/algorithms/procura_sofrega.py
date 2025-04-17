import heapq

def buscar(grafo, inicio, objetivo, heuristica_matriz):
    fila = [(heuristica_matriz[objetivo][inicio], [inicio])]
    visitados = set()

    while fila:
        h, caminho = heapq.heappop(fila)
        atual = caminho[-1]

        if atual == objetivo:
            custo = sum(grafo[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1))
            return caminho, [], custo

        if atual in visitados:
            continue
        visitados.add(atual)

        for vizinho in grafo.get(atual, {}):
            if vizinho not in visitados:
                heuristica = heuristica_matriz[objetivo][vizinho]
                heapq.heappush(fila, (heuristica, caminho + [vizinho]))

    return None, [], float('inf')
