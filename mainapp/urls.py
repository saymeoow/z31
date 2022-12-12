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
]