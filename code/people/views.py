from django.utils.translation import ugettext_lazy as _

from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .models import Person
from .tables import PeopleTable
from .filters import PeopleFilter


class PeopleListView(SingleTableMixin, FilterView):
    """
    View to list and filter the people.

    If in the future you want to improve the performance
    of the queryset, you can improve it by using a lazy page.
    (paginator_class = LazyPaginator)
    """
    template_name = 'people/dashboard.html'
    table_class = PeopleTable
    model = Person
    paginate_by = 5
    filterset_class = PeopleFilter
    extra_context = {
        'title': _('People'),
    }
