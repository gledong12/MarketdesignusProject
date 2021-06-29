import json

from django.http import response
from django.test import TestCase, Client, client

from urllib.parse  import urlencode
from .models import (
    Moving_Company_Information,
    Car,
    Company_Car,
    CustomerInfomation,
    Application_of_Moving,
    Moving_type,
    Satisfaction,
    Customer_Feedback_History)

class MovingCompanyInformationTest(TestCase):
    def setup(self):
        Car.objects.create(id =1, name='1t')
        Car.objects.create(id =2, name='2.5t')
        Car.objects.create(id=3, name='5t')
        Car.objects.create(id=4, name='etc')
        Company_Car.objects.create(
            id         = 1,
            car_id     = 1,
            company_id = 1
        )
        Company_Car.objects.create(
            id         = 2,
            car_id     = 2,
            company_id = 1
        )
        Company_Car.objects.create(
            id         = 3,
            car_id     = 3,
            company_id = 1
        )
        Moving_Company_Information.objects.create(
            id              = 1,
            name            = '삼성',
            master          = 'EFGGG',
            phone_number    = '010-1111-2222',
            address         = '서울 관악구 봉천동 서울대학교',
            business_number = '123-111-1111',
            staff           = 8,
            matching        = True 
        )
        
    def tearDown(self):
        Car.objects.all().delete()
        Company_Car.objects.all().delete()
        Moving_Company_Information.objects.all().delete()
        
    def test_movingcompanyinformationview_post_success(self):
        client = Client()
        
        company_information = urlencode({
            'name'           : '삼성',
            'master'         : 'EFGGG',
            'number'         : '010-1111-2222',
            'address'        : '서울 관악구 봉천동 서울대학교',
            'business_number': '123-111-1111',
            'staff'          : 8,
            'matching'       : True
        })
        
        response = client.post('/moving/company', company_information, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            'message' : 'SUCCESS'
        })
        
    def test_movingcompanyinformationview_post_invalid_key(self):
        client = Client()
        company_information = urlencode({
            'name11'         : 'ABCD',
            'master'         : 'EFGGG',
            'phone_number'   : '010-1111-2222',
            'address'        : '서울 관악구 봉천동 서울대학교',
            'business_number': '123-111-1111',
            'staff'          : 8,
            'matching'       : True 
        })
        response = client.post('/moving/company', company_information, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{
            'message' : 'INVALID_KEYS'
        })

class CustomerInformationTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        CustomerInfomation.objects.all().delete()
        
    def test_customerinformationview_post_success(self):
        client = Client()
        customer_information = urlencode({
            'name'                  : '이동근',
            'number'                : '111-1111-1111',
            'terms_of_use'          : True,
            'personal_information'  : True,
            'marketing_information' : True
        })
        
        response = client.post('/moving/customer', customer_information, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'message' : 'SUCCESS'
        })
        
    def test_customerinformationview_post_invalid_keys(self):
        client = Client()
        customer_information = urlencode({
            'namee'                 : '이동근',
            'number'                : '111-1111-1111',
            'terms_of_use'          : True,
            'personal_information'  : True,
            'marketing_information' : True
        })
        
        response = client.post('/moving/customer', customer_information, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_KEYS'
        })
    
class ApplicationofMovingTest(TestCase):
    def setUp(self):
       CustomerInfomation.objects.create(
           id                         = 1,
           name                       = '이동근',
           phone_number               = '010-1111-4111',
           terms_of_use               = True,
           personal_information       = True,
           marketing_information      = True,
           customer_registration_date = '2021-06-25'   
       )
       
    def tearDown(self):
        CustomerInfomation.objects.all().delete()
        Application_of_Moving.objects.all().delete()
   
    def test_applicationofmovingview_post_success(self):
        client = Client()
        application = urlencode({
            'departure_point'         : '서울 관악구 봉천동',
            'departure_floor'         : 3,
            'destination_point'       : '울산 울주군 굴화면',
            'destination_floor'       : 6,
            'moving_date'             : '2021-06-25',
            'storaging_moving'        : True,
            'name'                    : '이동근',
        })
        
        response =client.post('/moving/application', application, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'message' : 'SUCCESS'
        })
        
    def test_applicationofMoving_post_invalid_name(self):
        client = Client()
        application = urlencode({
            'departure_point'     : '서울 관악구 봉천동',
            'departure_floor'      : 3,
            'destination_point'    : '울산 울주군 굴화면',
            'destination_floor'    : 6,
            'moving_date'          : '2021-06-25',
            'storaging_moving'     : True,
            'name'                 : 'ffffff'
        })
        
        response = client.post('/moving/application', application, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'DO_NOT_EXIST_NAME'
        })
        
    def test_applicationofMoving_post_invalid_key(self):
        client = Client()
        application = urlencode({
            'deprture_point'         : '서울 관악구 봉천동',
            'departure_floor'         : 3,
            'destination_point'       : '울산 울주군 굴화면',
            'destination_floor'       : 6,
            'moving_date'             : '2021-06-25',
            'storaging_moving'        : True,
            'customer_information_id' : 1
        })
        
        response =client.post('/moving/application', application, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_KEYS'
        })
        
class CustomerFeedbackHistoryTest(TestCase):
    def setUp(test):
        Moving_type.objects.create(id=1, name='원룸이사')
        Moving_type.objects.create(id=2, name='가정이사')
        Satisfaction.objects.create(id=1, name='매우만족')
        Satisfaction.objects.create(id=2, name='만족')
        Satisfaction.objects.create(id=3, name='보통')
        Satisfaction.objects.create(id=4, name='불만족')
        Satisfaction.objects.create(id=5, name='매우불만족')
        CustomerInfomation.objects.create(
            id                         = 1,
            name                       = '이동근',
            phone_number               = '010-1111-1111',
            terms_of_use               = True,
            personal_information       = True,
            marketing_information      = True,
            customer_registration_date = '2021-06-01' 
        )
        Application_of_Moving.objects.create(
            id                   = 1,
            departure_point      = '서울 관악구 봉천동 서울대학교',
            departure_floor      = 5,
            destination_point    = '울산 울주군 남천동',
            destination_floor    = 6,
            moving_date           = '2021-06-25',
            storaging_moving      = True,
            customer_information_id = 1
        )
        Moving_Company_Information.objects.create(
            name = '삼성',
            master = 'AAAA',
            phone_number = '010-2222-2222',
            address = '가평 을왕리 평창동',
            business_number = '12-222-223564',
            business_registration_date = '2021-05-21',
            staff = 6,
            matching = True
        )
        
    def tearDown(self):
        Moving_type.objects.all().delete()
        Satisfaction.objects.all().delete()
        CustomerInfomation.objects.all().delete()
        Application_of_Moving.objects.all().delete()
        Moving_Company_Information.objects.all().delete()
        
    def test_customerfeedbackhistoryview_post_success(self):
        client = Client()
        feedback = urlencode({
            'opening_information' : True,
            'revisit'             : True,
            'price'               : 100000,
            'feedback'            : '너무 좋았습니다.',
            'customer'            : '이동근',
            'company'             : '삼성',
            'moving_type'         : '가정이사',
            'professional'        : '매우만족',
            'price_satisfaction'  : '매우만족',
            'kindness'            : '매우만족'
            })
        response = client.post('/moving/feedback', feedback, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'message' : 'SUCCESS'
        })
    
    def test_customerfeedbackhistoryview_post_invalid_keys(self):
        client = Client()
        feedback = urlencode({
            'opening_information' : True,
            'revisit'             : True,
            'price'               : 100000,
            'feedback'            : '너무 좋았습니다.',
            'customer'            : '이동근',
            'compeeany'           : '삼성',
            'moving_type'         : '가정이사',
            'professional'        : '매우만족',
            'price_satisfaction'  : '매우만족',
            'kindness'            : '매우만족'
            })
        
        response = client.post('/moving/feedback', feedback, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_KEYS'
        })
    
    def test_customerfeedbackhistoryview_post_invalid_customer(self):
        client = Client()
        feedback = urlencode({
            'opening_information' : True,
            'revisit'             : True,
            'price'               : 100000,
            'feedback'            : '너무 좋았습니다.',
            'customer'            : 'fffff',
            'company'             : '삼성',
            'moving_type'         : '가정이사',
            'professional'        : '매우만족',
            'price_satisfaction'  : '매우만족',
            'kindness'            : '매우만족'
            })
        response = client.post('/moving/feedback', feedback, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_CUSTOMER'
        })
    
    def test_customerfeedbackhistoryview_post_invalid_type(self):
        client = Client()
        feedback = urlencode({
            'opening_information' : True,
            'revisit'             : True,
            'price'               : 100000,
            'feedback'            : '너무 좋았습니다.',
            'customer'            : '이동근',
            'company'             : '삼성',
            'moving_type'         : 'fggg이사',
            'professional'        : '매우만족',
            'price_satisfaction'  : '매우만족',
            'kindness'            : '매우만족'
            })
        response = client.post('/moving/feedback', feedback, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_TYPE'
        })
    
    def test_customerfeedbackhistoryview_post_invalid_satisfaction(self):
        client = Client()
        feedback = urlencode({
            'opening_information' : True,
            'revisit'             : True,
            'price'               : 100000,
            'feedback'            : '너무 좋았습니다.',
            'customer'            : '이동근',
            'company'             : '삼성',
            'moving_type'         : '가정이사',
            'professional'        : '매우족',
            'price_satisfaction'  : '매우만족',
            'kindness'            : '매우만족'
            })
        response = client.post('/moving/feedback', feedback, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_SATISFACTION'
        })
