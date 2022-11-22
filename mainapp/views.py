from django.shortcuts import render
from .models import phone


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about_us.html')


def support(request):
    return render(request, 'Support.html')