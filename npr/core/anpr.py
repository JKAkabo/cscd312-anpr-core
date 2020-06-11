import os
import cv2
import imutils
import pytesseract
import numpy as np
from django.conf import settings

def process(file_path):
    image = cv2.imread(os.path.join(settings.BASE_DIR, file_path))
    image = imutils.resize(image, width=500)
    grayed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayed_image= cv2.bilateralFilter(grayed_image, 11,17,17)
    edged_image = cv2.Canny(grayed_image,170,200)
    countours, _ = cv2.findContours(edged_image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image_1=image.copy()
    cv2.drawContours(image_1,countours,-1,(0,255,0),3)

    countours = sorted(countours, key = cv2.contourArea, reverse=True)[:30]

    i = 0
    for c in countours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018*peri, False)
            if len(approx) >= 3:
                screenCnt = approx
                x, y, w, h = cv2.boundingRect(c)
                countour_image=image[y:y+h, x:x+w]

                filename = f'countour-{str(i)}.png'
                cv2.imwrite(os.path.join(settings.BASE_DIR, 'media', filename),countour_image)

                plate_number = pytesseract.image_to_string(os.path.join(settings.BASE_DIR, 'media', filename), lang='eng')

                if len(plate_number) > 1:
                    return plate_number

            i += 1
    return ''
