from django.shortcuts import render, redirect
from django.views import View
from django.views import generic

from products.models import CategoryScience, Category, Product

# Create your views here.
def for_all_pages(request):
    category = Category.objects.all()
    science = CategoryScience.objects.all()
    return {"category":category, "science":science}

class IndexView(View):
    def get(self,request):
        products = Product.objects.all()
        category = Category.objects.all()
        science = CategoryScience.objects.all()
        context = {
            "products":products,
            "category":category,
            "science":science,
        }
        return render(request, "index.html", context)
    
class ModelDetailView(generic.DetailView):
    def get(self, request):
        products = Product.objects.all()
        category = Category.objects.all()
        science = CategoryScience.objects.all()
        context = {
            "products":products,
            "category":category,
            "science":science,
        }  
        return render(request, "block/see.html", context)
