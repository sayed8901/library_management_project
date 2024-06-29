from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from .constants import ACTIVITY_TYPE


# Create your models here.
class Activity(models.Model):
    user = models.ForeignKey(User, related_name='activity_user', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='activity_book', on_delete=models.CASCADE)

    activity_type = models.CharField(max_length=10)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.activity_type} {self.book.book_name}'
    

