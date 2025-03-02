from django.db import models


# Create your models here.

class Brand(models.Model):
    B_Id=models.BigIntegerField(primary_key = True)
    B_name=models.CharField(max_length=100)
    B_description=models.CharField(max_length=200,default="", editable=False)
   
    

class Catageory(models.Model):
    Cat_Id=models.BigIntegerField(primary_key = True)
    Cat_name=models.CharField(max_length=200)
    Parent=models.ForeignKey(
        "self", null=True,on_delete=models.CASCADE)
   


class Product(models.Model):

    P_Id=models.BigIntegerField(primary_key = True)
    P_name=models.CharField()
    Cat=models.ForeignKey(
        "Catageory", on_delete=models.CASCADE)
   
    B=models.ForeignKey(
        "Brand", on_delete=models.CASCADE)
    P_description=models.CharField(max_length=200,default="", editable=False)
    photo=models.CharField(max_length=200,default="", editable=False)
   




    

  






