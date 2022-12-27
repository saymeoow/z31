from django.contrib.auth.views import LoginView
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

def apple(request):
    apple = Phones.objects.filter(company_name=5)
    context = {
        'model': apple,
        'price': apple,
        'img': apple,
        'descriptoin': apple,
        'company': apple,
        'id': apple,
    }
    return render(request, 'apple.html', context=context)

def mi(request):
    mi = Phones.objects.filter(company_name=3)
    context = {
        'model': mi,
        'price': mi,
        'img': mi,
        'descriptoin': mi,
        'company': mi,
        'id': mi,
    }
    return render(request, 'mi.html', context=context)


def samsung(request):
    samsung = Phones.objects.filter(company_name=4)
    context = {
        'model': samsung,
        'price': samsung,
        'img': samsung,
        'descriptoin': samsung,
        'company': samsung,
        'id': samsung,
    }
    return render(request, 'samsung.html', context=context)


class LoginUser(LoginView):
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))