from rest_framework import serializers
from rest_framework.response import Response

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = (
            'title',
            'author',
            'pub_date',
            'isbn',
            'pages_number',
            'link_url',
            'pub_language',
        )

