from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'company', 'lead_status', 'phone_number', 'date_created', 'last_contacted')
    list_filter = ('lead_status',)
    search_fields = ('first_name', 'email', 'company', 'lead_status', 'position', 'lead_source', )

