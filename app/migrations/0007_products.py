# Generated by Django 4.1.7 on 2023-04-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('typeOfProduct', models.CharField(choices=[('console-table', 'console-table'), ('bench', 'bench'), ('dinning-table', 'dinning-table'), ('side-table', 'side-table'), ('coffee-table', 'coffee-table'), ('pedestal-light', 'pedestal-light')], default='bench', max_length=14)),
                ('description', models.TextField()),
                ('imagebw1', models.ImageField(default='1.jpg', upload_to='productImage')),
                ('imageclr2', models.ImageField(default='1.jpg', upload_to='productImage')),
                ('image3', models.ImageField(default='1.jpg', upload_to='productImage')),
                ('image4', models.ImageField(default='1.jpg', upload_to='productImage')),
            ],
        ),
    ]
