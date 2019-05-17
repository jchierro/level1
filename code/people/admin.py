from django.contrib import admin

from .models import Person


class BaseAdmin(admin.ModelAdmin):
    """
    Basic class to inherit.
    """
    search_fields = ['__all__']
    list_filter = ['created_at', 'updated_at']


class PersonAdmin(BaseAdmin):
    """
    class PersonAdmin
    """
    list_display = ('email', 'username', 'created_at', 'updated_at')


admin.site.register(Person, PersonAdmin)
