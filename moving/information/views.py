from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models  import (
                    CustomerInfomation,
                    Moving_Company_Information, 
                    Car, 
                    Company_Car, 
                    Application_of_Moving, 
                    Moving_type, Satisfaction, 
                    Customer_Feedback_History)

class MovingCompanyInformationView(View):
    def post(self, request):
        try:
            data              = request.POST
            name              = data['name']
            master            = data['master']
            phone_number      = data['number']
            address           = data['address']
            business_number   = data['business_number']
            staff             = data['staff']
            matching          = data.get('matching', False)
            cars              = data.getlist('car')
            
            company = Moving_Company_Information.objects.create(
                name                       = name,
                master                     = master,
                phone_number               = phone_number,
                address                    = address,
                business_number            = business_number,
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
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)
        
    def get(self,request):

        companys = Moving_Company_Information.objects.all()
        result =[{
            'name'     : company.name,
            'tel'      : company.phone_number[:-3] + company.phone_number[-3:-1].replace(company.phone_number[-3:-1],'**') + company.phone_number[-1],
            'address'  : company.address[:10],
            'matching' : company.matching
        } for company in companys]
        
        return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)

class CustomerInformationView(View):
    def post(self, request):
        try:
            data                  = request.POST
            name                  = data['name']
            phone_number          = data['number']
            terms_of_use          = data.get('use', False)
            personal_information  = data.get('personal', False)
            marketing_information = data.get('marketing', False)
            
            if CustomerInfomation.objects.filter(Q(name=name) & Q(phone_number=phone_number)).exists():
                return JsonResponse({'message' : 'INVALID_NAME'}, status=400)
            
            CustomerInfomation.objects.create(
                name                  = name,
                phone_number          = phone_number,
                terms_of_use          = terms_of_use,
                personal_information  = personal_information,
                marketing_information = marketing_information
            )
        
            return JsonResponse({'message' : 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)
        
    def get(self, request):
        customers = CustomerInfomation.objects.all()
        result = [{
            'name'   : customer.name,
            'number' : customer.phone_number[:-3] + customer.phone_number[-3:-1].replace(customer.phone_number[-3:-1],'**') + customer.phone_number[-1]
        }for customer in customers]
    
        return JsonResponse({'message' : 'SUCCESS', 'result': result}, status=200)
        
class ApplicationofMovingView(View):
    def post(self, request):
        try:
            data                  = request.POST
            name                  = data['name'] 
            departure_point       = data['departure_point']
            departure_floor       = data['departure_floor']
            destination_point     = data['destination_point']
            destination_floor     = data['destination_floor']
            moving_date           = data['moving_date']
            storaging_moving      = data.get('storaging_moving', False)

            if not CustomerInfomation.objects.filter(name=name).exists():
                return JsonResponse({'message' : 'DO_NOT_EXIST_NAME'}, status=400)
            name = CustomerInfomation.objects.get(name=name).id
            
            Application_of_Moving.objects.create(
                departure_point         = departure_point,
                departure_floor         = departure_floor,
                destination_floor       = destination_floor,
                destination_point       = destination_point,
                moving_date             = moving_date,
                storaging_moving        = storaging_moving,
                customer_information_id = name
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)
        
    def get(self, request):
        applications = Application_of_Moving.objects.all()
        total_data_count = len(applications)
        
        result = [{
            'name'          : application.customer_information.name,
            'tel'           : application.customer_information.phone_number[:-3] + application.customer_information.phone_number[-3:-1].replace(application.customer_information.phone_number[-3:-1],'**') + application.customer_information.phone_number[-1],
            'start_address' : application.departure_point[:11],
            'end_addresses' : application.destination_point[:11],
            'moving_date'   : application.moving_date,
            'is_storage'    : application.storaging_moving
        } for application in applications]

        return JsonResponse({'total_data_count' : total_data_count, 'result' : result},status=200)
    
class CustomerFeedbackHistoryView(View):
    def post(self, request):
        try:
            data = request.POST
            opening_information = data.get('opening', False)
            revisit             = data.get('revisit', False)
            price               = data['price']
            feedback            = data['feedback']
            customer            = data['customer']
            company             = data['company']
            moving_type         = data['moving_type']
            professional        = data['professional']
            price_satisfaction  = data['price_satisfaction']    
            kindness            = data['kindness']

            if not CustomerInfomation.objects.filter(name=customer).exists():
                return JsonResponse({'message' : 'INVALID_CUSTOMER'},status = 400)
            customer = CustomerInfomation.objects.get(name=customer).id
            
            if not Moving_Company_Information.objects.filter(name=company).exists():
                return JsonResponse({'message' : 'INVALID_COMPANY'},status = 400)
            company = Moving_Company_Information.objects.get(name=company).id
            
            if not Moving_type.objects.filter(name=moving_type).exists():
                return JsonResponse({'message' : 'INVALID_TYPE'}, status = 400)
            moving_type = Moving_type.objects.get(name=moving_type).id
            
            if not Satisfaction.objects.filter(Q(name=professional) & Q(name=price_satisfaction) & Q(name=kindness)).exists():
                return JsonResponse({'message' : 'INVALID_SATISFACTION'}, status = 400)
            
            professional       = Satisfaction.objects.get(name=professional).id
            price_satisfaction = Satisfaction.objects.get(name=price_satisfaction).id
            kindness           = Satisfaction.objects.get(name=kindness).id
           
            Customer_Feedback_History.objects.create(
                opening_information          = opening_information,
                revisit                      = revisit,
                price                        = price,
                feedback                     = feedback,
                information_id               = customer,
                company_information_id       = company,
                moving_type_id               = moving_type,
                professional_satisfaction_id = professional,
                price_satisfaction_id        = price_satisfaction,
                kindness_satisfaction_id     = kindness
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status=400)