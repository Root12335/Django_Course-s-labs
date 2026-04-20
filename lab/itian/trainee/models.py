from django.db import models

# Create your models here.

from django.db import models
from course.models import Course

class Trainee(models.Model):

    name = models.CharField(max_length=100)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name