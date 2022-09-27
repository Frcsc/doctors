from django.db import models
from necktie.mixins import BaseModel

class DoctorDesription(BaseModel):
    name = models.CharField(max_length=512)

    class Meta:
        abstract = True
        
    def __str__(self):
        return str(self.name)

