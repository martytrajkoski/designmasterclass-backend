from rest_framework.routers import DefaultRouter
from accounts.api.urls import tutorialillustrator_router, tutorialphotoshop_router, course_router
from django.urls import path, include

router = DefaultRouter()
#tutorials
router.registry.extend(tutorialillustrator_router.registry)
router.registry.extend(tutorialphotoshop_router.registry)
router.registry.extend(course_router.registry)

urlpatterns = [
    path('', include(router.urls))
]