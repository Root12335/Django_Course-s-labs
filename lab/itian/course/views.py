from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Course

def list_course(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses': courses})

def detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'course/detail.html', {'course': course})

class CourseCreate(CreateView):
    model = Course
    fields = ['name']
    template_name = 'course/add.html'
    success_url = reverse_lazy('course_list')

class CourseUpdate(UpdateView):
    model = Course
    fields = ['name']
    template_name = 'course/update.html'
    success_url = reverse_lazy('course_list')

def delete(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request, 'course/delete.html', {'course': course})
