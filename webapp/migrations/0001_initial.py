# Generated by Django 4.2.6 on 2023-10-06 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMAGE_DATA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('img_src', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
