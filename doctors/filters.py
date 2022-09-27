from django.db.models import Q, Value
from django_filters import rest_framework as filters
from doctors.models import (
    Category,
    DoctorProfile,
    Language,
    District
)

class DoctorFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_search')
    language = filters.ModelChoiceFilter('language', to_field_name='name', queryset=Language.objects.all())
    category = filters.ModelChoiceFilter('category', to_field_name='name',queryset=Category.objects.all())
    district_name = filters.ModelChoiceFilter('district_name', to_field_name='name', queryset=District.objects.all())
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = DoctorProfile
        fields = ['search']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(address__icontains=value) |
            Q(postcode__icontains=value) |
            Q(email__icontains=value)
        )


