from django.http import HttpResponse, HttpResponseRedirect
# from .forms import Baby_RegistrationForm, Sitter_RegistrationForm, CheckinForm, CheckoutForm, Purchase_OrderForm, Sales_OrderForm
# from .models import Stay_Choice, Baby_Registration, Sitter_Registration, Baby_Fee, Checkin, Sitter_Fee, Checkout, Purchase_Order, Sales_Order 
from django.urls import reverse

atspages = {'loggin': 'You Can Log In Page', 'homepage': 'This ia Landing Page','babreg': 'This is Baby Registration Page', 'sitreg': 'This is Sitter Registration Page', 'checkin': 'This is Check In Page', 'checkout': 'This is Check Out Page', 'sales': 'This is Sales Creation Page', 'purchases': 'This is Purchase Management', 'edit':'This page is for editing purposes', 'finrec': 'This is Financial Records Management Page','summary': 'This is information summary page', 'bablist': 'This is a list of Babies', 'sitlist': 'This is a list of Sitters', 'saleslist': 'This is a list of Sales Records', 'inventory': 'This is a list of Inventory', 'checkinrec': 'This is a list of Checkins', 'checkoutrec': 'This is a list of Check outs'}
# Create your views here.
def daycare(request,pages):
    daystar = atspages.get(pages)
    print(daycare)
    return HttpResponse(daystar)

def index(request):
    return HttpResponse('<h1>This is Index Page</h1>')
    
