from django.db import models

class IMAGE_DATA(models.Model):
    Imgname=models.CharField(max_length=200)
    Imgsrc=models.ImageField(upload_to="img/")
