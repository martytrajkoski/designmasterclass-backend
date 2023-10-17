from rest_framework.routers import DefaultRouter
from accounts.api.urls import tutorialphotoshop_router, tutorialillustrator_router
from django.urls import path, include

router = DefaultRouter()
#tutorials
router.registry.extend(tutorialphotoshop_router.registry)
router.registry.extend(tutorialillustrator_router.registry)

urlpatterns = [
    path('', include(router.urls))
]