from django.db import models

# Create your models here.


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
    date = models.DateField()
    info = models.TextField()
