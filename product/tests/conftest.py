import pytest

from product.models import Category


@pytest.fixture(scope='function')
def add_category():
    def __add_category(name, description):

        category = Category.objects.create(
            name=name,
            description=description,
        )
        return category
    return __add_category
