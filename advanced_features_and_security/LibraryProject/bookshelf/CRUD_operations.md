# CRUD Operations in Django Shell

---

## Create
```python
from library.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_year=1949
)
book
```
**Output:**
```python
<Book: 1984 by George Orwell (1949)>
```

---

## Retrieve
```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.id, retrieved_book.title, retrieved_book.author, retrieved_book.published_year
```
**Output:**
```python
(1, '1984', 'George Orwell', 1949)
```

---

## Update
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book.title
```
**Output:**
```python
'Nineteen Eighty-Four'
```

---

## Delete
```python
retrieved_book.delete()
Book.objects.all()
```
**Output:**
```python
<QuerySet []>
```

---
