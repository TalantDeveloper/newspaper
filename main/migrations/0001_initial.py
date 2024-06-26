# Generated by Django 5.0.6 on 2024-05-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nomi')),
                ('content', models.TextField(verbose_name='Tafsilot')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Rasm')),
                ('file', models.FileField(upload_to='file/', verbose_name='Jurnal')),
            ],
        ),
    ]
