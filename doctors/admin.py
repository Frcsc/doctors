from django.contrib import admin
from doctors.models import (
    DoctorProfile, 
    OperatingHours,
    Category,
    Language,
    District
    )

class DoctorProfileAdmin(admin.ModelAdmin):

    readonly_fields = [
        'created_at',
        'updated_at'
    ]
    list_display = [
        'name',
        'address',
        'district_name',
        'postcode',
        'price'
    ]
admin.site.register(DoctorProfile, DoctorProfileAdmin)

class OperatingHoursAdmin(admin.ModelAdmin):
    list_display = [
        'doctor',
        'if_public_holiday',
        'weekday',
        'open_time',
        'close_time'
    ]
admin.site.register(OperatingHours, OperatingHoursAdmin)

class DoctorDescription(admin.ModelAdmin):
    list_display = [
        'name',
    ]

    readonly_fields = [
        'created_at',
        'updated_at'
    ]

admin.site.register(Category, DoctorDescription)
admin.site.register(District, DoctorDescription)
admin.site.register(Language, DoctorDescription)