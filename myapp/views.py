from django.shortcuts import render, redirect
from django.views import View
from products.models import CategoryScience, Category, Product
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q



# Create your views here.
def for_all_pages(request):
    category = Category.objects.all()
    science = CategoryScience.objects.all()
    return {"category":category, "science":science}

class IndexView(View):
    def get(self, request):
        # Barcha mahsulotlarni olish
        products = Product.objects.all()
        
        # Barcha kategoriyalarni olish
        category = Category.objects.all()
        
        # Barcha CategoryScience ob'ektlarini olish
        science = CategoryScience.objects.all()
        
        # Paginatsiya qilish
        paginator = Paginator(products, 6)  # Har bir sahifada 6 ta mahsulot
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        # Qidiruv funksiyasi
        q = request.GET.get('q', None)
        if q:
            filtered_products = Product.objects.filter(Q(name__icontains=q))
        else:
            filtered_products = products.order_by('-id')

        context = {
            "products": page_obj,  # Paginatsiya qilingan mahsulotlar
            "category": category,  # Kategoriyalar
            "science": science,  # Science kategoriyalari
            'article': page_obj,  # Maqolalar uchun paginatsiya obyekti
            'filtered_products': filtered_products,  # Qidiruv natijalari yoki barcha mahsulotlar
            'q': q,  # Qidiruv so'rovi
        }
        
        return render(request, "index.html", context)
    

class CategoryFilterView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        # Kategoriya ID orqali filterlash
        return Product.objects.filter(category_id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Barcha kategoriyalarni qo'shish
        context['category'] = Category.objects.all()
        return context
    
    
    
class ArticleListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        # Kategoriya ID orqali filterlash
        return Product.objects.filter(category_id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Barcha CategoryScience ob'ektlarini qo'shish
        context['science'] = CategoryScience.objects.all()
        return context