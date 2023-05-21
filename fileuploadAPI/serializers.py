from rest_framework import serializers

from fileuploadAPI.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author', 'pdf', 'cover']
        extra_kwargs = {'pdf': {'required': True}}
        
        def update(self, instance, validated_data):
            # Exclude 'pdf' and 'cover' from validated_data to prevent their modification
            validated_data.pop('pdf', None)
            validated_data.pop('cover', None)
            return super().update(instance, validated_data)