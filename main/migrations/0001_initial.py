# Generated by Django 4.2.1 on 2023-05-17 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000, verbose_name="Bouquet's description")),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of flower')),
                ('amount', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=100, verbose_name='Color of flower')),
                ('description', models.TextField(max_length=1000, verbose_name="Flower's description")),
            ],
        ),
        migrations.CreateModel(
            name='BouquetFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('bouquets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bouquet', verbose_name='Bouquet')),
                ('flowers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.flower', verbose_name='Flower')),
            ],
        ),
        migrations.AddField(
            model_name='bouquet',
            name='flowers',
            field=models.ManyToManyField(through='main.BouquetFlowers', to='main.flower'),
        ),
    ]
