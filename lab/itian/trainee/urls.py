from django.urls import path
from . import views

urlpatterns = [

    path(
        'list',
        views.list_trainee,
        name='trainee_list'
    ),

    path(
        '<int:id>',
        views.detail
    ),

    path(
        'add',
        views.TraineeCreate.as_view(),
        name='trainee_add'
    ),

    path(
        'update/<int:pk>',
        views.TraineeUpdate.as_view(),
        name='trainee_update'
    ),

    path(
        'delete/<int:id>',
        views.delete,
        name='trainee_delete'
    ),

]