from django.urls import path
from . import views
urlpatterns = [
    path('', views.view_students, name="user.view_students"),
    path('student/view_cities', views.view_cities, name="user.view_cities"),
    path('student/add_student', views.add_student, name="user.add_student"),
    path('student/delete_student/<int:SID>', views.delete_student, name="user.delete_student"),
    path('student/update_student/<int:SID>', views.update_student, name="user.update_student"),
    path('student/multi/add_student', views.multi_add_student, name="user.multi_add_student"),
    path('student/multi/delete_student/<int:SID>', views.multi_delete_student, name="user.multi_delete_student"),
    path('student/multi/update_student/<int:SID>', views.multi_update_student, name="user.multi_update_student"),
    path('student/multi', views.multi_view_students, name="user.multi_view_students"),
]