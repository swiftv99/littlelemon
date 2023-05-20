from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'price', 'description', 'category', 'created_at']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     category = Category.objects.create(**category_data)
    #     product = Product.objects.create(category=category, **validated_data)
    #     return product

    # def update(self, instance, validated_data):
    #     category_data = validated_data.pop('category')
    #     category_serializer = self.fields['category']
    #     category_instance = instance.category
    #     category = category_serializer.update(category_instance, category_data)
    #     instance.category = category
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance
