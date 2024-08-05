from django.shortcuts import render, redirect
from django.views import View
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
    

def categoryFilter(request,pk):
    products = Product.objects.filter(category_id=pk)
    category = Category.objects.all()
    
    context = {
        "category":category,
        "products":products,
    }
    return render(request, "index.html", context)


def articleFilter(request,pk):
    products = Product.objects.filter(category_id=pk)
    science = CategoryScience.objects.all()
    context = {
        "science":science,
        "products":products,
    }
    return render(request, "index.html", context)
    