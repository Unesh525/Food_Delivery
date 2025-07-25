from django.db import models
from pyexpat import model


class admindata(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models. CharField (max_length=100,primary_key=True)
    def __str__(self):
        return self.email

class logindata(models.Model):
    email = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class tdata(models.Model):
    id=models.IntegerField(auto_created=0,primary_key=True)
    email = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.CharField()
    transaction = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    def __str__(self):
        return self.date

class photodata(models.Model):
    email = models.CharField(max_length=100,primary_key=True)
    photo =models.CharField(max_length=100)
    def __str__(self):
        return self.email

class userdata(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email=models. CharField (max_length=100,primary_key=True)
    balance = models.IntegerField()
    def __str__(self):
        return self.email

class itemdata(models.Model):
    item_name = models.CharField(max_length=100,primary_key=True)
    item_description = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    item_price =models.IntegerField()
    def __str__(self):
        return self.item_name
class cartdata(models.Model):
    item_name = models.CharField(max_length=100,primary_key=True)
    quantity = models.IntegerField()
    main_price =  models.IntegerField()
    item_price = models.IntegerField()
    photo = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    email=models. CharField (max_length=100)
    def __str__(self):
        return self.item_name

class ordersdata(models.Model):
    order_id = models.IntegerField(auto_created=0,primary_key=True)
    user_email = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order_date = models.CharField()
    request  = models.CharField(max_length=100)
    def __str__(self):
        return self.user_email



