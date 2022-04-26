from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from users.models import User


def my_year_validator(value):
        if value < 0 or value > timezone.now().year:
            raise ValidationError(('%(value)s is not a correcrt year!'),
                params={'value': value},
            )


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=256, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.slug


class Category(models.Model):
    name = models.CharField('Название категории', max_length=256, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.slug


class Title(models.Model):
    name = models.CharField(
        'Название',
        max_length=300,
        db_index=True
    )
    year = models.IntegerField(
        'Год выпуска',
        validators=[my_year_validator]
    )
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
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.CharField(
        'Текст отзыва',
        max_length=3000,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        db_index=True
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
        db_index=True
    )

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name="unique_review")
        ]

    def __str__(self) -> str:
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments')
    text = models.CharField(
        'Текст комментария',
        max_length=300,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        db_index=True
    )
    pub_date = models.DateTimeField(
        'Дата публикации комментария',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self) -> str:
        return self.author
