from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, ALX!"})

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Listings!")
