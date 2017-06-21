class AddToCart(IDomainCommand):
    def execute(self, user: User, product_modification: ProductModification, quantity: int, dto: DTOAddToCart):
        pass