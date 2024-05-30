from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexats'),
    path('babyregistration/', views.baby_registration, name='babyregistrationats'),
    path('deletbabies/<int:baby_id>', views.deletbabies, name='deletbabies'), 
    path('editbabies/<int:baby_id>/', views.editbabies, name='editbabies'),
    path('home/', views.home, name='home'),
    # path('<int:year>/<str:month>/<str:day>/', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('sitterstatus/', views.sitter_presence, name='sitterstatusats'),
    path('babycheckin/', views.baby_checkin, name='babycheckinats'),
    path('babycheckout/', views.baby_checkout, name='babycheckoutats'),
    path('babylist/', views.babyrecords, name='babylist'),
    path('bcheckinrecord/', views.bcheckinrecord, name='bcheckinrecordats'),
    path('bcheckoutrecord/', views.bcheckoutrecord, name='bcheckoutrecordats'),
    path('editinfo/', views.edit, name='editinfoats'),
    path('financereport/', views.financereport, name='financereportats'),
    path('inventory/', views.inventorylist, name='inventory'),
    path('login/', views.login_user, name='login'),
    # path('signup/', views.signup, name='signupats'),
    path('purchaseorder/', views.enterpurchase, name='purchaseorder'),
    path('salesorder/', views.entersale, name='salesorderats'),
    path('salesreport/', views.productsaleslist, name='salesreport'),
    path('sitterlist/', views.sitterrecords, name='sitterlist'),
    path('sitterregistration/', views.sitter_registration, name='sitterregistrationats'),
    path('editsitters/<int:sitter_id>/', views.editsitters, name='editsitters'),
    path('deletesitters/<int:sitter_id>/', views.deletesitters, name='deletesitters'), 
    path('dashboard/', views.dashboard, name='dashboardats'),
    # path('search/', views.searchbabies, name='search'),
    path('logout/', views.logout_user, name='logout'),
    
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