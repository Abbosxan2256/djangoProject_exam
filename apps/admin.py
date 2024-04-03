from django.contrib import admin
from apps.models import ContactsPage
from import_export.admin import ImportExportModelAdmin


@admin.register(ContactsPage)
class ContactAdmin(ImportExportModelAdmin):
    pass





