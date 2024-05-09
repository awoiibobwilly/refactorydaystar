# from django.db import models


# class Baby_Registration(models.Model):
#     baby_gender = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ]
#     parent_gender = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ]
#     babyreg_baby_id = models.AutoField(primary_key=True)
#     babyreg_babys_sur_name = models.CharField(max_length=100)
#     babyreg_babys_other_names = models.CharField(max_length=200)
#     babyreg_babys_gender = models.ChoiceField(choices=baby_gender)
#     babyreg_babys_date_of_birth = models.DateField(auto_now_add=True)
#     babyreg_parents_sur_name = models.CharField(max_length=100)
#     babyreg_parentns_other_names = models.CharField(max_length=200)
#     babyreg_parents_gender = models.ChoiceField(choices=parent_gender)
#     babyreg_parents_date_of_birth = models.DateField(auto_now_add=True)
#     babyreg_parents_telephone = models.IntegerField(max_length=20)
#     babyreg_parents_address = models.CharField(max_length=200)
#     babyreg_parents_email = models.EmailField(max_length=254)

#     def __str__(self):
#         return self.babyreg_baby_id


# class Sitter_Registration(models.Model):
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
#     sitterreg_sitter_id = models.AutoField(primary_key=True)
#     sitterreg_sitter_sur_name = models.CharField(max_length=100)
#     sitterreg_sitter_other_names = models.CharField(max_length=200)
#     sitterreg_sitter_gender = models.ChoiceField(choices=sitter_gender)
#     sitterreg_sitter_date_of_birth = models.DateField(auto_now_add=True)
#     sitterreg_sitter_nin_number = models.IntegerField(max_length=50)
#     sitterreg_sitter_educlevel = models.ChoiceField(choices=sitter_edulevel)
#     sitterreg_sitter_religion = models.ChoiceField(choices=sitter_religion)
#     sitterreg_sitter_address = models.CharField(choices=sitter_location)
#     sitterreg_sitter_email = models.EmailField(max_length=254)
#     sitterreg_sitter_telephone = models.IntegerField(max_length=20)
#     sitterreg_nextofkin_sur_name = models.CharField(max_length=100)
#     sittereg_nextofkin_other_names = models.CharField(max_length=200)
#     sitterreg_nextofkin_gender = models.ChoiceField(choices=nok_gender)
#     sitterreg_nextofkin_date_of_birth = models.DateField(auto_now_add=True)
#     sitterreg_nextofkin_address = models.CharField(max_length=200)
#     sitterreg_nextofkin_email = models.EmailField(max_length=254)
#     sitterreg_nextofkin_telephone = models.IntegerField(max_length=20)

#     def __str__(self):
#         return self.sitterreg_sitter_id


# class Checkin(models.Model):
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
#     checkin_baby_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE)
#     checkin_sitter_availability = models.ChoiceField(choices=checkin_sitter_status)
#     checkin_time = models.TimeField(auto_now_add=True)
#     checkin_date = models.DateField(auto_now_add=True)
#     checkin_care_time = models.ChoiceField(choices=care_timein)
#     checkin_guardians_sur_name = models.CharField(max_length=100)
#     checkin_guardians_other_names = models.CharField(max_length=200)
#     checkin_guardians_telephone = models.IntegerField(max_length=20)
#     checkin_sitter_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE)
#     checkin_payment_choice = models.ChoiceField(choices=checkin_payment_option)
#     daystar_checkin_fee = models.IntegerField(max_length=50)
#     daystar_checkin_fee_currency = models.CharField(max_length= 10, default= 'UGX')
#     checkin_comment = models.CharField(max_length=1000)
    


# class Checkout(models.Model):
#     care_timeout = [
#         ('Morning', 'Morning'),
#         ('Afternoon', 'Afternoon'),
#         ('Evening', 'Evening'),
#         ('Night', 'Night'),]
#     checkout_payment_option = [
#         ('Daily', 'Daily'),
#         ('Weekly', 'Weekly'),
#         ('Monthly', 'Monthly'),]
#     checkin_baby_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE)
#     checkout_time = models.TimeField(auto_now_add=True)
#     checkout_date = models.DateField(auto_now_add=True)
#     checkout_care_time = models.ChoiceField(choices=care_timein)
#     checkout_guardians_sur_name = models.CharField(max_length=100)
#     checkout_guardians_other_names = models.CharField(max_length=200)
#     checkout_guardians_telephone = models.IntegerField()
#     checkout_sitter_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE)
#     checkout_payment_choice = models.ChoiceField(choices=checkout_payment_option)
#     daystar_care_time_fee = models.IntegerField(max_length=50)
#     daystar_care_time_fee_currency = models.CharField(max_length= 10, default= 'UGX')
#     checkout_sitter_fee = models.IntegerField(max_length=50)
#     checkout_sitter_fee_currency = models.CharField(max_length= 10, default= 'UGX')
#     checkout_comment = models.CharField(max_length=1000)

#     def __int__(self):
#         return self.checkin_baby_id


# class Purchase_Order(models.Model):
#     po_invoice_number = models.CharField(max_length=20)
#     po_item_number = models.CharField(max_length=20)
#     po_product_name = models.CharField(max_length=50)
#     po_unit_cost = models.IntegerField()
#     po_purchase_date = models.DateTimeField(auto_now_add=True)
#     po_entry_date = models.DateTimeField(auto_now_add=True)
#     po_quantity = models.IntegerField()
#     po_total = models.IntegerField()

#     def __int__(self):
#         return self.po_invoice_number

# class Sales_Order(models.Model):
#     so_baby_id = models.models.IntegerField()
#     so_date_created = models.DateTimeField(auto_now_add=True)
#     so_product_name = models.CharField(max_length=20)
#     so_unit_price = models.IntegerField()
#     so_quantity = models.IntegerField()
#     so_total = models.IntegerField()

#     def __int__(self):
#         return self.so_baby_id





    
    
    
    
    
    
    
    
    
    


   

