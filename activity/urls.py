from django.urls import path
from .views import borrow_book, return_book, borrowed_books, activity_report

urlpatterns = [  
    path('borrow/<int:book_id>/<int:user_id>/', borrow_book, name='borrow_book'),
    path('return/<int:book_id>/<int:user_id>/', return_book, name='return_book'),

    path('borrowed_books/<int:user_id>/', borrowed_books, name='borrowed_books'),
    path('activity_report/<int:user_id>/', activity_report, name='activity_report'),
]
