from django.db import models
from django.db.models import Q

from datetime import date


class Department(models.Model):
    
    class Meta:
        db_table = 'departments'
    
    department_id = models.AutoField(
        db_column='department_id',
        primary_key=True,
    )
    name = models.CharField(
        db_column='department',
        max_length=100,
    )
    sponsors = models.ManyToManyField(
        to='Sponsor',
        through='Donation',
        through_fields=('department', 'sponsor')
    )


class Wards(models.Model):
    
    class Meta:
        db_table = 'wards'
    
    name = models.CharField(
        db_column='ward',
        max_length=10,
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.CASCADE,
    )


class Sponsor(models.Model):
    
    class Meta:
        db_table = 'sponsors'
    
    name = models.CharField(
        db_column='sponsor',
        max_length=250,
    )


class Donation(models.Model):
    
    class Meta:
        db_table = 'donations'
    
    amount = models.DecimalField(
        max_digits=11, 
        decimal_places=2,
    )
    date = models.DateField(
        auto_now_add=True,
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.CASCADE,
    )
    sponsor = models.ForeignKey(
        to='Sponsor',
        on_delete=models.CASCADE,
    )

