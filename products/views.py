from django.shortcuts import render
from .models import ProductModel, CategoryModel
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#creating a new product
@api_view(['POST'])
def create_product(request):
    products_serializer = ProductSerializer(data=request.data)
    if products_serializer.is_valid():
        products_serializer.save()
        return Response(products_serializer.data,status=status.HTTP_201_CREATED)
    return Response(products_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#getting details of all products
@api_view(['GET'])
def retrieve_products(request):
    products = ProductModel.objects.all()
    
    category = request.query_params.get('category_name')
    min_price = request.query_params.get('min_price')
    max_price = request.query_params.get('max_price')

    if category:
        products=products.filter(category_name__category_name__iexact=category)
    if min_price:
        products=products.filter(price__gte=min_price)
    if max_price:
        products=products.filter(price__lte=max_price)
    
    products_serializer = ProductSerializer(products, many=True)
    return Response(products_serializer.data,status=status.HTTP_200_OK)

#to update or delete a product based on product id
@api_view(['PATCH','DELETE'])
def update_products(request,pk):
    try:
        product=ProductModel.objects.get(id=pk)
    except ProductModel.DoesNotExist:
        return Response({'message':'Product does not exist'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        product_serializer=ProductSerializer(product,data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'message':'Product deleted'},status=status.HTTP_204_NO_CONTENT)

#to create a new category
@api_view(['POST'])
def create_category(request):
    category_serializer = CategorySerializer(data=request.data)
    if category_serializer.is_valid():
        category_serializer.save()
        return Response(category_serializer.data, status=status.HTTP_201_CREATED)
    return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to get details of all categories
@api_view(['GET'])
def retrieve_categories(request):
    categories = CategoryModel.objects.all()
    category_serializer = CategorySerializer(categories, many=True)
    return Response(category_serializer.data,status=status.HTTP_200_OK)