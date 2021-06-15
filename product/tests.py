import pytest
from django.test import TestCase

from product.models import Category, Product


def build_category():
    return Category.objects.create(
        name='Limpeza',
        description='Limpeza em Geral'
    )


@pytest.mark.django_db
@pytest.fixture
def create_product(request):
    product = Product.objects.create(
        name='Sabão',
        description='Lava roupas',
        price=15.70,
        stock=20,
        gtin='a42fbabf-5e6e',
    )
    product.category.set([build_category()])

    request.cls.fake_product = product


@pytest.fixture
def create_category(request):
    category = Category.objects.create(
        name='Limpeza',
        description='Limpeza em Geral'
    )
    request.cls.fake_category = category


@pytest.mark.usefixtures(
    'create_category',
    'create_product',
)
class TestProduct(TestCase):

    def test_get_all_categories(self):

        # Preparação

        product = self.fake_product

        # Ação

        category = product.get_all_categories()

        # Assercao

        self.assertEqual(
            category, 'Nome: Limpeza - Descrição: Limpeza em Geral,')

    def test_class_product(self):

        product = self.fake_product

        self.assertEqual(product.name, 'Sabão')
        self.assertEqual(product.description, 'Lava roupas')
        self.assertEqual(product.price, 15.70)
        self.assertEqual(product.gtin, 'a42fbabf-5e6e')
        self.assertEqual(product.stock, 20)
        self.assertEqual(len([product.category]), 1)


class TestViewsProduct(TestCase):

    def test_list_all_products(self):

        response = self.client.get('/products')

        self.assertEqual(response.status_code, 200)
