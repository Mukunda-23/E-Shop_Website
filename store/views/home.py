from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        prod = None
        categ= Category.get_all_category()
        categoryID= request.GET.get('category')
        if categoryID:
            prod=Product.get_all_products_by_category_id(categoryID)
        else:
            prod=Product.get_all_products()

        data={}
        data['prod'] = prod
        data['categ']= categ
        #print('you are:-',request.session.get('email'))
        #print('you are:-',request.session.get('customer_id'))
        return render(request,"index.html",data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if product in cart:
            quantity = cart[product]
            if remove:
                if quantity <= 1:
                    cart.pop(product)
                else:
                    cart[product] = quantity - 1
            else:
                cart[product] = quantity + 1
        else:
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('homepage')

