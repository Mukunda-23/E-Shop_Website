from django.db import models


class Customer(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
