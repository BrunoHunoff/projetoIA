import cv2
from django.http import JsonResponse
import os
import re
import easyocr

# Inicializa o leitor OCR para inglês e português
reader = easyocr.Reader(['en', 'pt'])

# Função para validar o padrão da matrícula portuguesa
def validar_placa(placa):
    # Aceita os formatos: AA00AA, 00AA00, AA0000, 0000AA
    padrao = r"^[A-Z]{2}\d{2}[A-Z]{2}$|^\d{2}[A-Z]{2}\d{2}$|^[A-Z]{2}\d{4}$|^\d{4}[A-Z]{2}$"
    return bool(re.match(padrao, placa))

# Função que extrai texto da imagem e procura por matrículas válidas
def extrairTexto(image_path):    
    results = reader.readtext(image_path, detail=0)
    print("🧾 Resultado bruto OCR:", results)

    formattedResults = []
    for text in results:
        text = re.sub(r"[^A-Za-z0-9]", "", text).upper()

        # Correção de confusões comuns
        text = text.replace("O", "0")
        text = text.replace("I", "1")
        text = text.replace("Z", "2")  # opcional

        formattedResults.append(text)

    print("🔤 Após correção:", formattedResults)

    placas = [placa for placa in formattedResults if validar_placa(placa)]
    print("✅ Matrículas validadas:", placas)

    return placas if placas else []


# Função que processa o upload da imagem, salva temporariamente, e extrai a matrícula
def upload_image(request):
    if request.method == 'POST':
        if 'imagem' not in request.FILES:
            return 'imagem não encontrada'

        imagem = request.FILES['imagem']
        image_path = f"./media/{imagem.name}"

        os.makedirs("media", exist_ok=True)

        # Salva a imagem temporariamente
        with open(image_path, 'wb+') as destination:
            for chunk in imagem.chunks():
                destination.write(chunk)

        # Extrai texto (matrícula)
        placa = extrairTexto(image_path)

        # Apaga imagem depois de processar
        os.remove(image_path)

        return placa

    return JsonResponse({'error': 'Método não permitido'}, status=405)
