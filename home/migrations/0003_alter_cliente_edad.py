# Generated by Django 5.2 on 2025-05-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_cliente_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(max_length=3),
        ),
    ]
