# Generated by Django 5.0.6 on 2024-05-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Nomi'),
        ),
    ]
