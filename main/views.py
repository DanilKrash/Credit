from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def contact(request):
    return render(request, 'main/about_us.html')
