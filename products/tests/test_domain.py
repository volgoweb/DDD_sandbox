from django.test import TestCase

from ..domain.aggregates import Product

class Product2(Product):
    def bla(self):
        print('==============================Product2')
        print(self.id)
        print(self.name)


class TestProductAggregate(TestCase):
    def test_base(self):
        p2 = Product2(_id=1, name='name11')
        p2.bla()
        p1 = Product(_id=1, name='name11')
        print('============================== p1')
        print(p1.id)

