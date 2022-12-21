from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PhonesList, PhonesDetail

urlpatterns = [
    path('smartphoneslist', PhonesList.as_view()),
    path('smartphonesdetails/<slug>/', PhonesDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
