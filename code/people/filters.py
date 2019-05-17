from django_filters import FilterSet

from .models import Person


class PeopleFilter(FilterSet):
    """
    Class to filter by the attributes of the people.
    """
    class Meta:
        model = Person
        fields = {
            'username': ['icontains'],
            'email': ['icontains']
        }
