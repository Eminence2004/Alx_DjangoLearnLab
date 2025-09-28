from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create an author and a book to test with
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Initial Book',
            publication_year=2020,
            author=self.author
        )
        self.list_url = reverse('book-list')  # from your urls.py
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {'title': 'Updated Book'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        url = f"{self.list_url}?title=Initial Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_search_books(self):
        url = f"{self.list_url}?search=Initial"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ordering_books(self):
        url = f"{self.list_url}?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
