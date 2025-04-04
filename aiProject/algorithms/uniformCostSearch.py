from .citiesData import CITIES_DISTANCE

def uniform_cost_search(start, goal):
    """
    Retorna o caminho mais curto e a distância total entre 'start' e 'goal'.
    """
    
    print("ENTREI")
    
    if start not in CITIES_DISTANCE:
        return "Cidade não encontrada" + start, None
    
    if goal not in CITIES_DISTANCE:
        return "Cidade não encontrada" + start, None
    
    
    # Fila de prioridade: (custo_acumulado, cidade_atual, caminho)
    frontier = [(0, start, [start])]
    #heapq.heappush(frontier, (0, start, [start]))
    visited = []

    while frontier:
        frontier.sort()
        
        current_cost, current_city, path = frontier.pop(0)

        if current_city == goal:
            return path, current_cost  # Caminho encontrado!

        if current_city in visited:
            continue

        visited.append(current_city)

        for neighbor, distance in CITIES_DISTANCE[current_city].items():
            if neighbor not in visited:
                new_cost = current_cost + distance
                new_path = path + [neighbor]
                frontier.append((new_cost, neighbor, new_path))

    return None, float('inf')