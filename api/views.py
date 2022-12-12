from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .serializers import PhonesSerializer
from mainapp.models import Phones


class PhonesList(ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer



class PhonesDetail(RetrieveAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    lookup_field = 'slug'
