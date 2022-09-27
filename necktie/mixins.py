from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.localtime)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ProfileMixins(models.Model):
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    postcode = models.CharField(max_length=512)
    email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    consultation_fee_description = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        abstract = True