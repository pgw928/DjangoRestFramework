from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# 현재 식재료 
class Grocery(models.Model):
    id = models.AutoField(primary_key=True) #PK(현재식재료PK)
    email = models.CharField(max_length=50, null=True) # FK(사용자id값)
    all_grocery_id = models.IntegerField(blank=True, null=True) # FK(식료품id값)
    name = models.CharField(max_length=20, null=True)
    count = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    gubun = models.CharField(max_length=5, null=True)
    cordinate = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'GROCERY'

    def __str__(self):
        return '{0}'.format(self.reg_date)

# 전체 식재료 
class AllGrocery(models.Model):
    id = models.AutoField(primary_key=True) #PK(현재식재료PK)
    name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'ALL_GROCERY'

    def __str__(self):
        return self.name

