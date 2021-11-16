# Generated by Django 2.2.7 on 2020-12-17 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0021_auto_20201208_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id_red', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('enlace', models.CharField(max_length=400)),
                ('icono', models.ImageField(upload_to='')),
                ('id_empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='DireccionEntrega',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=250)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.Cliente')),
            ],
        ),
    ]