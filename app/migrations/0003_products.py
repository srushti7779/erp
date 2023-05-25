# Generated by Django 4.1.7 on 2023-04-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_product_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('typeOfProduct', models.CharField(choices=[('console-table', 'console-table'), ('bench', 'bench'), ('dinning-table', 'dinning-table'), ('side-table', 'side-table'), ('coffee-table', 'coffee-table'), ('pedestal-light', 'pedestal-light')], default='bench', max_length=14)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='productImage')),
                ('image2', models.ImageField(upload_to='productImage')),
            ],
        ),
    ]