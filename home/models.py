from django.db import models

class Fish(models.Model):
    fish_id = models.AutoField
    fish_name = models.CharField(max_length=50)
    fish_desc = models.CharField(max_length=300)
    date = models.DateField()
    fish_price = models.IntegerField()
    fish_image = models.ImageField( upload_to="media/")

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    date = models.DateField()
    product_price = models.IntegerField()
    product_image = models.ImageField( upload_to="media/")    
 

class Food(models.Model):
    food_id = models.AutoField
    food_name = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=300)
    date = models.DateField()
    food_price = models.IntegerField()
    food_image = models.ImageField( upload_to="media/")  

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email= models.CharField(max_length=111)
    address= models.CharField(max_length=130)
    city= models.CharField(max_length=111)
    phone= models.CharField(max_length=111,default="")



