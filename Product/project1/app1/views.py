from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProductForm
from .models import Product
from django.contrib import admin
# Create your views here.


def home(request):
    form = ProductForm()
    template_name = 'app1/index.html'

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():

            form.save()
        form = ProductForm()
    

    data = Product.objects.all()

    context = {
        'form': form,
        'data': data,
    }

    return render(request, template_name, context)


def delete_record(request, id):
    a = Product.objects.get(pk=id)
    a.delete()
    return redirect('/')


# update view
def update_record(request, id):
    if request.method == 'POST':
        data = Product.objects.get(pk=id)
        form = ProductForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:

        data = Product.objects.get(pk=id)
        form = ProductForm(instance=data)

    context = {
        'form': form,
        
    }

    return render(request, 'app1/update.html', context)
