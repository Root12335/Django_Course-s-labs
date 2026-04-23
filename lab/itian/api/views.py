from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from course.models import Course
from trainee.models import Trainee
from .serializers import CourseSerializer, TraineeSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TraineeViewSet(viewsets.ModelViewSet):
    queryset = Trainee.objects.select_related('course').all()
    serializer_class = TraineeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    