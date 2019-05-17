from django_tables2 import Table

from .models import Person


class PeopleTable(Table):
    """
    Table to list the people.
    """
    class Meta():
        model = Person
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at')

