from django.db.models import Q
from doctors.test_data import (
    test_data_one_doctors,
    test_data_two_doctors,
    test_data_four_doctors
)
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from doctors.models import DoctorProfile


class DoctorListTest(APITestCase):
    def setUp(self):
        url = reverse('all:doctors-list')
        self.data = test_data_four_doctors
        self.doctors = self.client.post(url, self.data, format="json")

    def test_get_list_of_doctors(self):
        response = self.client.get(reverse('all:doctors-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DoctorProfile.objects.count(), 4)
        last_doctor = DoctorProfile.objects.all()[3]
        self.assertEqual(DoctorProfile.objects.filter(id=last_doctor.id).count(), 1)

class DoctorTests(APITestCase):

    url = reverse('all:doctors-list')

    def test_creating_a_single_doctor(self):
        data = test_data_one_doctors
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DoctorProfile.objects.count(), 1)
        self.assertEqual(DoctorProfile.objects.get().name, 'Abu Mohamed')

    def test_creating_multiple_doctors(self):
        data = test_data_four_doctors
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DoctorProfile.objects.count(), 4)

    def test_filter_by_district(self):
        data = test_data_four_doctors
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DoctorProfile.objects.filter(district_name__name='Brikama').count(), 2)

    def test_filter_by_category(self):
        data = test_data_four_doctors
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DoctorProfile.objects.filter(category__name='Dentist').count(), 1)

    def test_filter_by_language(self):
        data = test_data_four_doctors
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DoctorProfile.objects.filter(language__name='Arabic').count(), 3)
        self.assertEqual(DoctorProfile.objects.filter(language__name='Malay').count(), 1)

    def test_filter_by_language(self):
        data = test_data_four_doctors
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DoctorProfile.objects.count(), 4)
        self.assertEqual(DoctorProfile.objects.filter(price__range=[100, 200]).count(), 2)