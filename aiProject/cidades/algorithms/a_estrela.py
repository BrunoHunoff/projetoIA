import heapq

def buscar(grafo, inicio, objetivo, heuristica_matriz):
    fila = [(heuristica_matriz[objetivo][inicio], 0, [inicio])]
    visitados = set()
    iteracoes = []

    while fila:
        f, custo, caminho = heapq.heappop(fila)
        atual = caminho[-1]
        iteracoes.append((caminho, custo))

        if atual == objetivo:
            return caminho, iteracoes, custo

        if atual in visitados:
            continue
        visitados.add(atual)

        for vizinho, peso in grafo.get(atual, {}).items():
            if vizinho not in visitados:
                novo_custo = custo + peso
                prioridade = novo_custo + heuristica_matriz[objetivo][vizinho]
                heapq.heappush(fila, (prioridade, novo_custo, caminho + [vizinho]))

    return None, [], float('inf')
