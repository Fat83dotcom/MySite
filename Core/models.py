from django.db import models
from utils.randstr import slugfyNew
from django.contrib.auth.models import User
from utils.images import resizeImage
from django.urls import reverse


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


class Portfolio(models.Model):
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portifolios'
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default='',
        null=False,
        blank=True,
        max_length=255
    )

    def __str__(self) -> str:
        return self.title


class PortfolioProjects(models.Model):
    class Meta:
        verbose_name = 'Portfolio_Project'
        verbose_name_plural = 'Portifolio_Project'

    PORJECT_CHOICE = (
        ('P', 'Pessoal'),
        ('C', 'Cliente'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    typeProject = models.CharField(max_length=1, choices=PORJECT_CHOICE)
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.SET_NULL,
        null=True,
        related_name='portfolioProject'
    )
    pictures = models.ImageField(
        upload_to='projects/%Y/%m/',
        blank=True,
        default=''
    )
    slug = models.SlugField(
        unique=True,
        default='',
        null=False,
        blank=True,
        max_length=255
    )
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugfyNew(self.name, 10)

        super().save(*args, **kwargs)

        if self.pictures:
            resizeImage(self.pictures, 500)


class ProjectsLinks(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=2048, null=True)
    project = models.ForeignKey(
        PortfolioProjects,
        on_delete=models.SET_NULL,
        related_name='linkProject',
        null=True
    )

    def __str__(self):
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default='',
        null=False,
        blank=True,
        max_length=255
    )
    isPublished = models.BooleanField(
        default=False, help_text='Marque para publicar.'
    )
    content = models.TextField()

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugfyNew(self.title, 10)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class PostManager(models.Manager):
    def getIsPublished(self):
        return self.filter(isPublished=True).order_by('-id')


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    objects = PostManager()

    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255)
    content = models.TextField()
    cover = models.ImageField(
        upload_to='posts/%Y/%m/', blank=True, default=''
    )
    coverInPostContent = models.BooleanField(
        default=True,
        help_text='Exibe a imagem no conteudo do post.'
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='createdBy'
    )
    updatedAt = models.DateTimeField(auto_now=True)
    updatedBy = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='updatedBy'
    )
    categoryKey = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True,
        default=None
    )
    tagKey = models.ManyToManyField(Tag, blank=True, default='')
    slug = models.SlugField(
        unique=True,
        default='',
        null=False,
        blank=True,
        max_length=255
    )
    isPublished = models.BooleanField(
        default=False, help_text='Marque para publicar.'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if not self.isPublished:
            return reverse('blogIndex')
        return reverse('blogPost', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugfyNew(self.title, 10)

        super().save(*args, **kwargs)

        if self.cover:
            resizeImage(self.cover, 900)
