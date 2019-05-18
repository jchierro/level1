from django.urls import path
from . import views


urlpatterns = [
    # Dashboard
    path('', views.PeopleListView.as_view(), name='dashboard'),
]
