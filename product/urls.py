from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_categories, name='list_categories'),
    path('create/', views.create_categories, name='create_categories'),
    path('delete/<int:id>', views.delete_categories, name='delete_category'),
    path('update/<int:id>', views.update_categories, name='update_category'),
]

