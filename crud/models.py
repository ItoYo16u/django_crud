from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class householdAccount(models.Model):
    item =models.CharField("item",max_length=30)
    price = models.IntegerField("price")
    category = models.CharField("category",max_length=30)
    memo = models.CharField('memo',max_length=140,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    updated_at =models.DateTimeField(auto_now=True)