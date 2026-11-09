from django.db import models
from django.contrib.auth.models import User
from places.models import Place


class Review(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Место"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Пользователь"
    )
    rating = models.PositiveIntegerField(
        verbose_name="Оценка (1-5)"
    )
    comment = models.TextField(
        verbose_name="Комментарий"
    )

    def __str__(self):
        return f"{self.place.name} - {self.rating}/5"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-id"]
