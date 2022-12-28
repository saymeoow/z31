from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .paginations import UpgradePagination
from .serializers import PhonesSerializer
from mainapp.models import Phones


class PhonesList(ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    ordering = ['model']
    search_fields = ['slug']
    pagination_class = UpgradePagination


class PhonesDetail(RetrieveAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    lookup_field = 'slug'
