from django.urls import path
from .views import AddBookView, DetailBookView

urlpatterns = [
    path('add/', AddBookView.as_view(), name='add_book'),

    path('details/<int:id>/', DetailBookView.as_view(), name='detail_book_info'),
]
