from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexats'),
    path('home/', views.home, name='homeats'),
    path('sitterstatus/', views.sitter_presence, name='sitterstatusats'),
    path('babycheckin/', views.baby_checkin, name='babycheckinats'),
    path('babycheckout/', views.baby_checkout, name='babycheckoutats'),
    path('babylist/', views.babyrecords, name='babylist'),
    path('babyregistration/', views.baby_registration, name='babyregistrationats'),
    path('bcheckinrecord/', views.bcheckinrecord, name='bcheckinrecordats'),
    path('bcheckoutrecord/', views.bcheckoutrecord, name='bcheckoutrecordats'),
    path('editinfo/', views.editinfo, name='editinfoats'),
    path('financereport/', views.financereport, name='financereportats'),
    path('inventory/', views.inventory, name='inventoryats'),
    path('login/', views.login, name='loginats'),
    # path('signup/', views.signup, name='signupats'),
    path('purchaseorder/', views.procure_item, name='purchaseorderats'),
    path('salesorder/', views.generate_sale, name='salesorderats'),
    path('salesreport/', views.salesreport, name='salesreportats'),
    path('sitterlist/', views.sitterrecords, name='sitterlistats'),
    path('sitterregistration/', views.sitter_registration, name='sitterregistrationats'),
    path('dashboard/', views.dashboard, name='dashboardats'),
    
]

    # home
    # babycheckin
    # babycheckout
    # babylist
    # babyregistration
    # bcheckinrecord
    # bcheckoutrecord
    # editinfo
    # financereport
    # inventory
    # login
    # purchaseorder
    # salesorder
    # salesreport
    # sitterlist
    # sitterregistration
    # summary