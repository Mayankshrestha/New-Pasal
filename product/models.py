from django.db import models 
# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length = 60)
	parent = models.ForeignKey('self', null = True, blank = True)

class Product(models.Model):
	product_name = models.CharField(max_length = 50)
	category = models.ForeignKey('Category')
	price = models.IntegerField()
	stock_qty = models.IntegerField()
	product_image = models.ImageField(blank = True, null = True)

class Customer(models.Model):
	full_name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 50)
	profile_image = models.ImageField(blank = True , null = True)

class Sales(models.Model):
	product_id = models.ForeignKey ('Product')
	customer_id = models.ForeignKey ('Customer')
	quantity = models.IntegerField()
	sales_date = models.DateTimeField()

	
