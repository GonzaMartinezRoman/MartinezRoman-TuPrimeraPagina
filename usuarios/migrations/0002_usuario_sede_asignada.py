# Generated by Django 5.2 on 2025-05-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sede_asignada',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
