from django.views.generic import CreateView
from django.contrib import messages

from django.urls import reverse_lazy

# importing LoginRequiredMixin to protect TransactionCreateMixin class so that only a logged in user can view these...
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Transaction
from .forms import DepositForm

# to implement email sending functionality
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string





# creating a function to use send email functionality for transactions
def send_transaction_email(user, amount, subject, template):
    send_email = EmailMultiAlternatives(subject, '', to = [user.email])
    message = render_to_string(template, {
        'user': user,
        'amount' : amount,
    })
    send_email.attach_alternative(message, 'text/html')

    send_email.send()




# Create your views here.
class DepositMoneyView(LoginRequiredMixin, CreateView):
    form_class = DepositForm
    model = Transaction
    template_name = 'deposit_form.html'
    success_url = reverse_lazy('homepage')

    title = 'Deposit'


    # kono transaction er somoy, user er account ta transaction form e pass kore dite..
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account
        })

        return kwargs
    

    # template e 'title' ke context data hishebe pass korte...
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title,
        })

        return context
    


    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        account.balance += amount

        account.save(
            update_fields=['balance',] # saving updated balance field
        )
        

        # messages to show from frontend
        messages.success(
            self.request,
            f'{amount}$ has been deposited to your account successfully.'
        )


        # mail sending implementation for deposit message
        send_transaction_email(self.request.user, amount, 'Deposit Message', 'deposit_email.html')


        return super().form_valid(form) # finally, parent ke overwrite kore uporer kajgulo define kore save kore dicchi
    
    
