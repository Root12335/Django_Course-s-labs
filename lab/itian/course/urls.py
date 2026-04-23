from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_course, name='course_list'),
    path('<int:id>', views.detail, name='course_detail'),
    path('add', views.CourseCreate.as_view(), name='course_add'),
    path('update/<int:pk>', views.CourseUpdate.as_view(), name='course_update'),
    path('delete/<int:id>', views.delete, name='course_delete'),
]
