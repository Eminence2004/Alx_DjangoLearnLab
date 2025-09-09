# Create Operation

## Command
```python
from library.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_year=1949
)
book
```

## Expected Output
```python
<Book: 1984 by George Orwell (1949)>
```

✅ Book instance successfully created.
