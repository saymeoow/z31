from django.contrib import admin
from mainapp.forms import PhoneFromAdmin
from mainapp.models import Phones
from mainapp.models import Company


class PhoneAdmin(admin.ModelAdmin):

    list_display = ['model', 'price', 'id', 'company_name']
    list_display_links = ['model', 'price']
    list_editable = ['company_name']
    ordering = ['price']
    list_filter = ['company_name']
    list_per_page = 10
    search_fields = ['company_name', 'model']
    form = PhoneFromAdmin


admin.site.register(Phones, PhoneAdmin)
admin.site.register(Company)
