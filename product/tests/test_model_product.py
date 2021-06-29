import pytest

from product.models import Category


@pytest.mark.django_db
def test_category_model():
    category = Category(
        name='IPHONE',
        description='IPHONE XR'
    )
    category.save()
    assert category.name == 'IPHONE'
    assert category.description == 'IPHONE XR'
    assert category.created_at
    assert category.updated_at
    assert str(category) == category.name
