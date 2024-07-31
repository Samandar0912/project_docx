from django.shortcuts import render, redirect
from django.views import View
from products.models import Article, Category

# Create your views here.

class IndexView(View):
    def get(self,request):
        products = Article.objects.all()
        category = Category.objects.all()
        context = {
            "products":products,
            "category":category,
        }
        return render(request, "index.html", context)
    