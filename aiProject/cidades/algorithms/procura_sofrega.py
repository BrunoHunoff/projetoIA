import heapq

def buscar(grafo, inicio, objetivo, heuristica_matriz):
    fila = [(heuristica_matriz[objetivo][inicio], [inicio])]
    visitados = set()
    iteracoes = []

    while fila:
        h, caminho = heapq.heappop(fila)
        atual = caminho[-1]
        
        custo = sum(grafo[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1))
        
        iteracoes.append((caminho, custo))

        if atual == objetivo:
            
            return caminho, iteracoes, custo

        if atual in visitados:
            continue
        visitados.add(atual)

        for vizinho in grafo.get(atual, {}):
            if vizinho not in visitados:
                heuristica = heuristica_matriz[objetivo][vizinho]
                heapq.heappush(fila, (heuristica, caminho + [vizinho]))

    return None, [], float('inf')
