from django.shortcuts import render,redirect
from .models import *

def upload_img(request):
    return render(request,"upload_img.html")

def upload_database(request):
    if request.method=='POST':
        imgvar=request.POST['imgname']
        imgsr=request.FILES['image']
        img_user=IMAGE_DATA.objects.create(Imgname=imgvar,Imgsrc=imgsr)
        return redirect('showlink')
    
def show_img(request):
    all_data=IMAGE_DATA.objects.all()
    return render(request,"show.html",{'key1':all_data})