# Generated by Django 4.2.6 on 2023-10-06 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_data',
            old_name='image_name',
            new_name='Image_name',
        ),
        migrations.RenameField(
            model_name='image_data',
            old_name='img_src',
            new_name='Img_src',
        ),
    ]