from rest_framework import serializers
from .models import Book
class BookSerializer(serializers.Serializer):
   title = serializers.CharField(max_length=200)
   year = serializers.CharField(max_length=4)
   isbn = serializers.CharField(max_length=13)
   summary = serializers.CharField(max_length=1000)
   author = serializers.CharField()
   
   def create(self, validated_data):
    return Book.objects.create(**validated_data)
