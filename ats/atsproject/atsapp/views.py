from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . forms import * 
from . models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as my_login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from functools import partial
import calendar
from calendar import HTMLCalendar
from django.db.models import F, Sum


# def searchbabies(request):
#     form = Baby_RegisterForm()
#     results = []
#     if request.method == 'GET':
#         search = request.GET.get('searched')
#         if search:
#             babiz_sur_name = Baby_Register.objects.filter(babiz_sur_name__icontains=search)
#         return render(request, 'atsapp/search.html', {'babiz_sur_name': babiz_sur_name})
#     else:
#         print('The Baby you are trying to search is not available, please try with another name.')
#         return request(request, 'atsapp/search.html', {})

# def searchbabies(request):
#     form = Baby_RegisterForm()
#     results = []
#     if request.method == 'GET':
#         form = Baby_RegisterForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Baby.objects.filter(Q(babiz_sur_name__icontains=query) | Q(babiz_other_names__icontains=query))
#     return render(request, 'search.html', {'form':form, 'results':results})

def email_user(email):
    print(f"Dear {email}, An invoice has been raised in your name. Please, if you have not placed any order, reachout to us for more information")


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            my_login(request, user)
            return redirect(reverse('home'))       
        else:
            messages.success(request, ('There was an error trying to login, please make sure you have a username and password'))
            return redirect('login')
    else:
        return render(request, 'atsapp/login.html', {})


@login_required
def baby_registration(request):
    submitted = False
    if request.method == 'POST':
        form = Baby_RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/babyregistration?submitted=True')    
    else:
        form = Baby_RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'atsapp/babyregistration.html', {'form':form, 'submitted':submitted})

@login_required
def deletbabies(request, baby_id):
    Baby_Register.objects.filter(id=baby_id).delete()
    return redirect('babylist')

# def editbabies(request, baby_id):
#     baby= Baby_Register.objects.get(id=baby_id)
#     if request.method == 'POST':
#         form = Baby_RegisterForm(request.POST)
#         if form.is_valid():
#             baby.save()
#             redirect_url = reverse('baby_registration')
#             return HttpResponseRedirect(redirect_url)
#     else:
#         form = Baby_RegisterForm()
#         return render(request, 'atsapp/editinfo.html', {'form': form, 'baby_id': baby_id})


@login_required
def editbabies(request, baby_id):
    baby = get_object_or_404(Baby_Register, pk=baby_id)
    if request.method == 'POST':
        form = Baby_RegisterForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            return redirect('babylist')
    else:
        form = Baby_RegisterForm(instance=baby)
    return render(request, 'atsapp/editinfo.html', {'form':form})

   
@login_required
def babyrecords (request):
    babylists = Baby_Register.objects.all()
    return render(request, 'atsapp/babylist.html', {'babylists':babylists})


@login_required
def sitter_registration(request):
    submitted = False
    if request.method == 'POST':
        form = Sitter_RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sitterregistration?submitted=True')
    else:
        form = Sitter_RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'atsapp/sitterregistration.html', {'form':form, 'submitted':submitted})

@login_required
def sitterrecords(request):
    sitterlists = Sitter_Register.objects.all()
    return render(request, 'atsapp/sitterlist.html', {'sitterlists': sitterlists})
    
@login_required
def deletesitters(request, sitter_id):
    Sitter_Register.objects.filter(id=sitter_id).delete()
    return redirect('sitterlist')

@login_required
def editsitters(request, sitter_id):
    sitter = get_object_or_404(Sitter_Register, pk=sitter_id)
    if request.method == 'POST':
        form = Sitter_RegisterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('sitterlist')
    else:
        form = Sitter_RegisterForm(instance=sitter)
    return render(request, 'atsapp/editinfo.html', {'form':form})
# @login_required
# def editbaby(request):
#     submitted = False
#     if request.method == 'POST':
#         form = Sitter_RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/sitterregistration?submitted=True')
#     else:
#         form = Sitter_RegisterForm()
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'atsapp/sitterregistration.html', {'form':form, 'submitted':submitted})


    
# @login_required
# def sitterrecords (request):
#     sitterlists = Sitter_Register.objects.all()
#     return render(request, 'atsapp/sitterlist.html', {'sitterlists':sitterlists})

    


@login_required
def sitter_presence(request):
    submitted = False
    if request.method == 'POST':
        form = Sitter_StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sitterstatus?submitted=True')
    else:
        form = Sitter_StatusForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'atsapp/sitterstatus.html', {'form':form, 'submitted':submitted})
@login_required
def baby_checkin(request):
    submitted = False
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/babycheckin?submitted=True')
    else:
        form = CheckinForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'atsapp/babycheckin.html', {'form':form, 'submitted':submitted})

@login_required
def bcheckin_list(request):
    checkinlist = Checkin.objects.all()
    return render(request, 'atsapp/bcheckinrecord.html', {'checkinlist': checkinlist})
    
@login_required
def delete_checkin(request, checkin_id):
    Checkin.objects.filter(id=checkin_id).delete()
    return redirect('bcheckinrecord')

@login_required
def edit_checkin(request, checkin_id):
    checkin = get_object_or_404(Checkin, pk=checkin_id)
    if request.method == 'POST':
        form = CheckinForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            return redirect('bcheckinrecord')
    else:
        form = CheckinForm(instance=checkin)
    return render(request, 'atsapp/editinfo.html', {'form':form})

@login_required
def bcheckout_list(request):
    checkoutlist = Checkout.objects.all()
    return render(request, 'atsapp/bcheckoutrecord.html', {'checkoutlist': checkoutlist})

@login_required
def baby_checkout(request):
    submitted = False
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/babycheckout?submitted=True')
    else:
        form = CheckoutForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'atsapp/babycheckout.html', {'form':form, 'submitted':submitted})

@login_required
def delete_checkout(request, checkout_id):
    Checkout.objects.filter(id=checkout_id).delete()
    return redirect('bcheckoutrecord')

@login_required
def edit_checkout(request, checkout_id):
    checkout = get_object_or_404(Checkout, pk=checkout_id)
    if request.method == 'POST':
        form = CheckoutForm(request.POST, instance=checkout)
        if form.is_valid():
            form.save()
            return redirect('bcheckoutrecord')
    else:
        form = CheckoutForm(instance=checkout)
    return render(request, 'atsapp/editinfo.html', {'form':form})

@login_required
def sitterrecords(request):
    sitterlists = Sitter_Register.objects.all()
    return render(request, 'atsapp/sitterlist.html', {'sitterlists': sitterlists})
    
@login_required
def deletesitters(request, sitter_id):
    Sitter_Register.objects.filter(id=sitter_id).delete()
    return redirect('sitterlist')

@login_required
def editsitters(request, sitter_id):
    sitter = get_object_or_404(Sitter_Register, pk=sitter_id)
    if request.method == 'POST':
        form = Sitter_RegisterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('sitterlist')
    else:
        form = Sitter_RegisterForm(instance=sitter)
    return render(request, 'atsapp/editinfo.html', {'form':form})

# @login_required
# def procure_item(request):
#     submitted = False
#     if request.method == 'POST':
#         form = ProcurementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/purchaseorder?submitted=True')
#     else:
#         form = ProcurementForm()
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'atsapp/purchaseorder.html', {'form':form, 'submitted':submitted})

# @login_required
# def generate_sale(request):
#     submitted = False
#     if request.method == 'POST':
#         form = Sales_OrderForm(request.POST)
#         if form.is_valid():
#             with transaction.atomic():
#                 order = form.save()
#                 # import sys
#                 # sys.exit(0)
#                 order.so_item_number.po_quantity -= order.so_quantity
#                 order.so_item_number.save()
#             transaction.on_commit(partial(email_user, 'mukoroberts@gmail.com'))
#             return redirect('/salesorder?submitted=True')
#         else:
#             return render(request, 'atsapp/salesorder.html', {'form':form})
#     form = Sales_OrderForm()
#     return render(request, 'atsapp/salesorder.html', {'form':form, 'submitted':submitted})


@login_required
def enterpurchase(request):
    submitted = False
    if request.method == 'POST':
        formp = PurchaseForm(request.POST)
        if formp.is_valid():
            formp.save()
            return HttpResponseRedirect('/purchaseorder?submitted=True')
    else:
        formp = PurchaseForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'atsapp/purchaseorder.html', {'formp':formp, 'submitted':submitted})

@login_required
def inventorylist(request):
    purchaselists = Purchase.objects.all()
    return render(request, 'atsapp/inventory.html', {'purchaselists': purchaselists})

@login_required
def edit_inventory(request, inventory_id):
    inventory = get_object_or_404(Purchase, pk=inventory_id)
    if request.method == 'POST':
        form_inventory = PurchaseForm(request.POST, instance=inventory)
        if form_inventory.is_valid():
            form_inventory.save()
            return redirect('inventory')
    else:
        form_inventory = PurchaseForm(instance=inventory)
    return render(request, 'atsapp/editinfo.html', {'form_inventory':form_inventory})


# @login_required
# def edit_inventory(request, inventory_id):
#     Purchase.objects.get(id=inventory_id)
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return redirect('inventory')

@login_required
def delete_inventory(request, inventory_id):
    Purchase.objects.filter(id=inventory_id).delete()
    return redirect('inventory')


@login_required
def entersale(request):
    submitted = False
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()
                # import sys
                # sys.exit(0)
                order.so_item_number.po_quantity -= order.so_quantity
                order.so_item_number.save()
            transaction.on_commit(partial(email_user, 'mukoroberts@gmail.com'))
            return redirect('/salesorder?submitted=True')
        else:
            return render(request, 'atsapp/salesorder.html', {'form':form})
    form = SalesForm()
    return render(request, 'atsapp/salesorder.html', {'form':form, 'submitted':submitted})

@login_required
def productsaleslist(request):
    saleslists = Sales.objects.all()
    return render(request, 'atsapp/salesreport.html', {'saleslists': saleslists})

@login_required
def delete_sales(request, sales_id):
    Sales.objects.filter(id=sales_id).delete()
    return redirect('salesreport')

@login_required
def edit_sales(request, sales_id):
    sales = get_object_or_404(Sales, pk=sales_id)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sales)
        if form.is_valid():
            form.save()
            return redirect('salesreport')
    else:
        form = SalesForm(instance=sales)
    return render(request, 'atsapp/editinfo.html', {'form':form})

@login_required
def finance_report(request):
    checkin_finance_report = Checkin.objects.all()
    checkout_finance_report = Checkout.objects.all()
    sales_finance_report = Sales.objects.all()
    purchases_finance_report = Purchase.objects.all()
    return render(request, 'atsapp/financereport.html', {'checkin_finance_report': checkin_finance_report, 'checkout_finance_report': checkout_finance_report, 'sales_finance_report': sales_finance_report, 'purchases_finance_report': purchases_finance_report})


def index(request):
    return render(request, 'atsapp/index.html')
# @login_required
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    # day = day.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    # day_number = list(calendar.day_name).index(day)
    month_number = int(month_number)
    # day_number = int(day_number)
    
    # Craete a Calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    #Get the current Year
    now = datetime.now()
    current_year = now.year

    #Get the current time
    # time = now.strftime('%I:%M:%S %p')
    time = now.strftime('%I:%M %p')
    return render(request, 'atsapp/home.html', {'year':year, 'month':month, 'month_number':month_number, 'cal':cal, 'current_year':current_year, 'time':time})



@login_required
def babycheckin(request):
    return render(request, 'atsapp/babycheckin.html')
@login_required
def babycheckout(request):
    return render(request, 'atsapp/babycheckout.html')
@login_required
def babylist(request):
    return render(request, 'atsapp/babylist.html')
@login_required
def babyregistration(request):
    return render(request, 'atsapp/babyregistration.html')
@login_required
def bcheckinrecord(request):
    return render(request, 'atsapp/bcheckinrecord.html')
@login_required
def bcheckoutrecord(request):
    return render(request, 'atsapp/bcheckoutrecord.html')
@login_required
def edit(request):
    return render(request, 'atsapp/editinfo.html')
@login_required
def financereport(request):
    return render(request, 'atsapp/financereport.html')
@login_required
def inventory(request):
    return render(request, 'atsapp/inventory.html')

def login(request):
    return render(request, 'atsapp/login.html')
@login_required
def purchaseorder(request):
    return render(request, 'atsapp/purchaseorder.html')
@login_required
def salesorder(request):
    return render(request, 'atsapp/salesorder.html')
@login_required
def salesreport(request):
    return render(request, 'atsapp/salesreport.html')
@login_required
def sitterlist(request):
    return render(request, 'atsapp/sitterlist.html')
@login_required
def sitterregistration(request):
    return render(request, 'atsapp/sitterregistration.html')
@login_required
def dashboard(request):
    return render(request, 'atsapp/dashboard.html')



@login_required
def logout_user(request):
    logout(request)
    return redirect('indexats')


@login_required
def general_counts_view(request):

    total_quantity_purchased = Purchase.purchase_total_quantity()

    total_babies = Baby_Register.objects.count()  # Count all babies registered

    total_baby_checkin = Checkin.objects.count()  # Count all babies checked in

    total_baby_checkout = Checkout.objects.count()  # Count all babies checked out

    total_sitters = Sitter_Register.objects.count()  # Count all sitters registered

    total_dolls = Purchase.objects.count()  # Count all sitters registered

    # Annotate each sale with the total price (quantity * unit_price)
    sales_with_total = Sales.objects.annotate(total_price=F('so_quantity') * F('so_unit_price'))
    # Calculate the grand total of all sales
    grand_total_sales = sales_with_total.aggregate(total_sales=Sum('total_price'))

    # Annotate each purchase with the total price (quantity * unit_price)
    purchases_with_total = Purchase.objects.annotate(total_price=F('po_quantity') * F('po_unit_cost'))
    # Calculate the grand total of all purchases
    grand_total_purchases = purchases_with_total.aggregate(total_purchases=Sum('total_price'))


    return render(request, 'atsapp/dashboard.html', {'total_babies': total_babies, 'total_sitters': total_sitters, 'total_dolls': total_dolls, 'grand_total_sales': grand_total_sales, 'grand_total_purchases': grand_total_purchases, 'total_quantity_purchased': total_quantity_purchased, 'total_baby_checkin': total_baby_checkin, 'total_baby_checkout': total_baby_checkout})


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    