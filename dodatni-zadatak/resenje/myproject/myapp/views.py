import logging

from django.shortcuts import render
from django.http import HttpResponse
import tarfile
import os

from myproject import settings
# Configure logging
logging.basicConfig(level=logging.DEBUG)

def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        upload_dir = os.path.join(settings.BASE_DIR, 'uploads')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        tar_file = request.FILES['tarfile']
        upload_path = os.path.join(upload_dir, 'uploaded.tar')
        with open(upload_path, 'wb+') as destination:
            for chunk in tar_file.chunks():
                destination.write(chunk)

        with tarfile.open(upload_path) as tar:
            for member in tar.getmembers():
                logging.debug(f'Extracting {member.name} to {settings.BASE_DIR}')
                tar.extract(member, upload_dir)

        os.remove(upload_path)

        return HttpResponse("File uploaded and extracted successfully.")
    return HttpResponse("Upload failed.")
def profile(request):
    return render(request, 'profile.html')