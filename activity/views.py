from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from book.models import Book
from activity.models import Activity

from django.contrib.auth.models import User

# to implement email sending functionality
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string




def book_activity_email(user, book, amount, subject, template):
    send_email = EmailMultiAlternatives(subject, '', to = [user.email])
    message = render_to_string(template, {
        'book': book,
        'user': user,
        'amount' : amount,
    })
    send_email.attach_alternative(message, 'text/html')

    send_email.send()




# Create your views here.
def borrow_book(request, book_id, user_id):
    target_book = Book.objects.get(pk = book_id)

    # getting current user 
    current_user = User.objects.get(pk = user_id)
    # getting UserAccount model by using related_name 'account'
    print(current_user.account.balance)
    print(target_book.price)
    

    if target_book.quantity < 1:
        messages.warning(request, 'You can not borrow this book as there are no more copy available to borrow')
        return redirect('homepage')
    
    if current_user.account.balance < target_book.price:
        messages.warning(request, 'You can not borrow this book as you dont have enough money to borrow')
        return redirect('homepage')

    if target_book.quantity > 0 and current_user.account.balance >= target_book.price:
        # decreasing book quantity
        target_book.quantity -= 1
        target_book.save()
        
        # decreasing user balance
        current_user.account.balance -= target_book.price
        current_user.account.save()


        # creating a new book borrowing order
        book_borrow_order = Activity.objects.create(
            user = request.user,
            book = target_book,
            activity_type = 'Borrowed',
        )
        book_borrow_order.save()
        print(book_borrow_order)

        book_activity_email(request.user, target_book, target_book.price, 'Borrow Book Message', 'borrow_book_email.html')

        messages.success(request, 'Book borrowing successful.')
        return redirect('homepage')

    messages.error(request, 'An unexpected error occurred.')
    return redirect('homepage')




def return_book(request, book_id, user_id):
    target_book = Book.objects.get(pk = book_id)

    # getting current user 
    current_user = User.objects.get(pk = user_id)
    # getting UserAccount model by using related_name 'account'
    print(current_user.account.balance)
    print(target_book.price)
    
    # increasing book quantity
    target_book.quantity += 1
    target_book.save()
        
    # increasing user balance
    current_user.account.balance += target_book.price
    current_user.account.save()


    # getting target_activity
    target_activity_list = Activity.objects.filter(
        user = current_user, activity_type = 'Borrowed', book = target_book
    )
    target_activity = target_activity_list[0]

    # updating activity type of the target_book of current user rather that creating a new activity
    target_activity.activity_type = 'Returned'
    target_activity.save()

    messages.success(request, 'Book returned successfully.')

    book_activity_email(request.user, target_book, target_book.price, 'Book Returning Message', 'return_book_email.html')

    return redirect('homepage')




def borrowed_books(request, user_id):
    # getting current user
    current_user = User.objects.get(pk = user_id)
    
    # getting all the books borrowed by this user
    target_books = Activity.objects.filter(
        user = current_user, activity_type = 'Borrowed'
    )
    print(target_books.count())

    return render(request, 'borrowed_books.html', {'data': target_books})




# creating activity history report views
def activity_report(request, user_id):
    # getting current user
    current_user = User.objects.get(pk = user_id)
    
    # getting all the books borrowed by this user
    target_activities = Activity.objects.filter(
        user = current_user,
    )
    print(target_activities.count())

    return render(request, 'activity_report.html', {'data': target_activities})

