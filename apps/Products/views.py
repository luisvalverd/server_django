from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView, UpdateView 

from .models import Products
from .forms import CreateProductForm

# Create your views here.

class ProdutctListView(ListView):
    model = Products
    context_object_name = 'list_products'
    template_name = 'Products/list-products.html'


class ProductDelete(DeleteView):
    model = Products
    template_name = 'Products/delete-product.html'
    success_url = "/products"
    pk_url_kwarg = "id"

class ProductUpdate(UpdateView):
    model = Products
    fields = "__all__"
    template_name = 'Products/update-product.html'
    success_url = "/products"
    pk_url_kwarg = "id"

# functiion form

def create_product(request):

    form = CreateProductForm()

    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/products")

    context = {'form': form}

    return render(request, 'Products/create-product.html', context)

# * delete ussing functions
"""
def delete_product(request, id):
    product_inst = get_object_or_404(Products, id = id)

    product_inst.delete()

    return redirect("/products") 
"""