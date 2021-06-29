from product.serializers import CategorySerializer


def test_valid_category_serializer():
    valid_serializer_data = {
        "name": "iphone",
        "description": "iphonexr"
    }
    serializer = CategorySerializer(
        data=valid_serializer_data
    )
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_category_serializer():
    invalid_serializer_data = {
        "name": "iphone",
    }
    serializer = CategorySerializer(
        data=invalid_serializer_data
    )

    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"description": ["This field is required."]}
