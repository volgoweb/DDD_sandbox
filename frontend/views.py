from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .adapters.carts import add_to_cart, get_cart
from .adapters.products import get_all_products


@csrf_exempt
def add_to_cart_view(request):
    product_id = int(request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))
    add_to_cart(
        user_id=1,
        product_id=product_id,
        quantity=quantity,
    )
    return HttpResponse('ok')


def get_products(request):
    # products = [
    #     {
    #         'id': 1,
    #         'name': 'Product 1',
    #     },
    #     {
    #         'id': 2,
    #         'name': 'Product 2',
    #     },
    #     {
    #         'id': 3,
    #         'name': 'Product 3',
    #     },
    # ]
    products = get_all_products()
    return JsonResponse({
        'objects': products,
    })


def get_cart_data(request):
    user_id = 1
    cart_DTO = get_cart(user_id)
    return JsonResponse(cart_DTO, safe=False)
