# from product.forms import CategoryForm, ProductForm
# from django.shortcuts import redirect, render, get_object_or_404
# from .models import Category, Product


# def list_categories(request):
#     categories = Category.objects.all()
#     return render(request, 'category.html', {'categories': categories})


# def update_categories(request, id):
#     categories = Category.objects.get(id=id)
#     if request.method == 'POST':
#         form = CategoryForm(request.POST or None, instance=categories)
#         if form.is_valid():
#             form.save()
#         return redirect('list_categories')
#     return render(request, 'form.html', {'form':form})

# def delete_categories(request, id):
#     categories = Category.objects.get(id=id)
#     categories.delete()
#     return redirect('list_categories')
    

# def create_categories(request):
#     form = CategoryForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('list_categories')
#     return render(request, 'form.html', {'form': form})


# def list_products(request):
#     products = Product.objects.all()
#     return render(request, 'product.html', {'products': products})


# def update_products(request, id):
#     form = ProductForm(request.POST or None)
#     if request.method == 'POST':
#         products = Product.objects.get(id=id)
#         form = ProductForm(request.POST or None, instance=products)
#         if form.is_valid():
#             form.save()
#         return redirect('list_products')
#     return render(request, 'form.html', {'form':form})

# def delete_products(request,id):
#     get_object_or_404(Product, id=id).delete()
#     return redirect('list_products')
    

# def create_products(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('list_products')
#     return render(request, 'form.html', {'form': form})

# def index(request):
#     return render(request, 'base.html')

