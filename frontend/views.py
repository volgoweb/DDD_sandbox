from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .adapters.carts import add_to_cart


@csrf_exempt
def add_to_cart(request):
    product_id = request.POST.get('product_id', None)
    quantity = request.POST.get('quantity', None)
    add_to_cart(1, product_id, quantity=quantity)
    return HttpResponse('ok')


