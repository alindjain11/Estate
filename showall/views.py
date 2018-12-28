from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from .models import Showall
from .forms import PropertyForm
from django.views.generic import CreateView,UpdateView
from django.views.generic.edit import ModelFormMixin
from .decorators import user_authenticate
from django.utils.decorators import method_decorator


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

@method_decorator(user_authenticate, name='dispatch')
class postproperty(CreateView):
    model = Showall
    form_class = PropertyForm
    template_name = 'properties/properties.html'
    sucess_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.profile = self.request.user
        self.object.save()
        return super(postproperty, self).form_valid(form)
    # if request.method == 'POST':
    #     form = PropertyForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    # return render(request,'properties/properties.html', {'form':form})
# Create your views here.



def enquiries(request):
    return render(request, 'properties/enquiries.html')
