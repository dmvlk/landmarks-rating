from django.db import models


class Place(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название места"
    )
    address = models.CharField(
        max_length=300,
        verbose_name="Адрес"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
        ordering = ["name"]
