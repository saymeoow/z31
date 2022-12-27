from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('about', views.about,
         name='about'),
    path('support', views.support,
         name='support'),
    path('smartphones', views.phones,
         name='smartphones'),
    path('smartphones/<slug:current_slug>/', views.current_phones,
         name='current_phone'),
    path('apple', views.apple, name='apple'),
    path('samsung', views.samsung, name='samsung'),
    path('mi', views.mi, name='mi'),
    path('login/', views.LoginUser, name='login')
]