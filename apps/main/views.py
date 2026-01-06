from django.shortcuts import render # для отрисовки шаблона с контекстом.
from apps.books.models import Book, Author, Genre

# обработчик HTTP-запроса
def home(request):
    # Получаем параметры фильтрации из GET-запроса
    year_from = request.GET.get('year_from')
    year_to = request.GET.get('year_to')
    author_id = request.GET.get('author')
    genre_id = request.GET.get('genre')

    # Начинаем с оптимизированного запроса. менеджер модели Book
    books = Book.objects.select_related('author').prefetch_related('genres')    #  — нет N+1

    # Применяем фильтры
    if year_from:
        books = books.filter(published_year__gte=year_from)
    if year_to:
        books = books.filter(published_year__lte=year_to)
    if author_id:
        books = books.filter(author_id=author_id)
    if genre_id:
        books = books.filter(genres__id=genre_id)

    # Убираем дубли, если был фильтр по жанру (ManyToMany → дубли)
    books = books.distinct()

    # Получаем списки для формы
    authors = Author.objects.all()
    genres = Genre.objects.all()

    context = {
        'books': books,
        'authors': authors,
        'genres': genres,
        'year_from': year_from,
        'year_to': year_to,
        'selected_author': author_id,
        'selected_genre': genre_id,
    }
    return render(request, 'main/home.html', context)