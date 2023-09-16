from django.contrib import admin
from django.http.request import HttpRequest
from SiteSetup.models import MenuLink, SiteSetup


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_Or_Path'
    list_display_links = 'id', 'text', 'url_Or_Path'
    search_fields = 'id', 'text', 'url_Or_Path'


class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description'
    list_display_links = 'title', 'description'
    search_fields = 'title', 'description'
    inlines = MenuLinkInLine,

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()