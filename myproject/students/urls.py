from django.urls import path
from .views import student_list, add_student, get_by_id, update_student, delete_student

urlpatterns = [
    path('student', student_list),
    path('student/new', add_student),
    path('student/<int:id>', get_by_id),
    path('student/<int:id>/update', update_student),
    path('student/<int:id>/del', delete_student)
]