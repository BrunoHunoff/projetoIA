from .algorithms import custo_uniforme, aprofundamento_progressivo, procura_sofrega, a_estrela

def get_grafo():
    return {
        'Aveiro': {'Porto': 68, 'Viseu': 95, 'Coimbra': 68, 'Leiria': 115},
        'Braga': {'Viana do Castelo': 48, 'Vila Real': 106, 'Porto': 53},
        'Bragança': {'Vila Real': 137, 'Guarda': 202},
        'Beja': {'Évora': 78, 'Faro': 152, 'Setúbal': 142},
        'Castelo Branco': {'Coimbra': 159, 'Guarda': 106, 'Portalegre': 80, 'Évora': 203},
        'Coimbra': {'Aveiro': 68, 'Viseu': 96, 'Leiria': 67, 'Castelo Branco': 159},
        'Évora': {'Lisboa': 150, 'Santarém': 117, 'Portalegre': 131, 'Castelo Branco': 203, 'Beja': 78, 'Setúbal': 103},
        'Faro': {'Beja': 152, 'Setúbal': 249, 'Lisboa': 299},
        'Guarda': {'Bragança': 202, 'Castelo Branco': 106, 'Vila Real': 157, 'Viseu': 85},
        'Leiria': {'Aveiro': 115, 'Coimbra': 67, 'Lisboa': 129, 'Santarém': 70},
        'Lisboa': {'Évora': 150, 'Leiria': 129, 'Santarém': 78, 'Setúbal': 50, 'Faro': 299},
        'Porto': {'Aveiro': 68, 'Braga': 53, 'Viana do Castelo': 71, 'Vila Real': 116, 'Viseu': 133},
        'Santarém': {'Lisboa': 78, 'Leiria': 70, 'Évora': 117},
        'Setúbal': {'Lisboa': 50, 'Évora': 103, 'Beja': 142, 'Faro': 249},
        'Viana do Castelo': {'Braga': 48, 'Porto': 71},
        'Vila Real': {'Braga': 106, 'Bragança': 137, 'Guarda': 157, 'Porto': 116, 'Viseu': 110},
        'Viseu': {'Aveiro': 95, 'Coimbra': 96, 'Porto': 133, 'Guarda': 85, 'Vila Real': 110},
        'Portalegre': {'Castelo Branco': 80, 'Évora': 131}
    }

def get_heuristica():
    return {
        'Aveiro': 366,
        'Braga': 454,
        'Bragança': 487,
        'Beja': 99,
        'Castelo Branco': 280,
        'Coimbra': 319,
        'Évora': 157,
        'Faro': 0,
        'Guarda': 352,
        'Leiria': 278,
        'Lisboa': 195,
        'Portalegre': 228,
        'Porto': 418,
        'Santarém': 231,
        'Setúbal': 168,
        'Viana do Castelo': 473,
        'Vila Real': 429,
        'Viseu': 363
    }

def executar_busca(origem, destino, metodo):
    grafo = get_grafo()
    heuristica = get_heuristica()

    if metodo == 'custo_uniforme':
        return custo_uniforme.buscar(grafo, origem, destino)
    elif metodo == 'aprofundamento_progressivo':
        return aprofundamento_progressivo.buscar(grafo, origem, destino)
    elif metodo == 'procura_sofrega':
        return procura_sofrega.buscar(grafo, origem, destino, heuristica)
    elif metodo == 'a_estrela':
        return a_estrela.buscar(grafo, origem, destino, heuristica)
    else:
        return None, [], 0
