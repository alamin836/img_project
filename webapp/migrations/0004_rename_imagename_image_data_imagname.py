# Generated by Django 4.2.6 on 2023-10-06 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_image_name_image_data_imagename_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_data',
            old_name='Imagename',
            new_name='Imagname',
        ),
    ]
