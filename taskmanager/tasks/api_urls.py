from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = router.urls