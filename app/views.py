from django.shortcuts import render
from .models import *

# Create your views here.
def erp(request):
    return render(request, 'app/erp.html')

def home(request):
    return render(request, 'app/index.html')

def projectcategory(request):
    return render(request, 'app/projectscategory.html')

def projectimages(request,type):
    project = Project.objects.filter(category=type)
    return render(request, 'app/projectimages.html',{"project":project})

def products(request):
    return render(request, 'app/products.html')

def subproducts(request,type):
    product = Products.objects.filter(typeOfProduct=type)
    return render(request, 'app/subproducts.html',{"product":product})

def productdescription(request,id):
    product = Products.objects.get(id=id)
    return render(request, 'app/productdescription.html',{"product":product})


def aboutus(request):
    return render(request, 'app/aboutus.html')

def contact(request):
    return render(request, 'app/contact.html')