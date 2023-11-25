from django.conf import settings
from django.db import models
from django.db.models import Q, F

class Specialization(models.Model):
    
    class Meta:
        db_table = 'specializations'
    
    specialization = models.CharField(max_length=120)
    doctors = models.ManyToManyField(
        to='Doctor',
    )


class Doctor(models.Model):
    
    class Meta:
        db_table = 'doctors'
    
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patr_name = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
    )
    premium = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
    )


class Vacation(models.Model):
    
    class Meta:
        db_table = 'vacations'
        constraints = [
            models.CheckConstraint(
                name='chk_end_gt_start',
                check=Q(end_date__gt=F('start_date'))
            )
        ]
    
    start_date = models.DateField()
    end_date = models.DateField()
    doctor = models.ForeignKey(
        to='Doctor',
        on_delete=models.CASCADE,
    )

