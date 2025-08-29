from django.contrib import admin

# Register your models here.
class BookAdmin('title', 'author', 'Publication_year')
list_display = ('author', 'publication_year')
list_filter = ('author', 'publication_year')
search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

