from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, TraineeViewSet


router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course-api')
router.register('trainees', TraineeViewSet, basename='trainee-api')

urlpatterns = router.urls
