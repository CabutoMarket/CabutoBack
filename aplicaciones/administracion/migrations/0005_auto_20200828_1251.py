# Generated by Django 3.0.9 on 2020-08-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_auto_20200828_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
