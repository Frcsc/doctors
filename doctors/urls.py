from django.urls import path, include

from rest_framework import routers
from doctors import api

app_name = 'doctors'

router = routers.DefaultRouter() 
router.register(r'doctor', api.DoctorViewset, basename="doctors"),

urlpatterns = [
    path('', include(router.urls)),
]