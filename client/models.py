from django.db import models
from django.core.validators import MaxValueValidator

class Client(models.Model):
    # BUY_STATUS = [
    #     (1, 'CREADO'),
    #     (2, 'PENDIENTE'),
    #     (3, 'PAGADO'),
    #     (4, 'RECHAZADO')
    # ]

    # datos cliente
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    document_type = models.CharField(max_length=50)
    document_number = models.IntegerField() 
    country = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    movil_type = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50)

    # datos del servicios
    service = models.CharField(max_length=50)
    payment_day = models.PositiveIntegerField(validators=[MaxValueValidator(31)], null=True)

    # datos para mercadopago

    # fecha y hora
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "client"