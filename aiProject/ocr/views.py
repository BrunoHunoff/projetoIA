import os
from ocr.ocr import upload_image

def ocr_view(request):
    placa = None
    
    if request.method == 'POST' and 'imagem' in request.FILES:        
        placa = upload_image(request)
    
    return render(request, 'ocr/upload.html', {'placa': placa})