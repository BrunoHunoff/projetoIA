from django.urls import path
from .ocr import upload_image

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
]
