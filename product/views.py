from product.forms import CategoryForm
from django.shortcuts import redirect, render
from .models import Category


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


def update_categories(request, id):
    categories = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=categories)
    if form.is_valid():
        form.save()
        return redirect('list_categories')
    return render(request, 'form.html', {'form':form})

def delete_categories(request, id):
    categories = Category.objects.get(id=id)
    categories.delete()
    return redirect('list_categories')
    

def create_categories(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_categories')
    return render(request, 'form.html', {'form': form})