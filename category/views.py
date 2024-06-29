from django.shortcuts import render
from . import models
from . import forms

# necessary importing for class view implementation
from django.views.generic import CreateView
from django.urls import reverse_lazy



# Create your views here.
class AddCategoryView(CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('homepage')

