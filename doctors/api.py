from rest_framework import  status, viewsets
from rest_framework.response import Response
from doctors.filters import DoctorFilter
from django.shortcuts import get_object_or_404

from doctors.models import DoctorProfile
from doctors.serializers import DoctorProfileDetailSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileDetailSerializer
    filterset_class = DoctorFilter

    def retrieve(self, request, *args, **kwargs):
        doctor = get_object_or_404(DoctorProfile, id=self.kwargs['pk'])
        serializer = DoctorProfileDetailSerializer(doctor)
        return Response(serializer.data)

    def create(self, request):
        serializer = DoctorProfileDetailSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.data, status=status.HTTP_201_CREATED)