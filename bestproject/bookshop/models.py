from django.db import models


class Author(models.Model):
    class Meta:
        db_table = "author"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField(
            max_length=150,
            db_index=True,
            verbose_name="Имя",
            help_text="тут введите имя автора")

    def __str__(self):
        return self.name


class Genre(models.Model):
    class Meta:
        db_table = "genre"
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        db_table = "book"
        verbose_name = "книга"
        verbose_name_plural = "книги"

    name = models.CharField(max_length=150, db_index=True)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    book_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    class Meta:
        db_table = "Comment"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    text = models.TextField()
    comment_book = models.ForeignKey(
            Book,
            on_delete=models.CASCADE,
            related_name="Comment")

    def __str__(self):
        return self.text[:10] + "..."
