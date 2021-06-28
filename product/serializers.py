from rest_framework import serializers
from .models import Category
from .models import Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
            ]
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description',
            instance.description
        )
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'gtin',
            'category'
        ]
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        ) 
