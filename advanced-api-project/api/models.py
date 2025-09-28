from django.db import models

# Create your models here.


# Author model represents an individual writer who can have many books
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author’s full name

    def __str__(self):
        return self.name
    

# Book model represents a book written by an Author.
# It links back to Author with a ForeignKey (one-to-many relationship).
class Book(models.Model):
    title = models.CharField(max_length=255)             # Book title
    publication_year = models.IntegerField()             # Year published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title