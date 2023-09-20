from django.contrib import admin
from django.urls import reverse
from Core.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name', 'slug'
    list_filter = 'name', 'slug'
    list_per_page = 10
    ordering = '-id',
    # prepopulated_fields = {
    #     'slug': ('name',),
    # }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'name', 'slug'
    list_filter = 'name', 'slug'
    list_per_page = 10
    ordering = '-id',
    # prepopulated_fields = {
    #     'slug': ('name',),
    # }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug', 'isPublished', 'content'
    search_fields = 'id', 'title', 'slug', 'isPublished'
    list_display_links = 'title', 'slug', 'isPublished'
    list_filter = 'title', 'slug'
    list_per_page = 10
    ordering = '-id',
    # prepopulated_fields = {
    #     'slug': ('name',),
    # }


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = 'id', 'title', 'isPublished', 'createdBy',
    list_display_links = 'title',
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
    # autocomplete_fields = 'tagKey', 'categoryKey',

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
