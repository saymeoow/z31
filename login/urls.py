from django.urls import path
import login.views

urlpatterns = [
    path('login/', login.views.logins),
    path('logout/', login.views.logouts),
    path('register/', login.views.registers)
]