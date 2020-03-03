from django.contrib import admin

from .models import Link, SideBar
from mblog.custom_site import custom_site
from mblog.BasicOwnerAdmin import BasicOwnerAdmin

@admin.register(Link, site=custom_site)
class LinkAdmin(BasicOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BasicOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')