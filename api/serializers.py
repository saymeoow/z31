from rest_framework.serializers import ModelSerializer

from mainapp.models import Phones


class PhonesSerializer(ModelSerializer):
    class Meta:
        model = Phones
        fields = ['model', 'price', 'company_name', 'slug',]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
