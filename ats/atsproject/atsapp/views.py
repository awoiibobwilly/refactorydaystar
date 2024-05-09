from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import Baby_RegistrationForm, Sitter_RegistrationForm, CheckinForm, CheckoutForm, Purchase_OrderForm, Sales_OrderForm
# from .models import Baby_Registration, Sitter_Registration, Checkin, Checkout, Purchase_Order, Sale_Order
from django.urls import reverse


# from .forms import Baby_RegistrationForm, Sitter_RegistrationForm, CheckinForm, CheckoutForm, Purchase_OrderForm, Sales_OrderForm
# from .models import Stay_Choice, Baby_Registration, Sitter_Registration, Baby_Fee, Checkin, Sitter_Fee, Checkout, Purchase_Order, Sales_Order 
# from django.urls import reverse

# atspages = {'loggin': 'You Can Log In Page', 'homepage': 'This ia Landing Page','babreg': 'This is Baby Registration Page', 'sitreg': 'This is Sitter Registration Page', 'checkin': 'This is Check In Page', 'checkout': 'This is Check Out Page', 'sales': 'This is Sales Creation Page', 'purchases': 'This is Purchase Management', 'edit':'This page is for editing purposes', 'finrec': 'This is Financial Records Management Page','summary': 'This is information summary page', 'bablist': 'This is a list of Babies', 'sitlist': 'This is a list of Sitters', 'saleslist': 'This is a list of Sales Records', 'inventory': 'This is a list of Inventory', 'checkinrec': 'This is a list of Checkins', 'checkoutrec': 'This is a list of Check outs'}
# # Create your views here.
def daycare(request,pages):
    daystar = atspages.get(pages)
    print(daycare)
    return HttpResponse(daystar)

def index(request):
    return render(request, 'atsapp/index.html')

def home(request):
    return render(request, 'atsapp/home.html')

# def babycheckin(request):

#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         babin_form = CheckinForm(request.POST)
#         # check whether it's valid:
#         if babin_form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/babycheckin/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         babin_form = CheckinForm()

#     return render(request, 'atsapp/babycheckin.html', {'babin_form': babin_form})
    


# def babycheckout(request):

#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         babout_form = CheckoutForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/babycheckout/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         babout_form = CheckoutForm()

#     return render(request, 'atsapp/babycheckout.html', {'babout_form': babout_form})



def babylist(request):
    return render(request, 'atsapp/babylist.html')



# def babyregistration(request):

#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         babyreg_form = Baby_RegistrationForm(request.POST)
#         # check whether it's valid:
#         if babyreg_form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/babyregistration/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         babyreg_form = Baby_RegistrationForm()

#         return render(request, 'atsapp/babyregistration.html', {'babyreg_form': babyreg_form})



def bcheckinrecord(request):
    return render(request, 'atsapp/bcheckinrecord.html')

def bcheckoutrecord(request):
    return render(request, 'atsapp/bcheckoutrecord.html')

def editinfo(request):
    return render(request, 'atsapp/editinfo.html')

def financereport(request):
    return render(request, 'atsapp/financereport.html')

def inventory(request):
    return render(request, 'atsapp/inventory.html')

def login(request):
    return render(request, 'atsapp/login.html')

# def purchaseorder(request):

#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         po_form = Purchase_OrderForm(request.POST)
#         # check whether it's valid:
#         if po_form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/purchaseorder/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         po_form = Purchase_OrderForm()

#     return render(request, 'atsapp/purchaseorder.html', {'po_form': po_form})

# def salesorder(request):

#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         so_form = Sales_OrderForm(request.POST)
#         # check whether it's valid:
#         if so_form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/salesorder/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         so_form = Sales_OrderForm()

#     return render(request, 'atsapp/salesorder.html', {'so_form': so_form})



def salesreport(request):
    return render(request, 'atsapp/salesreport.html')



def sitterlist(request):
    return render(request, 'atsapp/sitterlist.html')



# def sitterregistration(request):

#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         sitreg_form = Sitter_RegistrationForm(request.POST)
#         # check whether it's valid:
#         if sitreg_form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/sitterregistration/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         sitreg_form = Sitter_RegistrationForm()

#     return render(request, 'atsapp/sitterregistration.html', {'sitreg_form': sitreg_form})



def dashboard(request):
    return render(request, 'atsapp/dashboard.html')





def index(request):
    return render(request, 'atsapp/index.html')

def home(request):
    return render(request, 'atsapp/home.html')

def babycheckin(request):
    return render(request, 'atsapp/babycheckin.html')

def babycheckout(request):
    return render(request, 'atsapp/babycheckout.html')

def babylist(request):
    return render(request, 'atsapp/babylist.html')

def babyregistration(request):
    return render(request, 'atsapp/babyregistration.html')

def bcheckinrecord(request):
    return render(request, 'atsapp/bcheckinrecord.html')

def bcheckoutrecord(request):
    return render(request, 'atsapp/bcheckoutrecord.html')

def editinfo(request):
    return render(request, 'atsapp/editinfo.html')

def financereport(request):
    return render(request, 'atsapp/financereport.html')

def inventory(request):
    return render(request, 'atsapp/inventory.html')

def login(request):
    return render(request, 'atsapp/login.html')

def purchaseorder(request):
    return render(request, 'atsapp/purchaseorder.html')

def salesorder(request):
    return render(request, 'atsapp/salesorder.html')

def salesreport(request):
    return render(request, 'atsapp/salesreport.html')

def sitterlist(request):
    return render(request, 'atsapp/sitterlist.html')

def sitterregistration(request):
    return render(request, 'atsapp/sitterregistration.html')

def dashboard(request):
    return render(request, 'atsapp/dashboard.html')

    

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    