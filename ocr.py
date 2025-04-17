import cv2
from django.http import JsonResponse
import os
import re
import easyocr

reader = easyocr.Reader(['en', 'pt'])

def validar_placa(placa):
    padrao = r"^[A-Z]{2}\d{2}[A-Z]{2}$|^\d{2}[A-Z]{2}\d{2}$|^[A-Z]{2}\d{4}$|^\d{4}[A-Z]{2}$"
    return bool(re.match(padrao, placa))

def extrairTexto(image_path):    
    results = reader.readtext(image_path, detail=0)
    print("🧾 Resultado bruto OCR:", results)

    formattedResults = []
    for text in results:
        text = re.sub(r"[^A-Za-z0-9]", "", text).upper()

        text = text.replace("O", "0")
        text = text.replace("I", "1")
        text = text.replace("Z", "2")  

        formattedResults.append(text)

    print(" Após correção:", formattedResults)

    placas = [placa for placa in formattedResults if validar_placa(placa)]
    print(" Matrículas validadas:", placas)

    return placas if placas else []



def upload_image(request):
    if request.method == 'POST':
        if 'imagem' not in request.FILES:
            return 'imagem não encontrada'

        imagem = request.FILES['imagem']
        image_path = f"./media/{imagem.name}"

        os.makedirs("media", exist_ok=True)

        with open(image_path, 'wb+') as destination:
            for chunk in imagem.chunks():
                destination.write(chunk)

        placa = extrairTexto(image_path)

        os.remove(image_path)

        return placa

    return JsonResponse({'error': 'Método não permitido'}, status=405)
