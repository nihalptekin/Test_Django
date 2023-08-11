from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from .views import FlightView
from django.contrib.auth.models import AnonymousUser, User
# Create your tests here.
#class isminin sonu TestCase olmali
class FlightTestCase(APITestCase):
    def setUp(self):
        self.factory=APIRequestFactory()
        self.user=User.objects.create_user(
            username="fatih",
            email="f@gmail.com",
            password="secret11",
        )
    
    #fonksiyon yazarken "test" ile baslamali
    def test_flight_list(self):
        request=self.factory.get('/flights')
        response=FlightView.as_view({'get':'list'})(request)
        # request.user=AnonymousUser
        self.assertEqual(response.status_code, 200)

    def test_flight_list_as_login(self):
        request=self.factory.get('/flights')
        force_authenticate(request, user=self.user)
        self.user.is_staff=Trueself.user.
        response=FlightView.as_view({'post':'create'})(request)
        # request.user=AnonymousUser
        self.assertEqual(response.status_code, 200)

    