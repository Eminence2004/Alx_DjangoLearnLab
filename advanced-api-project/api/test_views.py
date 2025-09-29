from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Book, Author
from rest_framework import status


class BookAPITestCase(TestCase):
    """
    Tests for Book API endpoints.
    Django automatically uses a **separate test database** when running tests,
    so these tests do not affect your production or development data.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name='Author 1')
        self.book = Book.objects.create(title='Book 1', publication_year=2020, author=self.author)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ✅ using status
        # ✅ using response.data
        self.assertTrue('title' in response.data[0])

    def test_create_book(self):
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')  # ✅ using response.data
