from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . forms import * 
from . models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from functools import partial

def email_user(email):
    print(f"Dear {email}, An invoice has been raised in your name. Please, if you have not placed any order, reachout to us for more information")


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))       
        else:
            messages.success(request, ('There was an error trying to login, please make sure you have a username and password'))
            return redirect('login')
    else:
        return render(request, 'atsapp/login.html', {})



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
   

def babyrecords (request):
    babylists = Baby_Register.objects.all()
    return render(request, 'atsapp/babylist.html', {'babylists':babylists})



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

def sitterrecords (request):
    sitterlists = Sitter_Register.objects.all()
    return render(request, 'atsapp/sitterlist.html', {'sitterlists':sitterlists})

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


def procure_item(request):
    submitted = False
    if request.method == 'POST':
        form = ProcurementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/purchaseorder?submitted=True')
    else:
        form = ProcurementForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'atsapp/purchaseorder.html', {'form':form, 'submitted':submitted})


def generate_sale(request):
    submitted = False
    if request.method == 'POST':
        form = Sales_OrderForm(request.POST)
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
    form = Sales_OrderForm()
    return render(request, 'atsapp/salesorder.html', {'form':form, 'submitted':submitted})






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

    

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    