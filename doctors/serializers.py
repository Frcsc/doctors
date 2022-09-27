from rest_framework import serializers

from doctors.models import (
    DoctorProfile,
    OperatingHours,
    Category,
    Language,
    District
)
from doctors.model_mixins import DoctorDesription

class DoctorDesriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDesription
        fields = [
            'id',
            'name'
        ]  

class DoctorProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DoctorProfile
        fields = [
            'id',
            'name',
            'address',
            'postcode',
            'email',
            'price',
            'consultation_fee',
            'consultation_fee_description'
        ]

class DoctorProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorProfile
        fields = [
            *DoctorProfileSerializer.Meta.fields,
            'district_name',
            'language',
            'category',
            'operating_hours'
        ]

    class OperatinghoursSerializer(serializers.ModelSerializer):
        class Meta:
            model = OperatingHours
            fields = [
                'if_public_holiday',
                'weekday',
                'open_time',
                'close_time'
            ]

    class LanguageSerializer(DoctorDesriptionSerializer):
        class Meta:
            model = Language
            fields = [
                *DoctorDesriptionSerializer.Meta.fields
            ]

    class CategorySerializer(DoctorDesriptionSerializer):
        class Meta:
            model = Category
            fields = [
                *DoctorDesriptionSerializer.Meta.fields
            ]
    class DistrictSerializer(DoctorDesriptionSerializer):
        class Meta:
            model = District
            fields = [
                *DoctorDesriptionSerializer.Meta.fields
            ]
    language = LanguageSerializer(many=True, source='language_set', read_only=False)
    category = CategorySerializer()
    district_name = DistrictSerializer()
    operating_hours = OperatinghoursSerializer(many=True, source='operatinghours_set') 

    def validate_language(self, data):
        list_of_languages = []
        for each_language in data:
            if Language.objects.filter(name=each_language['name']).exists():
                language = Language.objects.get(name=each_language['name'])
            else:
                language = Language.objects.create(name=each_language['name'])
            list_of_languages.append(language)
        return list_of_languages

    def validate_email(self, data):
        if DoctorProfile.objects.filter(email=data).exists():
            raise serializers.ValidationError( "An acoount associated with this email already exist") 
        return data

    def validate_district_name(self, data):
        if District.objects.filter(name=data['name']).exists():
            district_name = District.objects.get(name=data['name'])
        else:
            district_name = District.objects.create(name=data['name'])
        return district_name

    def validate_category(self, data):
        if Category.objects.filter(name=data['name']).exists():
            category = Category.objects.get(name=data['name'])
        else:
            category = Category.objects.create(name=data['name'])
        return category

    def validate_operating_hours(self, data):
        for each_week in data:
            if each_week['weekday'] not in range(1, 8):
                raise serializers.ValidationError( "Please enter a value between 1 and 7") 
        return data

    def create(self, validated_data):
        doctor = DoctorProfile.objects.create(
            name=validated_data['name'],
            address=validated_data['address'],
            district_name=validated_data['district_name'],
            postcode=validated_data['postcode'],
            email=validated_data['email'],
            price=validated_data['price'],
            consultation_fee=validated_data['consultation_fee'],
            consultation_fee_description=validated_data['consultation_fee_description'],
            category=validated_data['category']
        )
        
        for each_language in validated_data['language_set']:
            each_language.doctor.add(doctor)

        for each_day in validated_data['operatinghours_set']:
            OperatingHours.objects.create(
                doctor=doctor,
                if_public_holiday=each_day['if_public_holiday'],
                weekday=each_day['weekday'],
                open_time=each_day['open_time'],
                close_time=each_day['close_time']
            )
        return doctor