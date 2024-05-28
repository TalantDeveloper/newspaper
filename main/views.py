from django.shortcuts import render
from .models import Magazine


def welcome(request):
    return render(request, 'main/welcome.html')


def magazine_details(request, pk):
    magazine = Magazine.objects.get(pk=pk)
    content = {
        'magazine': magazine,
    }
    return render(request, 'main/detail.html', content)


def like_request(request):
    return None