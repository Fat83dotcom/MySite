from django.contrib import admin
from django.urls import reverse
from Core.models import Tag, Category, Post
from Core.models import Portfolio, PortfolioProjects, ProjectsLinks
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name', 'slug'
    list_filter = 'name', 'slug'
    list_per_page = 10
    ordering = '-id',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name', 'slug'
    list_filter = 'name', 'slug'
    list_per_page = 10
    ordering = '-id',


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = 'id', 'title', 'isPublished', 'createdBy', 'link'
    list_display_links = 'title', 'link'
    search_fields = 'id', 'slug', 'title', 'excerpt',
    list_per_page = 10
    list_filter = 'isPublished',
    list_editable = 'isPublished',
    ordering = '-id',
    readonly_fields = (
        'createdAt', 'updatedAt', 'updatedBy', 'createdBy', 'link'
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    summernote_fields = ('content',)

    def link(self, post):
        if not post.id:
            return '-'
        urlPost = reverse('blogPost', args=(post.slug,))
        return mark_safe(f'<a href="{urlPost}" target="_blank">Post</a>')

    def save_model(self, request, obj, form, change):
        if change:
            obj.updatedBy = request.user
        else:
            obj.createdBy = request.user

        obj.save()


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = 'title',
    list_display_links = 'title',


class ProjectLinksInLine(admin.TabularInline):
    model = ProjectsLinks
    extra = 1


@admin.register(PortfolioProjects)
class PortfolioProjectsAdmin(SummernoteModelAdmin):
    list_display = 'name', 'typeProject', 'isPublished'
    list_display_links = 'name',
    list_editable = 'isPublished',
    inlines = ProjectLinksInLine,
