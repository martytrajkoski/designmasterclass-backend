# from rest_framework.routers import DefaultRouter
# from accounts.api.urls import tutorialillustrator_router, tutorialphotoshop_router, course_router, userLogin_router, userLogout_router, userView_router, userRegister_router
# from django.urls import path, include

# router = DefaultRouter()
# #tutorials
# router.registry.extend(tutorialillustrator_router.registry)
# router.registry.extend(tutorialphotoshop_router.registry)
# router.registry.extend(course_router.registry)

# #user
# router.registry.extend(userLogin_router.registry)
# router.registry.extend(userLogout_router.registry)
# router.registry.extend(userRegister_router.registry)
# router.registry.extend(userView_router.registry)

# urlpatterns = [
#     path('', include(router.urls))
# ]