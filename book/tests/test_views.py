import pytest
from django.urls import reverse
from ..models import Book

@pytest.mark.django_db
def test_book_create_view(api_client):
    
    response = api_client.post(reverse('book:book-list'), data={
        "title": "test_title",
        "author": "test_author",
        "pub_date": "2020-12",
        "isbn": "1231231231231",
        "pages_number": 55,
        "link_url": "https://example.pl",
        "pub_language": "pl"
    }, format='json')

    assert response.status_code == 201
    assert response.json() == {
        "title": "test_title",
        "author": "test_author",
        "pub_date": "2020-12",
        "isbn": "1231231231231",
        "pages_number": 55,
        "link_url": "https://example.pl",
        "pub_language": "pl"
    }


@pytest.mark.django_db
def test_book_update_view(api_client):
    
    book = Book.objects.create(
        title = "test_title",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "1231231231231",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "pl"
    )

    response = api_client.patch(reverse('book:book-detail', args = [book.id]), data={
        "title": "test_123",
        "author": "test_author",
        "pub_date": "2020-12",
        "isbn": "1231231231231",
        "pages_number": 55,
        "link_url": "https://example.pl",
        "pub_language": "pl"
    }, format='json')

    assert response.status_code == 200
    assert response.json()['title'] == 'test_123'



@pytest.mark.django_db
def test_book_destroy_view(api_client):
    
    book = Book.objects.create(
        title = "test_title",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "1231231231231",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "pl"
    )

    response = api_client.delete(reverse('book:book-detail', args = [book.id]), format='json')

    assert response.status_code == 204


@pytest.mark.django_db
def test_book_list_view_filter_by_title(api_client):
    
    book_1 = Book.objects.create(
        title = "test_title",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "1231231231231",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "pl"
    )

    book_2 = Book.objects.create(
        title = "Hobbit",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "1231231231231",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "pl"
    )

    response = api_client.get(reverse('book:books-list'), {'title':'Hobbit'}, format='json')

    assert response.status_code == 200
    assert response.json()['count'] == 1


@pytest.mark.django_db
def test_book_list_view_filter_by_isbn(api_client):
    
    book_1 = Book.objects.create(
        title = "test_title",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "1111111111111",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "pl"
    )

    book_2 = Book.objects.create(
        title = "Hobbit",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "2222222222222",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "pl"
    )

    response = api_client.get(reverse('book:books-list'), {'isbn':'1111111111111'}, format='json')

    assert response.status_code == 200
    assert response.json()['count'] == 1


@pytest.mark.django_db
def test_book_list_view_filter_by_pub_language(api_client):
    
    book_1 = Book.objects.create(
        title = "test_title",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "1111111111111",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "pl"
    )

    book_2 = Book.objects.create(
        title = "Hobbit",
        author = "test_author",
        pub_date = "2020-12",
        isbn = "2222222222222",
        pages_number = 55,
        link_url = "https://example.pl",
        pub_language = "en"
    )

    response = api_client.get(reverse('book:books-list'), {'pub_language':'en'}, format='json')

    assert response.status_code == 200
    assert response.json()['count'] == 1
 
