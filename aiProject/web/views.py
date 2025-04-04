# views.py (em qualquer app)
from django.shortcuts import render
from ..ocr.ocr import upload_image
from ..algorithms.uniformCostSearch import uniform_cost_search

def pagina_teste(request):
    contexto = {
        'placa': None,
        'rota': None
    }

    if request.method == 'POST':
        # Processa OCR se veio imagem
        if 'imagem' in request.FILES:
            contexto['placa'] = upload_image(request)
        
        # Processa UCS se veio cidades
        if 'start' in request.POST and 'goal' in request.POST:
            start = request.POST['start']
            goal = request.POST['goal']
            path, cost = uniform_cost_search(start, goal)
            contexto['rota'] = {'path': path, 'cost': cost}
    
    return render(request, 'test.html', contexto)