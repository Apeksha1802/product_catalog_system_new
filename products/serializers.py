from rest_framework import serializers
from .models import ProductModel, CategoryModel

#serializer for category model
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoryModel
    fields = ['id','category_name']

#serializer for product model
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SlugRelatedField(
        queryset = CategoryModel.objects.all(),
        slug_field = 'category_name',
    )
    class Meta:
        model=ProductModel
        fields=['id', 'name', 'description', 'price', 'category_name']
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be non-negative")
        return value