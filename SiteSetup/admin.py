from django.contrib import admin
from SiteSetup.models import MenuLink, SiteSetup


class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'title', 'index_description_1',
        'index_description_2', 'blog_description'
    )
    inlines = MenuLinkInLine,
