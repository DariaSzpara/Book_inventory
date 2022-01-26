from rest_framework import response, routers

from .views import BookViewSet,BookListAPIView, BookImportAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'book'

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')
urlpatterns = [
    path('books-list/', BookListAPIView.as_view(), name='books-list'),
    path('book-import/',BookImportAPIView.as_view(), name='book-import'),
] + router.urls
