from django.db import models
from utils.modelValidator import validatePng
from utils.images import resizeImage


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_Or_Path = models.CharField(max_length=(2048))
    new_Tab = models.BooleanField(default=False)
    site_Setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE, blank=True,
        null=True, default=None
    )

    def __str__(self) -> str:
        return self.text


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_Header = models.BooleanField(default=True)
    show_Search = models.BooleanField(default=True)
    show_Menu = models.BooleanField(default=True)
    show_Description = models.BooleanField(default=True)
    show_Pagination = models.BooleanField(default=True)
    show_Footer = models.BooleanField(default=True)
    fav_icon = models.ImageField(
        upload_to='favicon/%Y/%m/', blank=True,
        default='', validators=[validatePng]
    )

    def save(self, *args, **kwargs) -> None:
        currentFaviconName = str(self.fav_icon.name)
        super().save(*args, **kwargs)
        favIconChanged = currentFaviconName = False

        if self.fav_icon:
            favIconChanged = currentFaviconName != self.fav_icon.name

        if favIconChanged:
            resizeImage(self.fav_icon, 32)

    def __str__(self) -> str:
        return self.title
