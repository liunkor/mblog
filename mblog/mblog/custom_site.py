from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Blog Administrator Page'
    site_title = 'Blog admin page'
    index_title = 'Admin page'

custom_site = CustomSite(name='cus_admin')