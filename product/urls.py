from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('categories', views.list_categories, name='list_categories'),
    path('create/', views.create_categories, name='create_categories'),
    path('delete/<int:id>', views.delete_categories, name='delete_category'),
    path('update/<int:id>', views.update_categories, name='update_category'),
    path('products', views.list_products, name='list_products'),
    path('create_product', views.create_products, name='create_product'),
    path('delete_product/<int:id>', views.delete_products, name='delete_product'),
    path('update_product/<int:id>', views.update_products, name='update_product'),
]

