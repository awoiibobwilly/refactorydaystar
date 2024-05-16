from django import forms
from django.forms import ModelForm
from .models import *

#This is Baby Registration Form

# class User_RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User_Registration
#         fields = ('username', 'email', 'new_password', 'confirm_password')
#         labels = {
#             'username':'Username',
#             'email':'Email',
#             'new_password':'New Password',
#             'confirm_password':'Confirm Password'}
#         widgets = {
#             'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'mukaroberts'}),
#             'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'mukaroberts@gmail.com'}),
#             'new_password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}),
#             'confirm_password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'})}
            



class Baby_RegisterForm(ModelForm):
    class Meta:
        model = Baby_Register
        fields = ('babiz_sur_name',  'babiz_other_names', 'babiz_gender', 'babiz_date_of_birth', 'parentz_sur_name', 'parentz_other_names', 'parentz_gender', 'parentz_date_of_birth',  'parentz_telephone', 'parentz_address', 'parentz_email')
        labels = {
            'babiz_sur_name':'Baby Surname',
            'babiz_other_names':'Baby Other Names',
            'babiz_gender':'Baby Gender',
            'babiz_date_of_birth':'Baby Date of Birth',
            'parentz_sur_name':'Parent Surname',
            'parentz_other_names':'Parent Other Names',
            'parentz_gender':'Parent Gender',
            'parentz_date_of_birth':'Parent Date of Birth',
            'parentz_telephone':'Parent Telephone',
            'parentz_address':'Parent Location',
            'parentz_email':'Parent Email'}
        widgets = {
            'babiz_sur_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vudriko'}),
            'babiz_other_names': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Trisher'}),
            'babiz_gender': forms.Select(attrs={'class': 'form-control', 'placeholder':'Female'}),
            'babiz_date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
            'parentz_sur_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mukasa'}),
            'parentz_other_names': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Roberts'}),
            'parentz_gender': forms.Select(attrs={'class': 'form-control', 'placeholder':'Male'}),
            'parentz_date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
            'parentz_telephone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'+256 772 772 772'}),
            'parentz_address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kabalagala'}),
            'parentz_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'mukaroberts@gmail.com'})}
        
        def __str__(self):
            return self.babiz_sur_name
       
#This is Baby Sitter Registration Form

class Sitter_RegisterForm(ModelForm):
    class Meta:
        model = Sitter_Register
        fields = ('sit_sur_name', 'sit_other_names', 'sit_gender', 'sit_date_of_birth', 'sit_nin_number', 'sit_educlevel', 'sit_religion', 'sit_address', 'sit_email', 'sit_telephone', 'snok_sur_name', 'snok_other_names', 'snok_gender', 'snok_date_of_birth', 'snok_address', 'snok_email', 'snok_telephone')
        labels = {
           'sit_sur_name':'Sitter Surname',
           'sit_other_names':'Sitter Other Names',
           'sit_gender':'Sitter Gender',
           'sit_date_of_birth':'Sitter Date of Birth',
           'sit_nin_number':'Sitter NIN Number',
           'sit_educlevel':'Sitter Education Level',
           'sit_religion':'Sitter Religion',
           'sit_address':'Sitter Address',
           'sit_email':'Sitter Email',
           'sit_telephone':'Sitter Telephone',
           'snok_sur_name':'Next Of Kin Surname',
           'snok_other_names':'Next Of Kin Other Names',
           'snok_gender':'Next Of Kin Gender',
           'snok_date_of_birth':'Next Of Kin Date of Birth',
           'snok_address':'Next Of Kin Address',
           'snok_email':'Next Of Kin Email',
           'snok_telephone':'Next Of Kin Telephone'}
        widgets = {
           'sit_sur_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vudriko'}),
           'sit_other_names': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Trisher'}),
           'sit_gender': forms.Select(attrs={'class': 'form-control', 'placeholder':'Female'}),
           'sit_date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
           'sit_nin_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'CF9912307FEGP'}),
           'sit_educlevel': forms.Select(attrs={'class': 'form-control', 'placeholder':'Some College'}),
           'sit_religion': forms.Select(attrs={'class': 'form-control', 'placeholder':'Anglican'}),
           'sit_address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kabalagala'}),
           'sit_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'mukaroberts@gmail.com'}),
           'sit_telephone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'+256 772 772 772'}),
           'snok_sur_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mukasa'}),
           'snok_other_names': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Roberts'}),
           'snok_gender': forms.Select(attrs={'class': 'form-control', 'placeholder':'Male'}),
           'snok_date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
           'snok_address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kabalagala'}),
           'snok_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'mukaroberts@gmail.com'}),
           'snok_telephone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'+256 772 772 772'})}
        
        def __str__(self):
            return self.sit_sur_name

class Sitter_StatusForm(ModelForm):
    class Meta:
        model = Sitter_Status
        fields = ('sitter_id', 'sitter_availability', 'sitter_time', 'sitter_date')
        labels = {
           'sitter_id':'Sitter ID Number',
           'sitter_availability':'Sitter Availability',
           'sitter_time':'Sitter Time',
           'sitter_date':'Sitter Date'}
        widgets = {
           'sitter_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'BDD0001'}),
           'sitter_availability': forms.Select(attrs={'class': 'form-control', 'placeholder':'On Duty'}),
           'sitter_time': forms.TextInput(attrs={'class':'form-control', 'placeholder':'10:00'}),
           'sitter_date': forms.DateInput(attrs={'class':'form-control','placeholder':'09/05/2024'})}
        
        def __str__(self):
            return self.sitter_id


class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ('baby_id', 'checkin_sitter_availability', 'checkin_time', 'checkin_date', 'checkin_care_time', 'checkin_guardians_sur_name', 'checkin_guardians_other_names', 'checkin_guardians_telephone', 'sitter_id', 'checkin_payment_choice','daystar_checkin_fee', 'daystar_checkin_fee_currency', 'checkin_comment')
        labels = {
            'baby_id':'Baby ID Number',
            'checkin_sitter_availability':'Sitter Availability',
            'checkin_time':'Checkin Time',
            'checkin_date':'Checkin Date',
            'checkin_care_time':'Care Time',
            'checkin_guardians_sur_name':'Guardians Surname',
            'checkin_guardians_other_names':'Guardians Other Names',
            'checkin_guardians_telephone':'Guardians Telephone',
            'checkin_payment_choice':'Payment Choice',
            'sitter_id':'Sitter ID Number',
            'daystar_checkin_fee':'Daystar Checkin Fee',
            'daystar_checkin_fee_currency':'Daystar Checkin Fee Currency',
            'checkin_comment':'Checkin Comment'}
        widgets = {
            'baby_id': forms.TextInput(attrs={'class':'form-control','placeholder':'BDD0001'}),
            'checkin_sitter_availability': forms.Select(attrs={'class':'form-control', 'placeholder':'On Duty'}),
            'checkin_time': forms.TimeInput(attrs={'class':'form-control','placeholder':'7:30 AM'}),
            'checkin_date': forms.DateInput(attrs={'class':'form-control','placeholder':'09/05/2024'}),
            'checkin_care_time': forms.Select(attrs={'class':'form-control','placeholder':'Morning'}),
            'checkin_guardians_sur_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Kizito'}),
            'checkin_guardians_other_names': forms.TextInput(attrs={'class':'form-control','placeholder':'Kenneth'}),
            'checkin_guardians_telephone': forms.TextInput(attrs={'class':'form-control','placeholder':'+256777777777'}),
            'checkin_payment_choice': forms.Select(attrs={'class': 'form-control','placeholder':'Daily'}),
            'sitter_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SDD0001'}),
            'daystar_checkin_fee': forms.TextInput(attrs={'class':'form-control','placeholder':'10,000'}),
            'daystar_checkin_fee_currency': forms.Select(attrs={'class': 'form-control','placeholder':'UGX'}),
            'checkin_comment': forms.Textarea(attrs={'class':'form-control','placeholder':'Thanks for your service'})}

        def __str__(self):
            return self.baby_id



class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        fields = ('baby_id', 'checkout_time', 'checkout_date', 'checkout_care_time', 'checkout_guardians_sur_name', 'checkout_guardians_other_names', 'checkout_guardians_telephone', 'sitter_id', 'checkout_payment_choice', 'daystar_care_time_fee', 'daystar_care_time_fee_currency', 'checkout_sitter_fee', 'checkout_sitter_fee_currency', 'checkout_comment')
        labels = {
            'baby_id':'Baby ID Number',
            'checkout_time':'Checkout Time',
            'checkout_date':'Checkout Date',
            'checkout_care_time':'Care Time',
            'checkout_guardians_sur_name':'Guardians Surname',
            'checkout_guardians_other_names':'Guardians Other Names',
            'checkout_guardians_telephone':'Guardians Telephone',
            'checkout_payment_choice':'Payment Choice',
            'sitter_id':'Sitter ID Number',
            'daystar_care_time_fee':'Daystar Care Time Fee',
            'daystar_care_time_fee_currency':'Daystar Care Time Fee Currency',
            'checkout_sitter_fee':'Checkout Sitter Fee',
            'checkout_sitter_fee_currency':'Checkout Sitter Fee Currency',
            'checkout_comment':'Checkout Comment'}
        widgets = {
            'baby_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'BDD0001'}),
            'checkout_time': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'7:30 AM'}),
            'checkout_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'09/05/2024'}),
            'checkout_care_time': forms.Select(attrs={'class':'form-control', 'placeholder':'Morning'}),
            'checkout_guardians_sur_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kizito'}),
            'checkout_guardians_other_names': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kenneth'}),
            'checkout_guardians_telephone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'+256777777777'}),
            'checkout_payment_choice': forms.Select(attrs={'class': 'form-control', 'placeholder':'Daily'}),
            'sitter_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SDD0001'}),
            'daystar_care_time_fee': forms.TextInput(attrs={'class':'form-control', 'placeholder':'10,000'}),
            'daystar_care_time_fee_currency': forms.Select(attrs={'class': 'form-control', 'placeholder':'UGX'}),
            'checkout_sitter_fee': forms.TextInput(attrs={'class':'form-control', 'placeholder':'10,000'}),
            'checkout_sitter_fee_currency': forms.Select(attrs={'class': 'form-control', 'placeholder':'UGX'}),
            'checkout_comment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Thanks for your service'})}

        def __str__(self):
            return self.baby_id

class ProcurementForm(ModelForm):
    class Meta:
        model = Procurement
        fields = ('po_item_number','po_product_name','po_unit_cost','po_purchase_date','po_entry_date','po_quantity','po_total_amount')
        labels = {
        'po_item_number':'Item Number',
        'po_product_name':'Product Name',
        'po_unit_cost':'Unit Cost',
        'po_purchase_date':'Date of Purchase',
        'po_entry_date':'Date of Entry',
        'po_quantity':'Quantity',
        'po_total_amount':'Total Amount'}
        widgets = {
            'po_item_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item Number'}),
            'po_product_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}),
            'po_unit_cost': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unit Cost'}),
            'po_purchase_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
            'po_entry_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
            'po_quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
            'po_total_amount': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Amount'})}

        def __str__(self):
            return self.po_item_number

class ProductsStockException(Exception):
    pass

class Sales_OrderForm(ModelForm):
    class Meta:
        model = Sales_Order
        fields = ('so_baby_id','so_date_created','so_item_number','so_unit_price','so_quantity','so_total_amount')
        labels = {
            'so_baby_id':'Baby ID Number',
            'so_date_created':'Date Created',
            'so_item_number':'Item Number',
            'so_unit_price':'Unit Price',
            'so_quantity':'Quantity',
            'so_total_amount':'Total Amount'}
        widgets = {
           'so_baby_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Baby ID Number'}),
           'so_date_created': forms.DateInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
           'so_item_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item Number'}),
           'so_unit_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unit Price'}),
           'so_quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
           'so_total_amount': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Amount'})}
   
    def save(self, commit=True):
        # This is checking to see if the product has enough items in the stock order
        order = super().save(commit=False)
        if order.so_item_number.po_quantity < order.so_quantity:
            raise ProductsStockException(f"Not enough products in inventory: {order.so_item_number}")
        if commit:
            order.save()
        return order
