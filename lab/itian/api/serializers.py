from rest_framework import serializers

from course.models import Course
from trainee.models import Trainee


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id', 'name', 'course']
