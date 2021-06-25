import json

from django.http import JsonResponse
from django.views import View

from .models  import (
                    Moving_Company_Information, 
                    Car, 
                    Company_Car, 
                    Application_of_Moving, 
                    Moving_type, Satisfaction, 
                    Customer_Feedback_History)

class Moving_Company_Information(View):
    def post(self, request):
        try:
            data              = request.post
            name              = data['name']
            master            = data['master']
            phone_number      = data['number']
            address           = data['address']
            business_number   = data['business_number']
            registration_date = data['registration_date']
            staff             = data['staff']
            matching          = data.get('matching', False)
            cars              = data.getlist('car')
            
            company = Moving_Company_Information.objects.create(
                name                       = name,
                master                     = master,
                phone_number               = phone_number,
                address                    = address,
                business_number            = business_number,
                business_registration_date = registration_date,
                staff                      = staff,
                matching                   = matching
            )
            
            company_id = company.id
            
            for car in cars:
                if not Car.objects.filter(name=car).exists():
                    car = Car.objects.get(name='etc')
                
                car = Car.objects.get(name=car)
                
                Company_Car.objects.create(
                    company_id = company_id,
                    car_id     = car.id
                )
                
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, statue=400)
        
class Application_of_Moving(View):
    def post(self, request):
        try:
            data                  = request.POST
            name                  = data['name']
            phone_number          = data['number']
            address               = data['address']
            departure_point       = data['departure_point']
            departure_floor       = data['deaparture_floor']
            destination_point     = data['destination_point']
            destination_floor     = data['destination_floor']
            moving_date           = data['moving_date']
            storaging_moving      = data.get('storaging_moving', False)
            terms_of_use          = data.get('terms', False)
            personal_information  = data.get('personal', False)
            marketing_information = data.get('marketing', False)
            
            Application_of_Moving.objects.create(
                name                  = name,
                phone_number          = phone_number,
                address               = address,
                departure_point       = departure_point,
                departure_floor       = departure_floor,
                destination_floor     = destination_floor,
                destination_point     = destination_point,
                moving_date           = moving_date,
                storaging_moving      = storaging_moving,
                terms_of_use          = terms_of_use,
                personal_information  = personal_information,
                marketing_information = marketing_information
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=200)
    

class Customer_Feedback_History(View):
    def post(self, request):
        try:
            data = request.POST
            opening_information = data.get('opeing', False)
            revisit             = data.get('revisit', False)
            price               = data['price']
            feedback            = data['feedback']
            customer            = data['customer']
            company             = data['company']
            moving_type         = data['moving_type']
            professional        = data['professional']
            price_satisfaction  = data['priec_satisfaction']
            kindness            = data['kindess']
            
            if not Application_of_Moving.objects.filter(name=customer).exists():
                return JsonResponse({'message' : 'INVALIED_CUSTOMER'},status = 400)
            customer = Application_of_Moving.objects.get(name=customer).id
            
            if not Moving_Company_Information.objects.filter(name=company).exists():
                return JsonResponse({'message' : 'INVALIED_COMPANY'},status = 400)
            company = Moving_Company_Information.objects.get(name=company).id
            
            if not Moving_type.objects.filter(name=moving_type).exists():
                return JsonResponse({'message' : 'INVALIED_TYPE'}, status = 400)
            moving_type = Moving_type.objects.get(name=moving_type).id
            
            if not Satisfaction.objects.filter(name=professional, name=price_satisfaction, name=kindness).exists():
                return JsonResponse({'message' : 'INVALIED_SATISFACTION'}, status = 400)
            
            professional       = Satisfaction.objects.get(name=professional).id
            price_satisfaction = Satisfaction.objects.get(name=price_satisfaction).id
            kindness           = Satisfaction.objects.get(name=kindness).id
            
            Customer_Feedback_History.objects.create(
                opening_information=opening_information,
                revisit                   = revisit,
                price                     = price,
                feedback                  = feedback,
                customer_information      = customer,
                company_information       = company,
                moving_type               = moving_type,
                professional_satisfaction = professional,
                price_satisfaction        = price_satisfaction,
                kindness_satisfaction     = kindness
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)