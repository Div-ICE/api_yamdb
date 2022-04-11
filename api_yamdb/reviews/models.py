import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField('Название категории', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Title(models.Model):
    """def get_rating(self):
        Функцию переписать, или вообще удалить
        rating = Review.objects.filter(title_id=id).aggregate('score')
        # функция неверная
        return rating # функция неверная
    """
    name = models.CharField(
        'Название',
        max_length=300,
    )
    year = models.IntegerField(
        'Год выпуска',
        validators=[
            MaxValueValidator(datetime.datetime.now().year),
            MinValueValidator(0),
        ]
    )
    rating = models.DecimalField(
        # get_rating(self),
        null=True,
        decimal_places=2,
        max_digits=2,
    )  # integer (Рейтинг на основе отзывов, если отзывов нет — `None`)
    description = models.TextField(
        'Описание',
        null=True,
        blank=True,
        max_length=3000,
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
    )

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.CharField(
        'Текст отзыва',
        max_length=3000,
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        'Оценка',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(
        'Дата публикации отзыва',
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.text


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE)
    text = models.CharField(
        'Текст комментария',
        max_length=300
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    pub_date = models.DateTimeField(
        'Дата публикации комментария',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.text
