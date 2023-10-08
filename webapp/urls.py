from django.urls import path
from .import views
urlpatterns=[
    path("",views.upload_img,name="upload"),
    path("upload",views.upload_database,name="upload_data"),
    path("show",views.show_img,name="showlink"),

]