# Generated by Django 3.0.9 on 2020-08-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20200815_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
