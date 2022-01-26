from urllib import response
from rest_framework import mixins, viewsets, generics, views
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters
from .filters import BookFilter
from rest_framework.response import Response
import requests

class BookViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny,]


class BookListAPIView(
    generics.ListAPIView
):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny,]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

class BookImportAPIView(views.APIView):
    def post(self,request,*args, **kwargs):
        keyword = request.data['keyword']
        url=f'https://www.googleapis.com/books/v1/volumes?q={keyword}'
        response = requests.get(url)
        print(response.json())
        for item in response.json()['items']:
            data = {
                'title': item['volumeInfo']['title'],
                'author':item['volumeInfo']['authors'][0],
                'pub_date': item['volumeInfo']['publishedDate'],
                'isbn':item.get('volumeInfo', {}).get('industryIdentifiers')[0].get('identifier'),
                'pages_number':item.get('volumeInfo',{}).get('pageCount'),
                'link_url':item.get('volumeInfo',{}).get('imageLinks',{}).get('smallThumbnail'),
                'pub_language':item['volumeInfo']['language'],
            }

            serializer = BookSerializer(data=data)
            print(serializer.is_valid(), serializer.errors)
            if serializer.is_valid():
                serializer.save()

        return Response(data={'message':'imported'})