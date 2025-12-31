# django-orm-guide

🎯The idea of the project: "Book club with ratings and recommendations"
Users register, add books, rate, write short reviews. The system shows:

- TOP 10 books by average rating,
- How many books has each user read,
- Books that "your friends" have read (so far, just other users),
- The ability to find books by genre or author,
- And, for example, "all the books you haven't evaluated yet."

🎨This project:
- it does not require external APIs,
- uses ManyToMany and ForeignKey relationships,
- and provides a reason to optimize queries (so that there are no N+1),
- It allows you to enter business logic (for example, calculating the average rating, checking whether the user has given a rating),
and in rare cases, raw SQL (for example, for complex analytics or an index based on an expression).

<br>

------------------------

<br>

## ⚙️Запуск через Docker (требуется Docker и Docker Compose):

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/melissapixel/django-orm-guide.git
   cd ваш-проект

2.  Создайте .env из шаблона:
    ```bash
    cp .env.example .env

   Отредактируйте .env — укажите свои пароли.

3.  Запустите:
    ```bash
    docker-compose up --build

4. Примените миграции (в новом терминале):
     ```bash
     docker-compose exec web python manage.py migrate

5. Откройте: http://localhost:8000


-------


