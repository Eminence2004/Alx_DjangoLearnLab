from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer serializes the Author model and nests related books dynamically.
class AuthorSerializer(serializers.ModelSerializer):
    # This nests a list of books using the BookSerializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
