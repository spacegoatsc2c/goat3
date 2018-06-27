from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from .models import Content

# Create your views here.
def home_page(request):
    error_text = ''
    if request.method == 'POST':
        try:
            content = Content(text=request.POST.get('upload_text', ''))
            content.save()
            content.full_clean()
        except ValidationError:
            error_text = "This has already been uploaded"
            content.delete()
    return render(request,
        'home.html',
        { 'uploaded_items': Content.objects.all(),
          'error_text': error_text,
        }
    )
