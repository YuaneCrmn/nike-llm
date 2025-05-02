from django.urls import path
from . import views

urlpatterns = [
    path('shirts/', views.ShirtListCreate.as_view(), name='shirt-create'),
    path('shirts/delete/<int:pk>/', views.ShirtListDelete.as_view(), name='shirt-delete'),
]