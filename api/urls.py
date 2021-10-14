

from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet
from .views import EventsViewSet

router = routers.DefaultRouter()
router.register("students",StudentViewSet )
router.register("trainers/",TrainerViewSet )
router.register("courses/",CourseViewSet )
router.register("events/",EventsViewSet )


urlpatterns = [
    path("",include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
]
