from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_categories, name='list_categories'),
]
