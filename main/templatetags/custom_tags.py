from django import template
from django.shortcuts import render
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag
def total_price(price, count):
    return int(price) * int(count)


@register.simple_tag
def custom_for(product_list):
    rendered_items = []
    for product in product_list:
        render_item = render_to_string('card_products.html', {'product': product})
        rendered_items.append(render_item)
    return '\n'.join(rendered_items)
