from django.urls import path
from . import views
urlpatterns = [
    path('student/view', views.view_students, name="user.view_students"),
    path('student/view_cities', views.view_cities, name="user.view_cities"),
]