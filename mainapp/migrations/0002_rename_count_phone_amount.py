# Generated by Django 3.2.15 on 2022-11-15 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='count',
            new_name='amount',
        ),
    ]
