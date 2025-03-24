from rest_framework import serializers
from .models import Book, Author, Genre, Language, Publisher, BookInstance
from django.contrib.auth.models import User
# class BookSerializer(serializers.Serializer):
#    title = serializers.CharField(max_length=200)
#    year = serializers.CharField(max_length=4)
#    isbn = serializers.CharField(max_length=13)
#    summary = serializers.CharField(max_length=1000)
#    language = serializers.CharField()
#    publisher = serializers.CharField()
#    genre = serializers.CharField()
#    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
#    def create(self, validated_data):
#       return Book.objects.create(**validated_data)
#    def update(self, instance, validated_data):
#       instance.title = validated_data.get('title', instance.title)
#       instance.year = validated_data.get('year', instance.year)
#       instance.isbn = validated_data.get('isbn', instance.isbn)
#       instance.summary = validated_data.get('summary', instance.summary)
#       instance.language = validated_data.get('language', instance.language)
#       instance.publisher = validated_data.get('publisher', instance.publisher)
#       instance.genre = validated_data.get('genre', instance.genre)
#       instance.author = validated_data.get('author_id', instance.author)
#       instance.save()
#       return instance

class BookSerializer(serializers.ModelSerializer):
   # owner = serializers.ReadOnlyField(source='owner.username')
   class Meta:
      model = Book
      fields = ('id', 'title', 'year', 'isbn', 'summary', 'language', 'publisher', 'genre', 'author', 'owner')



class UserSerializer(serializers.ModelSerializer):
   # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
   class Meta:
      model = User
      fields = ('id', 'username')

class GenreSerializer(serializers.ModelSerializer):
   # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
   class Meta:
      model = Genre
      fields = ('id', 'name')
   
class LanguageSerializer(serializers.ModelSerializer):
   # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
   class Meta:
      model = Language
      fields = ('id', 'name')

class PublisherSerializer(serializers.ModelSerializer):
   # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
   class Meta:
      model = Publisher
      fields = ('id', 'name')

class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
      model = Author
      fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'about')

class BookInstanceSerializer(serializers.ModelSerializer):
   class Meta:
      model = BookInstance
      fields = ('id', 'book', 'inv_nom', 'status', 'due_back', 'borrower')