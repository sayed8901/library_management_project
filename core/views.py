from django.shortcuts import render
from django.views.generic import TemplateView
from category.models import Category
from book.models import Book


# Create your views here.

# Creating TemplateView
# class HomeView(TemplateView):
#     template_name = 'index.html'
    

def home(request, category_slug = None):
    book_data = Book.objects.all()        # sob book gula ke anlam
    categories = Category.objects.all()        # sob category gulo anlam

    if category_slug is not None:
        target_category = Category.objects.get(slug = category_slug)
        book_data = Book.objects.filter(category_name = target_category)

    return render(request, 'index.html', {'data' : book_data, 'category' : categories})


