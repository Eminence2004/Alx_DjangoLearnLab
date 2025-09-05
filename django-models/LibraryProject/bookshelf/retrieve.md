# Retrieve Operation

## Command
```python
from library.models import Book
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.id, retrieved_book.title, retrieved_book.author, retrieved_book.published_year
```

## Expected Output
```python
(1, '1984', 'George Orwell', 1949)
```

✅ Retrieved all attributes of the created book.
