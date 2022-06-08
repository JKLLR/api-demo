from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('item/<str:pk>/', views.singleData),
    path('update/<str:pk>/', views.updateItem),
    path('delete/<str:pk>/', views.deleteItem),
]