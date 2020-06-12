from urllib.request import urlopen
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
from . import anpr
import numpy as np
import cv2
from .models import ProcessedImage
import cloudinary
# @csrf_exempt
# def recognize(request):
#     processed_image = ProcessedImage()
#     processed_image.image = request.FILES.get('image')
#     processed_image.plate_number = anpr.process(processed_image.image.name)
#     processed_image.save()
#     return JsonResponse({
#         'plate_number': processed_image.plate_number
#     })

@csrf_exempt
def recognize(request):
    processed_image = ProcessedImage()
    processed_image.image = request.FILES.get('image')
    processed_image.plate_number = ''
    processed_image.save()

    processed_image.plate_number = anpr.process(processed_image.image.build_url())
    processed_image.save()
    return JsonResponse({
        'plate_number': processed_image.plate_number
    })