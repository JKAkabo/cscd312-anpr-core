from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from . import anpr
from .models import ProcessedImage

@csrf_exempt
def recognize(request):
    processed_image = ProcessedImage()
    processed_image.image = request.FILES.get('image')
    processed_image.plate_number = anpr.process(processed_image.image.name)
    processed_image.save()
    return JsonResponse({
        'plate_number': processed_image.plate_number
    })
