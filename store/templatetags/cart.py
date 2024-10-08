from django import template


register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='prise_total')
def prise_total(product,cart):
    return product.prise * cart_quantity(product,cart)

@register.filter(name='total_cart_prise')
def total_cart_prise(products,cart):
    sum=0
    for p in products:
        sum += prise_total(p,cart)  
    return sum
    
