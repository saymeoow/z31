from django.shortcuts import render

from .models import Phones

def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about_us.html')


def support(request):
    return render(request, 'Support.html')


def phones(request):
    phone = Phones.objects.all()
    context = {
        'model': phone,
        'price': phone,
        'img': phone,
        'descriptoin': phone,
        'company': phone,
        'id': phone,
    }
    return render(request, 'smartphones.html', context=context)


def current_phones(request, current_slug):
    phone_model = Phones.objects.get(slug=current_slug)
    context = {
        'model': phone_model,
        'price': phone_model,
        'img': phone_model,
        'descriptoin': phone_model,
        'company': phone_model,
        'id': phone_model,
    }
    return render(request, 'current_phones.html', context=context)