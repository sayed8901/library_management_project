from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddCategoryView.as_view(), name='add_category'),
]
