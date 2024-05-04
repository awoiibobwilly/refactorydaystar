from django.db import models


# class Stay_Choice(models.Model):
#     stay = models.CharField(max_length=100,null=True, blank=True)
#     def __str__(self):
#         return self.saty


# class Baby_Registration(models.Model):
#     babyreg_baby_id = models.AutoField(primary_key=True)
#     babyreg_babys_sur_name = models.CharField(max_length=100)
#     babyreg_babys_other_names = models.CharField(max_length=200)
#     babyreg_babys_gender = models.models.CharField(max_length=200)
#     babyreg_babys_date_of_birth = models.DateField(auto_now_add=True)
#     babyreg_parents_sur_name = models.CharField(max_length=100)
#     babyreg_parentns_other_names = models.CharField(max_length=200)
#     babyreg_parents_gender = models.CharField(max_length=200)
#     babyreg_guardians_telephone = models.IntegerField(max_length=20)
#     babyreg_parents_date_of_birth = models.DateField(auto_now_add=True)
#     babyreg_babys_address = models.CharField(max_length=200)
#     babyreg_parents_sur_name = models.CharField(max_length=100)
#     babyreg_parentns_other_names = models.CharField(max_length=200)
#     babyreg_email = models.EmailField(max_length=254)

#     def __str__(self):
#         return self.babyreg_baby_id


# class Sitter_Registration(models.Model):
#     sitterreg_sitter_id = models.AutoField(primary_key=True)
#     sitterreg_sitter_sur_name = models.CharField(max_length=100)
#     sitterreg_sitter_other_names = models.CharField(max_length=200)
#     sitterreg_sitter_gender = models.models.CharField(max_length=200)
#     sitterreg_sitter_date_of_birth = models.DateField(auto_now_add=True)
#     sitterreg_sitter_nin_number = models.IntegerField(max_length=50)
#     sitterreg_sitter_educlevel = models.CharField(max_length=100)
#     sitterreg_sitter_religion = models.CharField(max_length=200)
#     sitterreg_nextofkin_address = models.CharField(max_length=200)
#     sitterreg_sitter_email = models.EmailField(max_length=254)
#     sitterreg_sitter_telephone = models.IntegerField(max_length=20)
#     sitterreg_nextofkin_sur_name = models.CharField(max_length=100)
#     sittereg_nextofkin_other_names = models.CharField(max_length=200)
#     sitterreg_nextofkin_gender = models.CharField(max_length=200)
#     sitterreg_nextofkin_date_of_birth = models.DateField(auto_now_add=True)
#     sitterreg_nextofkin_address = models.CharField(max_length=200)
#     sitterreg_nextofkin_email = models.EmailField(max_length=254)
#     sitterreg_nextofkin_telephone = models.IntegerField(max_length=20)

#     def __str__(self):
#         return self.sitterreg_sitter_id

# class Baby_Fee(models.Model):
#     baby_fee = models.ForeignKey(Baby_Registration,on_delete=models.CASCADE, null = True, blank = True)
#     bay_payment_category = models.ForeignKey(StayChoice,on_delete=models.CASCADE, null = True, blank = True)
#     baby_payamount = models.IntegerField(null=True, blank=True)
#     baby_paynum = models.IntegerField(null=True, blank=True)
#     baby_paycurrency = models.CharField(max_length= 10, default= 'UGX', null= True, blank=True)
    
#     def __int__(self):
#         return self.baby_paynum


# class Checkin(models.Model):
#     checkin_baby_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, null = True, blank = True)
#     checkin_time = models.TimeField(auto_now_add=True)
#     checkin_date = models.DateField(auto_now_add=True)
#     checkin_stay_duration = models.ForeignKey(StayChoice,on_delete=models.CASCADE, null = True, blank = True)
#     checkin_guardians_sur_name = models.CharField(max_length=100)
#     checkin_guardians_other_names = models.CharField(max_length=200)
#     checkin_guardians_telephone = models.IntegerField(max_length=20)
#     checkin_sitter_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, null = True, blank = True)
#     checkin_babay_fee = models.ForeignKey(Baby_Fee,on_delete=models.CASCADE, null = True, blank = True)
#     checkin_comment = models.CharField(max_length=200)


# class Sitter_Fee(models.Model):
#     sitter_fee = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, null = True, blank = True)
#     baby_payamount = models.IntegerField(null=True, blank=True)
#     baby_paynum = models.IntegerField(null=True, blank=True)
#     baby_paycurrency = models.CharField(max_length= 10, default= 'UGX', null= True, blank=True)
    
#     def __int__(self):
#         return self.baby_paynum


# class Checkout(models.Model):
#     checkin_baby_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, null = True, blank = True)
#     checkout_time = models.TimeField(auto_now_add=True)
#     checkout_date = models.DateField(auto_now_add=True)
#     checkout_stay_duration = models.ForeignKey(Stay_Choice,on_delete=models.CASCADE, null = True, blank = True)
#     checkout_guardians_sur_name = models.CharField(max_length=100)
#     checkout_guardians_other_names = models.CharField(max_length=200)
#     checkout_guardians_telephone = models.IntegerField()
#     checkout_sitter_id = models.ForeignKey(Sitter_Registration,on_delete=models.CASCADE, null = True, blank = True)
#     checkout_sitter_fee = models.ForeignKey(Sitter_Fee,on_delete=models.CASCADE, null = True, blank = True)
#     checkout_comment = models.CharField(max_length=200)



# class Purchase_Order(models.Model):
#     po_invoice_number = models.CharField(max_length=20)
#     po_item_number = models.CharField(max_length=20)
#     po_product_name = models.CharField(max_length=50)
#     po_unit_cost = models.IntegerField()
#     po_purchase_date = models.DateTimeField(auto_now_add=True)
#     po_entry_date = models.DateTimeField(auto_now_add=True)
#     po_quantity = models.IntegerField()
#     po_total = models.IntegerField()

# class Sales_Order(models.Model):
#     so_baby_id = models.models.IntegerField()
#     so_date_created = models.DateTimeField(auto_now_add=True)
#     so_product_name = models.CharField(max_length=20)
#     so_unit_price = models.IntegerField()
#     so_quantity = models.IntegerField()
#     so_total = models.IntegerField()





    
    
    
    
    
    
    
    
    
    


   

