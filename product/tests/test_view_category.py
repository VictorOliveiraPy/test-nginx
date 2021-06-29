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


@pytest.mark.django_db
def test_get_single_category(client, add_category):
    category = add_category(
        name='Iphone',
        description="xr 64"
    )
    resp = client.get(f"/api/category/{category.id}/")
    assert resp.status_code == 200
    assert resp.data["name"] == "Iphone"


def test_get_single_category_incorrect_id(client):
    resp = client.get("/api/category/buuh/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_category(client, add_category):

    category_one = add_category(
        name='Iphone',
        description='XR'
    )
    category_two = add_category(
        "Iphone",
        'XR'
    )
    resp = client.get(
        reverse('api-category')
    )
    assert resp.data[0]["name"] == category_one.name
    assert resp.data[1]["name"] == category_two.name


@pytest.mark.django_db
def test_remove_category(client, add_category):
    category = add_category(
        name="iphone",
        description="xr"
    )

    resp = client.get(
        f"/api/category/{category.id}/"
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "iphone"

    resp_two = client.delete(
        f"/api/category/{category.id}/"
    )
    assert resp_two.status_code == 204

    resp_three = client.get(
        "/api/category/"
    )
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_category_incorrect_id(client):
    resp = client.delete(f"/api/category/99/")
    assert resp.status_code == 404



@pytest.mark.django_db
def test_update_category(client, add_category):
    category = add_category(
        name="iphone",
        description="xr"
    )

    resp = client.put(
        f"/api/category/{category.id}/",
        {"name": "iphonexr",
         "description": "test"
         },
        content_type="application/json"
    )
    assert resp.status_code == 200
    assert resp.data["name"] == "iphonexr"
    assert resp.data["description"] == "test"

    resp_two = client.get(f"/api/category/{category.id}/")
    assert resp_two.status_code == 200
    assert resp_two.data["name"] == "iphonexr"
    assert resp.data["description"] == "test"


@pytest.mark.django_db
def test_update_category_incorrect_id(client):
    resp = client.put(f"/api/category/99/")
    assert resp.status_code == 404

   
@pytest.mark.django_db
def test_update_category_invalid_json(client, add_category):
    category = add_category(
        name="iphone",
        description="test"
    )
    resp = client.put(
        f"/api/category/{category.id}/",
        {}, content_type="application/json"
    )
    assert resp.status_code == 400


@pytest.mark.django_db
def test_update_category_invalid_json_keys(client, add_category):
    category = add_category(
        name="iphone",
        description="test"
    )

    resp = client.put(
        f"/api/category/{category.id}/",
        {"name": "iphone"},
        content_type="application/json",
    )
    assert resp.status_code == 400
