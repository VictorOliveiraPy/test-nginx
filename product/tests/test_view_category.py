import pytest

from django.urls import reverse

from product.models import Category


@pytest.mark.django_db
def test_add_category(client):
    category = Category.objects.all()
    assert len(category) == 0

    resp = client.post(reverse(
        "api-category"),
        {
            "name": "iphone",
            "description": "ihpone xr",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data['name'] == 'iphone'
    category = Category.objects.all()
    assert len(category) == 1



@pytest.mark.django_db
def test_add_invalid_json_category(client):
    category = Category.objects.all()
    assert len(category) == 0

    resp = client.post(reverse(
        "api-category"),
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    study = Category.objects.all()
    assert len(study) == 0