from django.db import models
from category.models import Category
from django.contrib.auth.models import User



# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    # One to many relationship with category
    category_name = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    # image field to save image in the car app's media folder    
    image = models.ImageField(upload_to='book/media/uploads/', blank = True, null = True)


    def __str__(self):
        return f'{self.book_name} - price: ${self.price} - available: {self.quantity} pcs.'




class Review(models.Model):
    book = models.ForeignKey(Book, related_name='review_book', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, related_name='review_user', on_delete=models.CASCADE, blank=True, null=True)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviews submitted on {self.created_on}"
    

