# from django import forms

# class Baby_RegistrationForm(forms.Form):
#     baby_gender = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ]
#     parent_gender = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ]
#     babyreg_baby_id = forms.AutoField(primary_key=True, label='Baby ID', required=True)
#     babyreg_babys_sur_name = forms.CharField(max_length=100, label='Baby Surname', required=True)
#     babyreg_babys_other_names = forms.CharField(max_length=200, label='Baby Other Names', required=True)
#     babyreg_babys_gender = forms.ChoiceField(choices=baby_gender, label='Baby Gender', required=True)
#     babyreg_babys_date_of_birth = forms.DateField(auto_now_add=True, label='Baby Birth of Date', required=True)
#     babyreg_parents_sur_name = forms.CharField(max_length=100, label='Parent Surname')
#     babyreg_parentns_other_names = forms.CharField(max_length=200, label='Parent Other Names')
#     babyreg_parents_gender = forms.ChoiceField(choices=parent_gender, label='Parent Gender')
#     babyreg_parents_date_of_birth = forms.DateField(auto_now_add=True, label='Parent Birth of Date', required=True)
#     babyreg_parents_telephone = forms.IntegerField(max_length=20, label='Parent Telephone', required=True)
#     babyreg_parents_address = forms.CharField(max_length=200, label='Parent Address', required=True)
#     babyreg_parents_email = forms.EmailField(max_length=254, label='Parent email', required=True)

#     def __str__(self):
#         return self.babyreg_baby_id


# class Sitter_RegistrationForm(forms.Form):
#     sitter_gender = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ]
#     nok_gender = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ]
#     sitter_edulevel = [
#         ('Primary', 'Primary'),
#         ('O-Level', 'O-Level'),
#         ('A-Level', 'A-Level'),
#         ('Certificate', 'Certificate'),
#         ('Diploma', 'Diploma'),
#         ('Degree', 'Degree'),
#         ('Others', 'Others'),
#         ]
#     sitter_religion = [
#         ('Born Aagain', 'Born Aagain'),
#         ('Anglican', 'Anglican'),
#         ('Catholic', 'Catholic'),
#         ('Islam', 'Islam'),
#         ('Others', 'Others'),
#         ]
#     sitter_location = [
#         ('Kabalagala', 'Kabalagala'),
#         ('Other', 'Other'),
#         ]
#     sitterreg_sitter_id = forms.AutoField(primary_key=True, label='Sitter ID', required=True)
#     sitterreg_sitter_sur_name = forms.CharField(max_length=100, label='Sitter Surname', required=True)
#     sitterreg_sitter_other_names = forms.CharField(max_length=200, label='Sitter Other Names', required=True)
#     sitterreg_sitter_gender = forms.ChoiceField(choices=sitter_gender, label='Sitter Gender', required=True)
#     sitterreg_sitter_date_of_birth = forms.DateField(auto_now_add=, label='Sitter Date of Birth', required=True)
#     sitterreg_sitter_nin_number = forms.IntegerField(max_length=50, label='NIN Number', required=True)
#     sitterreg_sitter_educlevel = forms.ChoiceField(choices=sitter_edulevel, label='Education Level')
#     sitterreg_sitter_religion = forms.ChoiceField(choices=sitter_religion, label='Religion (Optional)')
#     sitterreg_sitter_address = forms.CharField(max_length=200, default= 'Kabalagala', label='Next Ofkin Address', required=True)
#     sitterreg_sitter_email = forms.EmailField(max_length=254, label='Email Address(Optional)')
#     sitterreg_sitter_telephone = forms.IntegerField(max_length=20, label='Sitter Telephone', required=True)
#     sitterreg_nextofkin_sur_name = forms.CharField(max_length=100, label='Next Of Kin Surname', required=True)
#     sittereg_nextofkin_other_names = forms.CharField(max_length=200, label='Next Of Kin Other Names', required=True)
#     sitterreg_nextofkin_gender = forms.ChoiceField(choices=nok_gender, label='Next Of Kin Gender', required=True)
#     sitterreg_nextofkin_date_of_birth = forms.DateField(auto_now_add=, label='Next Of Kin Date of Birth', required=True)
#     sitterreg_nextofkin_address = forms.CharField(max_length=200, label='Next Of Kin Address', required=True)
#     sitterreg_nextofkin_email = forms.EmailField(max_length=254, label='Next Of Kin email(Optional)', required=True)
#     sitterreg_nextofkin_telephone = forms.IntegerField(max_length=20, label='Next Of Kin Telephone', required=True)

#     def __str__(self):
#         return self.sitterreg_sitter_id


# class CheckinForm(forms.Form):
#     care_timein = [
#         ('Morning', 'Morning'),
#         ('Afternoon', 'Afternoon'),
#         ('Evening', 'Evening'),
#         ('Night', 'Night'),]
#     checkin_payment_option = [
#         ('Daily', 'Daily'),
#         ('Weekly', 'Weekly'),
#         ('Monthly', 'Monthly'),]
#     checkin_sitter_status = [
#         ('On Duty', 'On Duty'),
#         ('Off Duty', 'Off Duty'),]
#     checkin_baby_id = forms.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, label= 'Baby ID', required=True)
#     checkin_sitter_availability = forms.ChoiceField(choices=checkin_sitter_status, label= 'Sitter Availability', required=True)
#     checkin_time = forms.TimeField(auto_now_add=True, label= 'Checkin Time', required=True)
#     checkin_date = forms.DateField(auto_now_add=True, label= 'Checkin Date', required=True)
#     checkin_care_time = forms.ChoiceField(choices=care_timein, label= 'Care Time', required=True)
#     checkin_guardians_sur_name = forms.CharField(max_length=100, label='Guardian Surname', required=True)
#     checkin_guardians_other_names = forms.CharField(max_length=200, label='Guardian Other Names', required=True)
#     checkin_guardians_telephone = forms.IntegerField(max_length=20, label='Guardian Telephone', required=True)
#     checkin_sitter_id = forms.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, label='Sitter ID', required=True)
#     checkin_payment_choice = models.ChoiceField(choices=checkin_payment_option, label='Mode of Payment', required=True)
#     daystar_checkin_fee = forms.IntegerField(max_length=50, label='Daystar Fee', required=True)
#     daystar_checkin_fee_currency = forms.CharField(max_length= 10, default= 'UGX', label='Currency', required=True)
#     checkin_comment = forms.CharField(max_length=1000, label='Comment (Optional)')
    


# class CheckoutForm(forms.Form):
#     care_timeout = [
#         ('Morning', 'Morning'),
#         ('Afternoon', 'Afternoon'),
#         ('Evening', 'Evening'),
#         ('Night', 'Night'),]
#     checkout_payment_option = [
#         ('Daily', 'Daily'),
#         ('Weekly', 'Weekly'),
#         ('Monthly', 'Monthly'),]
#     checkin_baby_id = forms.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, label='Baby ID', required = True)
#     checkout_time = forms.TimeField(auto_now_add=True, label='Checkout Time', required = True)
#     checkout_date = forms.DateField(auto_now_add=True, label='Checkout Date', required = True)
#     checkout_care_time = forms.ChoiceField(choices=care_timein, label='Care Time', required = True)
#     checkout_guardians_sur_name = forms.CharField(max_length=100, label='Guardian Surname', required = True)
#     checkout_guardians_other_names = forms.CharField(max_length=200, label='Guardian Other Names', required = True)
#     checkout_guardians_telephone = forms.IntegerField(label='Guardian Telephone', required = True)
#     checkout_sitter_id = forms.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, label='Sitter ID', required = True)
#     checkout_payment_choice = forms.ChoiceField(choices=checkout_payment_option, label='Mode of Payment', required = True)
#     daystar_care_time_fee = forms.IntegerField(label='Daystar Fee', required = True)
#     daystar_care_time_fee_currency = forms.CharField(max_length= 10, default= 'UGX', label='Daystar Fee Currency', required = True)
#     checkout_sitter_fee = forms.IntegerField(label='Sitter Fee', required = True)
#     checkout_sitter_fee_currency = forms.CharField(max_length= 10, default= 'UGX', label='Sitter Fee Currency', required = True)
#     checkout_comment = forms.CharField(max_length=1000, label='Comment(Optional)', required = True)

#     def __int__(self):
#         return self.checkin_baby_id


# class Purchase_OrderForm(forms.Form):
#     po_invoice_number = forms.CharField(max_length=20, label='Invoice Number', required = True)
#     po_item_number = forms.CharField(max_length=20, label='Item Number', required = True)
#     po_product_name = forms.CharField(max_length=50, label=' Product Name', required =True)
#     po_unit_cost = forms.IntegerField(label='Unit Cost', required = True)
#     po_purchase_date = forms.DateTimeField(auto_now_add=True, label='Purchase Date', required = True)
#     po_entry_date = forms.DateTimeField(auto_now_add=True, label='Item Entry Date', required = True)
#     po_quantity = forms.IntegerField(label='Quantity', required = True)
#     po_total = forms.IntegerField(label='Total Amount', required = True)
#     po_currency = forms.CharField(max_length= 10, default= 'UGX', label='Currency', required=True)
    

#     def __int__(self):
#         return self.po_invoice_number

# class Sales_OrderForm(forms.Form):
#     so_baby_id = forms.forms.IntegerField(label='Baby ID', required = True)
#     so_date_created = forms.DateTimeField(auto_now_add=True, label='Sales Order Date', required = True)
#     so_product_name = forms.CharField(max_length=20, label='Product Name', required = True)
#     so_unit_price = forms.IntegerField(label='Unit Cost', required = True)
#     so_quantity = forms.IntegerField(label='Quantity', required = True)
#     so_total = forms.IntegerField(label='Total Amount', required = True)
#     so_currency = forms.CharField(max_length= 10, default= 'UGX', label='Currency', required=True)

#     def __int__(self):
#         return self.so_baby_id