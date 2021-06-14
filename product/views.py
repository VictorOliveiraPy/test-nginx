from django.shortcuts import render
from .models import Category


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})
