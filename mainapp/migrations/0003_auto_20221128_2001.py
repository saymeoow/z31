# Generated by Django 3.2.15 on 2022-11-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20221128_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iphone',
            name='model_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='mi',
            name='model_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='model_name',
            field=models.CharField(max_length=256),
        ),
    ]