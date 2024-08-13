from django.db import models
from .product import Product
from .customer import Customer
import datetime
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone=models.CharField(max_length=100,default='')
    addres= models.CharField(max_length=100,default='',blank=True)
    quantity=models.IntegerField(default=1)
    prise=models.IntegerField(default=0)
    date=models.DateField(default=datetime.datetime.today)

    def placeorder(self):
        self.save()