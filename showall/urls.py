from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', listings, name='listings'),
    path('<int:id>', listing, name='listing'),
    #path('search', search, name='search'),
    path('postproperty/', postproperty , name='postproperty'),

]
