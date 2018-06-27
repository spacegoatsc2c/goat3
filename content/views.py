from django.shortcuts import render
from django.http import HttpResponse

from .models import Content

# Create your views here.
def home_page(request):

    if request.method == 'POST':
        Content.objects.create(text=request.POST.get('upload_text', ''))
    return render(request,
        'home.html',
        { 'uploaded_items': Content.objects.all()
        }
    )
