from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Client(models.Model):
    # datos cliente
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    document_type = models.CharField(max_length=50)
    document_number = models.IntegerField() 
    country = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50, unique=True)

    # datos del servicios
    service = models.CharField(max_length=50)

    # fecha y hora
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_start = models.CharField(max_length=5, editable=False)
    date_end = models.CharField(max_length=5, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:  
            now = timezone.now()
            self.date_start = now.strftime('%d/%m')
            self.date_end = (now + relativedelta(months=1)).strftime('%d/%m')
        super().save(*args, **kwargs)

    class Meta:
        db_table = "client"