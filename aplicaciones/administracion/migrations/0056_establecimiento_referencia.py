# Generated by Django 2.2.7 on 2021-04-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0055_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='establecimiento',
            name='referencia',
            field=models.CharField(default='', max_length=200),
        ),
    ]
