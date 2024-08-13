from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=50)
    prise=models.IntegerField(default=0)
    description=models.CharField(max_length=50,default="",null=True,blank=True)
    image=models.ImageField(upload_to="upload/prod")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
    
    @staticmethod
    def get_product_by_id(ids):
        if ids:
            return Product.objects.filter(id__in=ids)
        else:
            return Product.get_all_products()