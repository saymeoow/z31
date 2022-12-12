from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Phones


class PhoneFromAdmin(ModelForm):

    def clean_phones_company(self):

        company = Phones.objects.filter(company_name=self.instance)

        if len(company) > 0 and self.cleaned_data['company_name'] != company[0]:
            raise ValidationError(
                'Производителем телефона является другая компания',
                code='invalid',)
            return self.cleaned_data['company_name']