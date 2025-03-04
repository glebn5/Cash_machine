from django.shortcuts import render
from rest_framework.views import APIView
from .models import Item
from rest_framework.response import Response
from rest_framework import status
import datetime
import pdfkit
from django.template.loader import render_to_string
from django.conf import settings
import os
import qrcode
from django.http import HttpResponse
import socket

PDFKIT_CONFIGURATION = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

class CashMachineView(APIView):
    def post(self, request, *args, **kwargs):
        items_id = request.data.get('items', [])
        items = Item.objects.filter(id__in=items_id)

        # проверка существования элементов
        if not items.exists():
            return Response({'error': 'Товары не найдены'}, status=status.HTTP_400_BAD_REQUEST)
        
        total = sum(i.price for i in items)

        date = datetime.datetime.now()
        
        context = {
            'items': items,
            'total': total,
            'date': date.strftime("%d.%m.%y %H:%M"),
        }
        
        # рендеринг html шаблона в pdf
        options = {
            "enable-local-file-access": None,
            "page-size": "A7",
            "zoom": "1.0",
            "no-outline": None,
            "dpi": "300",
        }

        html_file = render_to_string('check.html', context)
        pdf_name = f'{date.strftime("%d-%m-%y_%H-%M")}.pdf'
        pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_name)
        pdfkit.from_string(html_file, pdf_path, configuration=PDFKIT_CONFIGURATION, options=options)

        

        # получим IP машины
        hostname = socket.gethostname() # возвращает имя хоста машины
        ip_address = socket.gethostbyname(hostname) # преобразует имя хоста в IP-адрес


        # создание qr-кода

        qr = qrcode.QRCode(
            version=3,               
            box_size=10,         
            border=4               
        )
        qr.add_data(f'http://{ip_address}:8000/media/{pdf_name}')
        qr.make(fit=True)
        qr_code_img = qr.make_image()
        qr_code_img.save(os.path.join(settings.MEDIA_ROOT, f"qr_{pdf_name}.png"))

        with open(os.path.join(settings.MEDIA_ROOT, f"qr_{pdf_name}.png"), 'rb') as qr_file:
            return HttpResponse(qr_file.read(), content_type="image/png")



        




        

