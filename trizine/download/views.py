from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
def download(request):
    #context = {
    #    "title":"test1"
    #}
    return render(request, "index.html")
    #return HttpResponse("<h1>hi</h1>")


def pdf_download(request):
    filepath = os.path.join(settings.MEDIA_ROOT, 'trizine_webzine.pdf')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response
