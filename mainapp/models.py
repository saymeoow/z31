from django.db import models
from .mixins import CreateUpdateDeletedMixin


class Phones(models.Model, CreateUpdateDeletedMixin):
    class Meta:
        verbose_name = u'Телефон'
        verbose_name_plural = u'Телефоны'

    id = models.AutoField(
        primary_key=True
    )
    model = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Модель'
    )
    price = models.IntegerField(
        blank=False,
        null=False,
        verbose_name=u"Цена"
    )
    description = models.TextField(
        blank=False,
        verbose_name=u"Описание"
    )
    company_name = models.ForeignKey(
        'Company',
        max_length=256,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name=u'Производитель'
    )
    img = models.ImageField(
        upload_to='static/img/',
        blank=False,
        null=True,
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.model


class Company(models.Model, CreateUpdateDeletedMixin):
    class Meta:
        verbose_name = u"Производитель"
        verbose_name_plural = u"Производители"

    model_name = models.CharField(
        max_length=256,
        blank=False
    )

    def __str__(self):
        return self.model_name
