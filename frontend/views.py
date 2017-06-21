from django.views.generic import TemplateView

from .adapters.carts import add_to_cart

def add_to_cart(request):
    product_modification_id = request.POST.get('product_modification_id', None)
    add_to_cart(request.user.pk, product_modification_id)

