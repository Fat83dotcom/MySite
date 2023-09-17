from django.db import models
from utils.randstr import slugfyNew


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugfyNew(self.name, 10)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugfyNew(self.name, 10)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
