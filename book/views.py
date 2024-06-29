from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Book, Review
from .forms import BookForm, ReviewForm
from activity.models import Activity

# necessary importing for class view implementation
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

# to use login required decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('homepage')




# detailsView class
class DetailBookView(DetailView):
    model = Book
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'

    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(data = self.request.POST)
        book = self.get_object() # current book er ekta object

        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = self.request.user
            new_review.book = book
            new_review.save()
        
        return self.get(request, *args, **kwargs)


    # to get reviews data as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()

        reviews = book.review_book.all()
        review_form = ReviewForm

        # to identify the user_has_borrowed the current book
        user_has_borrowed = False
        if self.request.user.is_authenticated:
            user_has_borrowed = Activity.objects.filter(
                user=self.request.user, book=book, activity_type='Borrowed'
            ).exists()
        
        context['reviews'] = reviews
        context['review_form'] = review_form
        context['user_has_borrowed'] = user_has_borrowed

        return context

