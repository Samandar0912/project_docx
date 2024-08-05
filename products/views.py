from django.shortcuts import render, redirect
from .forms import NewProductForm, ProdctForm
from .models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def new_product(request):
    if request.method == "GET":
        form = NewProductForm()
        return render(request, 'product_create.html', {'form': form})
    
    elif request.method == 'POST':
        form = NewProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(request=request)  # request argumentini qo'shamiz
            return redirect('main:index')
        
        return render(request, 'product_create.html', {'form': form})
    
    
def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product':product})



@login_required(login_url='login')
def product_update(request,pk):
    if request.user == Product.Author:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'GET':
            form = ProdctForm(instance=product)
            return render(request, 'product_update.html', {'form':form})
        elif request.method == 'POST':
            form = ProdctForm(instance=product, data=request.POST, files=request.FILES)
            form.is_valid()
            form.save()
            return redirect('products:detail', pk)
        return render(request, 'product_update.html', {'form':form})

    else:
        return redirect('main:index')    
    
        
def product_delate(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.Author:
        if request.method == 'POST':
            product.delete()
            return redirect('main:index')    
        return render(request, 'product_delate.html', {'product':product})
    else:
        return redirect('main:index')    