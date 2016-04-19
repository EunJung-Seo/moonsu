from django.db import models


class Phrase (models.Model):
    book_name = models.CharField(
        max_length=20,
    )

    book_cover = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )

    writer = models.CharField(
        max_length=20,
    )

    publisher = models.CharField(
        max_length=20,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return "{book_name} / {writer} / {publisher}".format(
            book_name=self.book_name,
            writer=self.writer,
            publisher=self.publisher,
        )
