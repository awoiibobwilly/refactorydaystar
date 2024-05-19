from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Baby_Register(models.Model):
    babiz_sur_name = models.CharField(max_length=20)
    babiz_other_names = models.CharField(max_length=20)
    babiz_gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female')])
    babiz_date_of_birth = models.DateField()
    parentz_sur_name = models.CharField(max_length=20)
    parentz_other_names = models.CharField(max_length=20)
    parentz_gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female')])
    parentz_date_of_birth = models.DateField()
    parentz_telephone = models.IntegerField()
    parentz_address = models.CharField(max_length=50)
    parentz_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.babiz_sur_name


class Sitter_Register(models.Model): 
    sit_sur_name = models.CharField(max_length=20)
    sit_other_names = models.CharField(max_length=20)
    sit_gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female')])
    sit_date_of_birth = models.DateField()
    sit_nin_number = models.CharField(max_length=20)
    sit_educlevel = models.CharField(max_length=20, choices=[('Primary', 'Primary'), ('O-Level', 'O-Level'), ('A-Level', 'A-Level'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Degree', 'Degree'), ('Others', 'Others')])
    sit_religion = models.CharField(max_length=20, choices=[('Born Aagain', 'Born Aagain'), ('Anglican', 'Anglican'), ('Catholic', 'Catholic'), ('Islam', 'Islam'), ('Others', 'Others')])
    sit_address = models.CharField(max_length=20, choices=[('Kabalagala', 'Kabalagala'), ('Other', 'Other')])
    sit_email = models.EmailField(max_length=50)
    sit_telephone = models.IntegerField()
    snok_sur_name = models.CharField(max_length=20)
    snok_other_names = models.CharField(max_length=10)
    snok_gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female')])
    snok_date_of_birth = models.DateField()
    snok_address = models.CharField(max_length=50)
    snok_email = models.EmailField(max_length=50)
    snok_telephone = models.IntegerField()

    def __str__(self):
        return self.sit_sur_name
 


class Sitter_Status(models.Model):
    sitter_id = models.ForeignKey(Sitter_Register, on_delete=models.CASCADE)
    sitter_availability = models.CharField(max_length=10, choices=[('On Duty', 'On Duty'), ('Off Duty', 'Off Duty')])
    sitter_time = models.TimeField()
    sitter_date = models.DateField()
    def __int__(self):
        return self.sitter_id

class Checkin(models.Model): 
    baby_id = models.ForeignKey(Baby_Register, on_delete=models.CASCADE)
    checkin_sitter_availability = models.ForeignKey(Sitter_Status, on_delete=models.CASCADE, max_length=10, default='On Duty')
    checkin_time = models.TimeField()
    checkin_date = models.DateField()
    checkin_care_time = models.CharField(max_length=10, choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Night', 'Night')])
    checkin_guardians_sur_name = models.CharField(max_length=100)
    checkin_guardians_other_names = models.CharField(max_length=200)
    checkin_guardians_telephone = models.IntegerField()
    sitter_id = models.ForeignKey(Sitter_Register, on_delete=models.CASCADE)
    checkin_payment_choice = models.CharField(max_length=10, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])
    daystar_checkin_fee = models.IntegerField()
    daystar_checkin_fee_currency = models.CharField(max_length= 10, choices=[('UGX', 'UGX'), ('USD', 'USD')], default= 'UGX')
    checkin_comment = models.CharField(max_length=1000)

    def __int__(self):
        return self.baby_id
    

class Checkout(models.Model): 
    baby_id = models.ForeignKey(Baby_Register, on_delete=models.CASCADE)
    checkout_time = models.TimeField()
    checkout_date = models.DateField()
    checkout_care_time = models.CharField(max_length=10, choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Night', 'Night'),])
    checkout_guardians_sur_name = models.CharField(max_length=100)
    checkout_guardians_other_names = models.CharField(max_length=200)
    checkout_guardians_telephone = models.IntegerField()
    sitter_id = models.ForeignKey(Sitter_Register, on_delete=models.CASCADE)
    checkout_payment_choice = models.CharField(max_length=10, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'),])
    daystar_care_time_fee = models.IntegerField()
    daystar_care_time_fee_currency = models.CharField(max_length= 10, choices=[('UGX', 'UGX'), ('USD', 'USD')], default= 'UGX')
    checkout_sitter_fee = models.IntegerField()
    checkout_sitter_fee_currency = models.CharField(max_length= 10, default= 'UGX')
    checkout_comment = models.CharField(max_length=1000)

    def __int__(self):
        return self.baby_id 

# class Procurement(models.Model):
#     po_item_number = models.CharField(max_length=20)
#     po_product_name = models.CharField(max_length=50)
#     po_unit_cost = models.IntegerField()
#     po_purchase_date = models.DateTimeField()
#     po_entry_date = models.DateTimeField()
#     po_quantity = models.PositiveSmallIntegerField()
#     po_total_amount = models.IntegerField()

#     def __int__(self):
#         return self.po_item_number 


# class Sales_Order(models.Model):
#     so_baby_id = models.ForeignKey(Baby_Register, on_delete=models.CASCADE)
#     so_date_created = models.DateTimeField()
#     so_item_number = models.ForeignKey(Procurement, on_delete=models.CASCADE)
#     so_unit_price = models.IntegerField()
#     so_quantity = models.PositiveSmallIntegerField()
#     so_total_amount = models.IntegerField()

#     def __str__(self):
#         return f'{self.so_quantity} x {self.so_item_number.po_item_number}'


class Purchase(models.Model):
    po_item_number = models.CharField(max_length=20)
    po_product_name = models.CharField(max_length=50)
    po_unit_cost = models.IntegerField()
    po_purchase_date = models.DateTimeField()
    po_entry_date = models.DateTimeField()
    po_quantity = models.PositiveSmallIntegerField()
    @property
    def total(self):
        return self.po_unit_cost*self.po_quantity

    def __str__(self):
        return self.po_item_number

class Sales(models.Model):
    so_baby_id = models.ForeignKey(Baby_Register, on_delete=models.CASCADE)
    so_date_created = models.DateTimeField()
    so_item_number = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    so_unit_price = models.IntegerField()
    so_quantity = models.PositiveSmallIntegerField()
    @property
    def total(self):
        return self.so_unit_price*self.so_quantity

    def __str__(self):
        return f'{self.so_quantity} x {self.so_item_number.po_item_number}'


    
    
    
    
    
    
    
    
    
    


   

