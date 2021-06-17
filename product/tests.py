import pytest
from django.test import TestCase
from asynctest import patch 
from product.models import Category, Product


def build_category():
    return Category.objects.create(
        name='Limpeza',
        description='Limpeza em Geral'
    )


# @pytest.mark.django_db
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


@pytest.mark.usefixtures(
    'create_category',
)
class TestCategory(TestCase):

    def test_get_all_categories(self):

        # Preparação

        category = self.fake_category

        # Assercao

        self.assertIsInstance(
            category, Category)

    def test_class_product(self):

        category = self.fake_category

        self.assertEqual(category.name, 'Limpeza')
        self.assertEqual(category.description, 'Limpeza em Geral')


@pytest.mark.usefixtures(
    'create_product',
)
class TestViewsProduct(TestCase):
    def test_create_products_route(self):

        payload = {
            "name":"TestProduct",
            "description":"TestProduct",
            "price":12.2,
            "stock":100,
            "gtin":'aghadj1',
            "category":1,
        }

        response = self.client.get('/create_product', data=payload)

        self.assertEqual(response.status_code, 200)

    def test_list_all_products_route(self):

        response = self.client.get('/products')

        self.assertEqual(response.status_code, 200)


    def test_update_products_route(self):

        response = self.client.patch('/update_product/1')

        self.assertEqual(response.status_code, 200)

    @patch('product.views.Product')
    def test_delete_products_route(
        self,
        product_mock
        ):

        product_mock = self.fake_product

        response = self.client.delete('/delete_product/1')

        self.assertEqual(response.status_code, 302)
