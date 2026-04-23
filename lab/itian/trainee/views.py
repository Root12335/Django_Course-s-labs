
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


from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

class TraineeCreate(CreateView):
    model = Trainee
    fields = ['name', 'course']
    template_name = 'trainee/add.html'
    success_url = reverse_lazy('trainee_list')

class TraineeUpdate(UpdateView):
    model = Trainee
    fields = ['name', 'course']
    template_name = 'trainee/update.html'
    success_url = reverse_lazy('trainee_list')


def delete(request, id):

    trainee = Trainee.objects.get(id=id)

    if request.method == "POST":

        trainee.delete()

        return redirect("trainee_list")

    return render(
        request,
        'trainee/delete.html',
        {
            'trainee': trainee
        }
    )