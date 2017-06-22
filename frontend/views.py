from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .adapters.carts import add_to_cart
from .adapters.products import get_all_products


@csrf_exempt
def add_to_cart_view(request):
    product_id = request.POST.get('product_id', None)
    quantity = request.POST.get('quantity', None)
    add_to_cart(1, product_id, quantity=quantity)
    return HttpResponse('ok')


def get_products(request):
    products = [
        {
            'id': 1,
            'name': 'Product 1',
        },
        {
            'id': 2,
            'name': 'Product 2',
        },
        {
            'id': 3,
            'name': 'Product 3',
        },
    ]
    products = get_all_products()
    return JsonResponse({
        'objects': products,
    })
