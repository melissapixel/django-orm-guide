from django.contrib import admin
from .models import Author, Genre, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_year', 'get_genres_display']
    list_filter = ['published_year', 'genres']
    search_fields = ['title', 'author__name']
    filter_horizontal = ['genres']

    @admin.display(description='Genres')
    def get_genres_display(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

admin.site.register(Book, BookAdmin)
# (или используй @admin.register, как раньше)