from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/',views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/filter_example/',views.testing, name='filter_example'),
    path('members/filter/',views.filter_django, name='filter_djano'),
    path('members/django_tags/',views.django_tags, name='django_tags'),
    path('members/templates/',views.template_test, name='templates'),
]
