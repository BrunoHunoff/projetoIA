from django.shortcuts import render
from .graph import GRAFO, HEURISTICAS
from .algorithms import custo_uniforme, aprofundamento_progressivo, procura_sofrega, a_estrela

import folium
from folium import plugins

from .heuristicas import HEURISTICAS_MATRIZ


ALGORITMOS = {
    'custo_uniforme': custo_uniforme.buscar,
    'aprofundamento_progressivo': aprofundamento_progressivo.buscar,
    'procura_sofrega': procura_sofrega.buscar,
    'a_estrela': a_estrela.buscar,
}

def index(request):
    cidades = list(GRAFO.keys())
    resultado = None
    mapa_html = None
    
    if request.method == 'POST':
        origem = request.POST['origem']
        destino = request.POST['destino']
        algoritmo = request.POST['algoritmo']
        funcao = ALGORITMOS[algoritmo]
        heuristica = HEURISTICAS_MATRIZ if 'sofrega' in algoritmo or 'estrela' in algoritmo else None
        caminho, iteracoes, custo = funcao(GRAFO, origem, destino, heuristica)
        resultado = {
            'caminho': caminho,
            'iteracoes': iteracoes,
            'custo': custo,
        }
        
        mapa_html = gerar_mapa(origem, destino, caminho, GRAFO)
    
    return render(request, 'cidades/mapa.html', {'cidades': cidades, 'resultado': resultado, 'mapa_html': mapa_html})


def gerar_mapa(origem, destino, caminho, grafo):
    mapa = folium.Map(location=[38.7169, -9.1395], zoom_start=6)
    
    coordenadas = {
        'Aveiro': [40.6405, -8.6538],
        'Beja': [38.0151, -7.8632],
        'Braga': [41.5452, -8.4265],
        'Bragança': [41.8060, -6.7567],
        'Castelo Branco': [39.8222, -7.4908],
        'Coimbra': [40.2118, -8.4295],
        'Évora': [38.5711, -7.9135],
        'Faro': [37.0194, -7.9304],
        'Guarda': [40.5373, -7.2676],
        'Leiria': [39.7436, -8.8070],
        'Lisboa': [38.7169, -9.1395],
        'Portalegre': [39.2967, -7.4280],
        'Porto': [41.1496, -8.611],
        'Santarém': [39.2362, -8.6859],
        'Setúbal': [38.5248, -8.8882],
        'Viana do Castelo': [41.6918, -8.8344],
        'Vila Real': [41.3006, -7.7441],
        'Viseu': [40.6610, -7.9097]
    }
    
    # Origem (azul)
    folium.Marker(coordenadas[origem], popup=f"Origem: {origem}", icon=folium.Icon(color='blue')).add_to(mapa)

    # Destino (vermelho)
    folium.Marker(coordenadas[destino], popup=f"Destino: {destino}", icon=folium.Icon(color='red')).add_to(mapa)

    # Cidades no meio (laranja)
    for cidade in caminho[1:-1]:  
        if cidade in coordenadas:
            folium.Marker(
                coordenadas[cidade],
                popup=f"{cidade}",
                icon=folium.Icon(color='orange', icon='info-sign')
            ).add_to(mapa)

    # Linha do percurso
    caminho_coords = [coordenadas[cidade] for cidade in caminho if cidade in coordenadas]
    folium.PolyLine(caminho_coords, color="green", weight=3, opacity=1).add_to(mapa)
    
    return mapa._repr_html_()


