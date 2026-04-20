from django.urls import path
from . import views

urlpatterns = [

    path(
        'list',
        views.list_trainee
    ),

    path(
        '<int:id>',
        views.detail
    ),

    path(
        'add',
        views.add
    ),

    path(
        'update/<int:id>',
        views.update
    ),

    path(
        'delete/<int:id>',
        views.delete
    ),

]