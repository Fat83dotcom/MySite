from django.contrib import admin
from Core.models import Tag, Category, Page


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
    list_display = 'id', 'title', 'slug'
    list_display_links = 'title', 'slug'
    list_filter = 'title', 'slug'
    list_per_page = 10
    ordering = '-id',
    # prepopulated_fields = {
    #     'slug': ('name',),
    # }
