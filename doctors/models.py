import uuid
from django.db import models
from necktie.mixins import BaseModel, ProfileMixins
from doctors.model_mixins import DoctorDesription

class Category(DoctorDesription):
    class Meta:
        verbose_name_plural = "Categories"

class District(DoctorDesription):
    class Meta:
        verbose_name_plural = "Districts"
        
class DoctorProfile(BaseModel, ProfileMixins):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    district_name = models.ForeignKey(District, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name) 

class Language(DoctorDesription):
    doctor = models.ManyToManyField(DoctorProfile)

  
class OperatingHours(BaseModel):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.PROTECT)
    if_public_holiday = models.BooleanField(default=True)
    weekday = models.IntegerField(null=True, blank=True)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return str(self.weekday)

    class Meta:
        verbose_name_plural = "Operating Hours"