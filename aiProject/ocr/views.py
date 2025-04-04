import cv2
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import re
import easyocr

# Inicializa o leitor OCR para inglês e português
reader = easyocr.Reader(['en', 'pt'])

# padrão: AA-00-00
# padrão: 00-00-AA
# padrão: 00-AA-00
# padrão: AA-00-AA
def validar_placa(placa):

    padrao = r"^[A-Z]{2}\d{4}$|^\d{4}[A-Z]{2}$|^\d{2}[A-Z]{2}\d{2}$|^[A-Z]{2}\d{2}[A-Z]{2}$"
    
    return bool(re.match(padrao, placa))


def extrairTexto(image_path):    
    results = reader.readtext(image_path, detail=0)

    #remove espaços e "-" dos textos
    #transforma para UpperCase
    formattedResults = [re.sub(r"[^A-Za-z0-9]", "", text).upper() for text in results]

    placas = [placa for placa in formattedResults if validar_placa(placa)]
    
    if placas:
        return placas
    else:
        return []
    

@csrf_exempt #desativa proteção pois ambiente é dev
def upload_image(request):
    if request.method == 'POST':

        if 'imagem' not in request.FILES:
            return JsonResponse({'error': 'Nenhuma imagem enviada'}, status=400)

        imagem = request.FILES['imagem']

        image_path = f"./media/{imagem.name}"

        os.makedirs("media", exist_ok=True)

        with open(image_path, 'wb+') as destination:
            for chunk in imagem.chunks():
                destination.write(chunk)

        placa = extrairTexto(image_path)

        os.remove(image_path)

        return JsonResponse({'placa_detectada': placa})

    return JsonResponse({'error': 'Método não permitido'}, status=405)

