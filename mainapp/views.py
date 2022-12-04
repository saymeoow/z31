from django.shortcuts import render
from .models import Phones , Company

def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about_us.html')


def support(request):
    return render(request, 'Support.html')

def Phone(request):
    phones = Phones.objects.all()
    return render(request, 'smartphones.html', {'models': phones})