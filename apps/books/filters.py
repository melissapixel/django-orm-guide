import django_filters
from .models import Book, Author, Genre

class BookFilter(django_filters.FilterSet):     # — основной класс для фильтрации
    
    # поиск по названию
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',  # ← case-insensitive contains
        label='Название книги:'
    )

    # Фильтр по году: от
    year_from = django_filters.NumberFilter(
        field_name='published_year',    # поле модели
        lookup_expr='gte',  # → gte = greater than or equal → >=
        label='Год от'
    )
    # Фильтр по году: до
    year_to = django_filters.NumberFilter(
        field_name='published_year',
        lookup_expr='lte',  # = less than or equal → <=
        label='Год до'
    )
    # Фильтр по автору (выпадающий список)
    author = django_filters.ModelChoiceFilter(
        queryset=Author.objects.all(),
        label='Автор'
    )
    # Фильтр по жанру (выпадающий список)
    genre = django_filters.ModelChoiceFilter(
        field_name='genres',  # ← ManyToMany!
        queryset=Genre.objects.all(),
        label='Жанр'
    )

    # Сортировка
    o = django_filters.OrderingFilter(
        choices=(
            ('published_year', 'Год публикации (сначала старые)'),
            ('-published_year', 'Год публикации (сначала новые)'),
            ('title', 'Название (А→Я)'),
            ('-title', 'Название (Я→А)'),
        ),
        label="Сортировать по"
    )

    class Meta:
        model = Book    # какую модель фильтруем.
        fields = []  # ← "не создавай автоматических фильтров"