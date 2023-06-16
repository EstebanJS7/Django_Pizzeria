# Generated by Django 3.2.19 on 2023-06-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('Basico', 'Básico'), ('Premium', 'Premium')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
