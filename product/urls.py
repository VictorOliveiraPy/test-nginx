from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index),
    # path('categories', views.list_categories, name='list_categories'),
    # path('create/', views.create_categories, name='create_categories'),
    # path('delete_category/<int:id>', views.delete_categories, name='delete_category'),
    # path('update_category/<int:id>', views.update_categories, name='update_category'),
    # path('products', views.list_products, name='list_products'),
    # path('create_product', views.create_products, name='create_product'),
    # path('delete_product/<int:id>', views.delete_products, name='delete_product'),
    # path('update_product/<int:id>', views.update_products, name='update_product'),
    path('api/category/', views.CategoryList.as_view(), name='api-category'),
    path('api/category/<int:pk>/', views.CategoryDetail.as_view(),
         name='category'),
    path('api/product/', views.ProductList.as_view(), name='api_product'),
    path('api/product/<int:pk>/', views.ProductDetail.as_view()),
]
