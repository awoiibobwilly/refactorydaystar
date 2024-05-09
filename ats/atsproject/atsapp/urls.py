from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexats'),
    path('home/', views.home, name='homeats'),
    path('babycheckin/', views.babycheckin, name='babycheckinats'),
    path('babycheckout/', views.babycheckout, name='babycheckoutats'),
    path('babylist/', views.babylist, name='babylistats'),
    path('babyregistration/', views.babyregistration, name='babyregistrationats'),
    path('bcheckinrecord/', views.bcheckinrecord, name='bcheckinrecordats'),
    path('bcheckoutrecord/', views.bcheckoutrecord, name='bcheckoutrecordats'),
    path('editinfo/', views.editinfo, name='editinfoats'),
    path('financereport/', views.financereport, name='financereportats'),
    path('inventory/', views.inventory, name='inventoryats'),
    path('login/', views.login, name='loginats'),
    path('purchaseorder/', views.purchaseorder, name='purchaseorderats'),
    path('salesorder/', views.salesorder, name='salesorderats'),
    path('salesreport/', views.salesreport, name='salesreportats'),
    path('sitterlist/', views.sitterlist, name='sitterlistats'),
    path('sitterregistration/', views.sitterregistration, name='sitterregistrationats'),
    path('dashboard/', views.dashboard, name='dashboardats'),
    path('<str:pages>', views.daycare, name='daycare'),
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