from rest_framework.routers import DefaultRouter
from accounts.api.urls import tutorial_router
from django.urls import path, include

router = DefaultRouter()
#tutorials
router.registry.extend(tutorial_router.registry)

urlpatterns = [
    path('', include(router.urls))
]