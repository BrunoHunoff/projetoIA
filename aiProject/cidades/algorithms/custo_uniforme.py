import heapq

def buscar(grafo, start, goal, heuristica=None):
    frontier = [(0, [start])]
    visited = set()
    iteracoes = []

    while frontier:
        currentCost, path = heapq.heappop(frontier)
        currentCity = path[-1]
        iteracoes.append((path, currentCost))

        if currentCity == goal:
            return path, iteracoes, currentCost

        if currentCity in visited:
            continue
        visited.add(currentCity)

        for neighbor, cost in grafo.get(currentCity, {}).items():
            if neighbor not in visited:
                heapq.heappush(frontier, (currentCost + cost, path + [neighbor]))

    return None, iteracoes, float('inf')
