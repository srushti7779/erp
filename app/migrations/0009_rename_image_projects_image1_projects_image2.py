# Generated by Django 4.1.7 on 2023-04-26 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_projects_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='projects',
            name='image2',
            field=models.ImageField(default=None, upload_to='projectsImage'),
            preserve_default=False,
        ),
    ]
