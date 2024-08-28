from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import ProductForm
from .models import Product
# Create your views here.

#____ here we perfrom CRUD operations


def home_view(request):
    return render(request, 'invApp/home.html')

#create view form
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})


#read view
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html',{'products': products})

#update view
def product_update_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})

#delete view
def delete_product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    else:
        
        return HttpResponseNotAllowed(['POST'], "Only POST method allowed")
