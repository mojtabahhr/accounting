from pyexpat import model
from typing import TYPE_CHECKING
from django.db import models
from datetime import datetime
# Create your models here.



class WorkerModel(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    phone_number = models.CharField(max_length=11)
    time_enterd = models.DateTimeField()
    time_exited = models.DateTimeField()
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.last_name}'
    


class TimeWorkModel(models.Model):
    worker = models.ForeignKey(to=WorkerModel, on_delete=models.PROTECT)
    date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    info = models.TextField()

    def __str__(self):
        return self.worker
    


class SalaryModel(models.Model):
    MONTH = (
        (1 , 'فروردین'),
        (2 , 'اردیبهشت'),
        (3 , 'خرداد'),
        (4 , 'تیر'),
        (5 , 'مرداد'),
        (6 , 'شهریور'),
        (7 , 'مهر'),
        (8 , 'آبان'),
        (9 , 'آذی'),
        (10 , 'دی'),
        (11 , 'بهمن'),
        (12 , 'اسفند'),
    )
    worker = models.ForeignKey(to=WorkerModel, on_delete=models.PROTECT)
    year = models.IntegerField()
    month = models.CharField(max_length=30,choices=MONTH)


class CostsModel(models.Model):
    
    WHO = (
        ('مجتبا','مجتبا'),
        ('امیر', 'امیر'),
        ('بابا', 'بابا')
    )

    TYPE = (
        ('هزینه های جاری', 'هزینه های جاری'),
        ('خوراک','خوراک')
    )
    who = models.CharField(max_length=30,choices=WHO)
    title = models.CharField(max_length=256)
    amount = models.IntegerField(blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    cost_type = models.CharField(max_length=30,choices=TYPE)
    info = models.TextField()


class BillsModel(models.Model):
    date = models.DateField()
    seller = models.CharField(max_length=256)
    address = models.CharField(max_length=500)
    acheteur = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    
