from django import template


register = template.Library()

# Calculate the total of a line item in cart.
@register.filter(name='calc_total')
def calc_total(price, quantity):
    return price * quantity