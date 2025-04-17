from django.shortcuts import render
from aiProject.cidades.graph import GRAFO
from aiProject.cidades.algorithms.aprofundamento_progressivo import buscar as aprofundamento_progressivo
from aiProject.cidades.algorithms.a_estrela import buscar as a_estrela
from aiProject.cidades.algorithms.procura_sofrega import buscar as procura_sofrega
from aiProject.algorithms.uniformCostSearch import uniform_cost_search
from aiProject.ocr.ocr import upload_image
from aiProject.cidades.views import gerar_mapa
from aiProject.cidades.heuristicas import HEURISTICAS_MATRIZ 

def interface(request):
    resultado = None
    placa = None
    mapa_html = None
    cidades = list(GRAFO.keys())

    mapa_html = gerar_mapa("Lisboa", "Lisboa", ["Lisboa"], GRAFO)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'ocr':
            imagem = request.FILES.get("imagem")
            if imagem:
                placa = upload_image(request)
                if placa:
                    placa = placa[0]

        elif action == 'buscar':
            origem = request.POST.get("origem")
            destino = request.POST.get("destino")
            algoritmo = request.POST.get("algoritmo")
            placa = request.POST.get("placa")

            if origem and destino:
                if algoritmo == "custo_uniforme":
                    caminho, custo = uniform_cost_search(origem, destino)
                    resultado = {"caminho": caminho, "custo": custo}

                elif algoritmo == "aprofundamento_progressivo":
                    caminho, _, custo = aprofundamento_progressivo(GRAFO, origem, destino)
                    resultado = {"caminho": caminho, "custo": custo}

                elif algoritmo == "procura_sofrega":
                    caminho, _, custo = procura_sofrega(GRAFO, origem, destino, HEURISTICAS_MATRIZ)
                    resultado = {"caminho": caminho, "custo": custo}

                elif algoritmo == "a_estrela":
                    caminho, _, custo = a_estrela(GRAFO, origem, destino, HEURISTICAS_MATRIZ)
                    resultado = {"caminho": caminho, "custo": custo}

                if resultado and resultado.get("caminho"):
                    mapa_html = gerar_mapa(origem, destino, resultado["caminho"], GRAFO)

    return render(request, "interface.html", {
        "resultado": resultado,
        "placa": placa,
        "cidades": cidades,
        "mapa_html": mapa_html
    })
