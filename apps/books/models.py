from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # ← чтобы писать author.books.all()
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='books'  # ← чтобы писать genre.books.all(). — для обратных связей в ORM (очень важно для запросов!)
    )
    published_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} ({self.published_year})"

    class Meta:
        ordering = ['-published_year', 'title']