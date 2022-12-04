from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('about', views.about, name='about'),
    path('support', views.support, name='support'),
    path('smartphones', views.Phone, name='smartphones')
]