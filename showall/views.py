from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from .choices import price_choices, bedroom_choices, state_choices

from .models import Showall
from .forms import PropertyForm

def listings(request):
    properties = Showall.objects.all()
    # count = 1
    # images = []
    # for i in properties:
    #     if count == 1:
    #         images = i.images.all()
    #         count = count + 1
    # print(images[0].image)
    return render(request, 'properties/listings.html', {'properties': properties,})

def listing(request, id):
    property = Showall.objects.get(id=id)
    #images = property.images.all()

    context={
        'property': property,
        #'images':images

    }
    return render(request,'properties/listing.html',context)


# def search(request):
#   queryset_list = Showall.objects.order_by('-list_date')
#
#   # Keywords
#   if 'keywords' in request.GET:
#     keywords = request.GET['keywords']
#     if keywords:
#       queryset_list = queryset_list.filter(description__icontains=keywords)
#
#   # City
#   if 'city' in request.GET:
#     city = request.GET['city']
#     if city:
#       queryset_list = queryset_list.filter(city__iexact=city)
#
#   # State
#   if 'state' in request.GET:
#     state = request.GET['state']
#     if state:
#       queryset_list = queryset_list.filter(state__iexact=state)
#
#   # Bedrooms
#   if 'bedrooms' in request.GET:
#     bedrooms = request.GET['bedrooms']
#     if bedrooms:
#       queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
#
#   # Price
#   if 'price' in request.GET:
#     price = request.GET['price']
#     if price:
#       queryset_list = queryset_list.filter(price__lte=price)
#
#   context = {
#     'state_choices': state_choices,
#     'bedroom_choices': bedroom_choices,
#     'price_choices': price_choices,
#     'listings': queryset_list,
#     'values': request.GET
#   }

  # return render(request, 'search.html', context)

def postproperty(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'properties/properties.html', {'form':form})
# Create your views here.
