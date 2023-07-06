from django.urls import path
from myapp.views import api_endpoint
from myapp.views import api_endpoint1

urlpatterns = [
    path('api/endpoint', api_endpoint, name='api_endpoint'),
    path('api/endpoint1', api_endpoint1, name='api_endpoint1')
]