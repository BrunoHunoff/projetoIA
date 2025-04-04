from django.shortcuts import render
from aiProject.algorithms.uniformCostSearch import uniform_cost_search

def pagina_teste(request):
    rota_resultado = 'aaaaaa'
    
    print(rota_resultado)

    # Verifica se há parâmetros GET (você pode usar POST também se quiser)
    if request.method == "GET" and "inicio" in request.GET and "destino" in request.GET:
        start = request.GET.get("inicio")
        end = request.GET.get("destino")
        rota_resultado = uniform_cost_search(start, end)
        
    print(rota_resultado)

    return render(request, 'test.html', {
        'resultado': rota_resultado
    })
