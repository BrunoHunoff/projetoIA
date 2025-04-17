def buscar(grafo, inicio, objetivo, heuristica=None):
    iteracoes = []

    def dfs(caminho, limite):
        atual = caminho[-1]
        if atual == objetivo:
            return caminho
        if limite == 0:
            return None
        for vizinho in grafo.get(atual, {}):
            if vizinho not in caminho:
                novo_caminho = dfs(caminho + [vizinho], limite - 1)
                if novo_caminho:
                    return novo_caminho
        return None

    for profundidade in range(100):
        caminho = dfs([inicio], profundidade)
        iteracoes.append((profundidade, caminho))
        if caminho:
            custo = sum(grafo[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1))
            return caminho, iteracoes, custo

    return None, iteracoes, float('inf')
