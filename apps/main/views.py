from django.shortcuts import render # для отрисовки шаблона с контекстом.
from apps.books.filters import BookFilter
from apps.books.models import Book
from django.core.paginator import Paginator

# обработчик HTTP-запроса
def home(request):
    queryset = Book.objects.select_related('author').prefetch_related('genres')    # Базовый queryset с оптимизацией
    book_filter = BookFilter(request.GET, queryset=queryset)    # Применяем фильтр
    filtered_books = book_filter.qs.distinct()    # Получаем отфильтрованные книги (с устранением дублей)

    paginator = Paginator(filtered_books, 2)  # 2 книг на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'filter': book_filter,        # ← передаём сам фильтр в шаблон
        'books': page_obj,      # — список книг для отображения.
    }
    return render(request, 'main/home.html', context)