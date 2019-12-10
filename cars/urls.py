from django.urls import path
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
# from .views import *
from . import views

urlpatterns = [
    # /cars/
    path('', views.index, name='car'),
    # path('image_upload', views.car_image_view, name = 'image_upload'), 
    path('Success/', views.Success, name = 'success'), 
    path('Gallary/', views.Gallary, name = 'gallary'),
]