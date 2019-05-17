from django.urls import path
from . import views


urlpatterns = [
    # Auth
    path('', views.PeopleListView.as_view(), name='dashboard'),
]
