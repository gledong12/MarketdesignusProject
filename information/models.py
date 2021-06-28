from django.db import models

class Moving_Company_Information(models.Model):
    name                       = models.CharField(max_length=50)
    master                     = models.CharField(max_length=20)
    phone_number               = models.CharField(max_length=20)
    address                    = models.CharField(max_length=100)
    business_number            = models.CharField(max_length=20)
    business_registration_date = models.DateField(auto_now_add=True)
    staff                      = models.IntegerField()
    matching                   = models.BooleanField(default=False)
    number_of_car              = models.ManyToManyField('Car', through='Company_Car', related_name='number_of_car')
    
    class Meta:
        db_table = 'company_information'
        
class Car(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'car'
        
class Company_Car(models.Model):
    company = models.ForeignKey('Moving_Company_Information', on_delete=models.CASCADE, related_name='company')
    car     = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='car')
    
    class Meta:
        db_table = 'company_car'
        
class CustomerInfomation(models.Model):
    name                       = models.CharField(max_length=45)
    phone_number               = models.CharField(max_length=50)
    terms_of_use               = models.BooleanField(default=False)
    personal_information       = models.BooleanField(default=False)
    marketing_information      = models.BooleanField(default=False)
    customer_registration_date = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'customer_information'

class Application_of_Moving(models.Model):
    departure_point       = models.CharField(max_length=100)
    departure_floor       = models.IntegerField()
    destination_point     = models.CharField(max_length=100)
    destination_floor     = models.IntegerField()
    moving_date           = models.DateField()
    storaging_moving      = models.BooleanField(default=False)
    customer_information  = models.ForeignKey('CustomerInfomation', on_delete=models.CASCADE)

    
    class Meta:
        db_table = 'application_of_moving'
        
class Moving_type(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'moving_type'
        
class Satisfaction(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'satisfaction'
        
class Customer_Feedback_History(models.Model):
    opening_information       = models.BooleanField(default=False)
    revisit                   = models.BooleanField(default=False)
    price                     = models.IntegerField()
    feeadback_date            = models.DateField(auto_now_add=True)
    feedback                  = models.TextField()
    information               = models.ForeignKey('Application_of_Moving', on_delete=models.CASCADE, related_name='information')
    company_information       = models.ForeignKey('Moving_Company_information', on_delete=models.CASCADE, related_name='company_information')
    moving_type               = models.ForeignKey('Moving_type', on_delete=models.CASCADE, related_name='moving_type')
    professional_satisfaction = models.ForeignKey('Satisfaction', on_delete=models.CASCADE, related_name='professional_satisfaction')
    price_satisfaction        = models.ForeignKey('Satisfaction', on_delete=models.CASCADE, related_name='price_satisfaction')
    kindness_satisfaction     = models.ForeignKey('Satisfaction', on_delete=models.CASCADE, related_name='Kindnedd_satisfaction')
    
    class Meta:
        db_table = 'feedback_history'
    
    