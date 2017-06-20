from .api.v_1_0.commands import AddToCart

def add_to_cart(request):
    product_modification_id = request.POST.get('product_modification_id', None)
    service = AddToCart()
    service.run()