from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order

class CheckOut(View):
    def post(self,request):
        addres=request.POST.get('addres')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_product_by_id(list(cart.keys()))
        
        print(addres,phone,customer,cart,products)
        
        for product in products:
            order=Order(customer=Customer(id=customer),
                        product=product,
                        prise=product.prise,
                        quantity=cart.get(str(product.id)),
                        addres=addres,
                        phone=phone)
            order.save()
        request.session['cart'] = {}
        return redirect('cart') 