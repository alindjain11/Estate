from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', listings, name='listings'),
    path('<int:id>', listing, name='listing'),
    path('postproperty/', login_required(postproperty.as_view()), name='postproperty'),
    path('enquiries/', enquiries,  name='enquiries', ),
    # path('postproperty/', postproperty , name='postproperty'),

]
