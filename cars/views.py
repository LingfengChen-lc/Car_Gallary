from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth.models import User
from cars.models import Car


def Success (request):
    return HttpResponse("Successfully uploaded")

def index(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Success/')   #/Success/ not correct!
    else:
        form = CarForm()
    return render(request, 'cars/car_image.html',{'form':form})

def Gallary(request):
    if request.method == 'GET':
        car_images = Car.objects.all()  #filter argument could be any fields in Car object
        context = {'car_images': car_images}
        return render(request, 'cars/gallary.html', context)
    return HttpResponse("Welcome to the home page")

# def display_car_images(request):
#     if request.method == 'GET':
#         Cars = Car.objects.all()
#         context = {'car_images' : Cars}
#         return render(request, 'display_car_image', context)

