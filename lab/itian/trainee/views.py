
# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect
from .models import Trainee

def list_trainee(request):

    trainees = Trainee.objects.all()

    return render(
        request,
        'trainee/list.html',
        {
            'trainees': trainees
        }
    )


def detail(request, id):

    trainee = Trainee.objects.get(id=id)

    return render(
        request,
        'trainee/detail.html',
        {
            'trainee': trainee
        }
    )


def add(request):

    if request.method == "POST":

        name = request.POST.get("name")

        Trainee.objects.create(
            name=name
        )

        return redirect("/trainee")

    return render(
        request,
        'trainee/add.html'
    )


def update(request, id):

    trainee = Trainee.objects.get(id=id)

    if request.method == "POST":

        trainee.name = request.POST.get("name")

        trainee.save()

        return redirect("/trainee")

    return render(
        request,
        'trainee/update.html',
        {
            'trainee': trainee
        }
    )


def delete(request, id):

    trainee = Trainee.objects.get(id=id)

    if request.method == "POST":

        trainee.delete()

        return redirect("/trainee")

    return render(
        request,
        'trainee/delete.html'
    )