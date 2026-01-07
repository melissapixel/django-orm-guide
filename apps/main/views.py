from django.shortcuts import render # для отрисовки шаблона с контекстом.
from apps.books.filters import BookFilter
from apps.books.models import Book

# обработчик HTTP-запроса
def home(request):
    # Базовый queryset с оптимизацией
    queryset = Book.objects.select_related('author').prefetch_related('genres')
    
    # Применяем фильтр
    book_filter = BookFilter(request.GET, queryset=queryset)
    
    # Получаем отфильтрованные книги (с устранением дублей)
    filtered_books = book_filter.qs.distinct()

    context = {
        'filter': book_filter,        # ← передаём сам фильтр в шаблон
        'books': filtered_books,      # — список книг для отображения.
    }
    return render(request, 'main/home.html', context)