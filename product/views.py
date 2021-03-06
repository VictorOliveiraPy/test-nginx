from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView 
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer

from .models import Product
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProductSerializer


class CategoryList(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()

        serializer = CategorySerializer(
            category,
            many=True
        )
        return Response(
            serializer.data
        )

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
            },
         )
    )
    def post(self, request, format=None):
        serializer = CategorySerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(
            serializer.data
        )
        
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(
            category,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class ProductList(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()

        serializer = ProductSerializer(
            product,
            many=True
        )
        return Response(
            serializer.data
        )

    def post(self, request, format=None):
        serializer = ProductSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(
            serializer.data
        )

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(
            product, 
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
