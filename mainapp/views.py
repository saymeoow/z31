from django.shortcuts import render
from .models import phone


def main(request):
    return render(request, 'mainapp/main.html')


def about(request):
    return render(request, 'mainapp/about_us.html')


def support(request):
    return render(request, 'mainapp/Support.html')
