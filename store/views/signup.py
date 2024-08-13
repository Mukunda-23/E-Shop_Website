import re
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.views import View
class Signup(View):
    def get(self,request):
      return render(request,'signup.html')
    def post(self,request):
        error_message = None
        value={}
        if request.method == 'POST':
            try:
                postdata = request.POST
                fname = postdata.get('fname')
                lname = postdata.get('lname')
                phone = postdata.get('phone')
                email = postdata.get('email')
                password = postdata.get('password')
                
                value={
                    'fname':fname,
                    'lname':lname,
                    'phone':phone,
                    'email':email
                }
                customer = Customer(fname=fname, lname=lname, phone=phone, email=email, password=password)
                # Validation
                error_message=self.validatecustomer(customer)
                # Saving data if no error
                if not error_message: 
                    customer.password=make_password(customer.password)  
                    customer.register() 
                    return redirect('homepage') # Assuming this method saves the customer
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
        data = {
        'error': error_message,
        'value': value
        }
        return render(request, 'signup.html',data)
    def validatecustomer(self,customer):
        error_message=None
        if not customer.fname:
            error_message = "First name required"
        elif len(customer.fname) < 4:
            error_message = "First name must be at least 4 characters long"
        elif not customer.lname:
            error_message = "Last name required"
        elif not customer.phone:
            error_message = "Phone number required"
        else:
            email_condition = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            if not re.match(email_condition,customer.email):
                error_message = "Invalid email format"
            elif not customer.password:
                error_message = "Password required"
            elif customer.isExists():
                error_message='email alrey register....'
        return error_message

           

        
        
    