from rest_framework import serializers

from inventoryAPI.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'created_at']


class BaseProductSerializer(serializers.ModelSerializer):
    # company = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'price', 'description', 'category', 'company', 'created_at']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    
    
class ProductSerializer(BaseProductSerializer):
    # category = CategorySerializer()
    company = serializers.SlugRelatedField(slug_field='username', read_only=True)


class AdminProductSerializer(BaseProductSerializer):
    pass
