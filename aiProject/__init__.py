from algorithms.uniformCostSearch import uniform_cost_search
if __name__ == "__main__":
    path, distance = uniform_cost_search("Aveiro", "Lisboa")
    print("Caminho:", path)
    print("Distância total:", distance, "km")