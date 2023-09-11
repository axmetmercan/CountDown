from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProfileViewset,
                    ContactViewset,
                    ExperiencesViewset,
                    ProjectCategoriesViewset,
                    ProjectViewset,
                    AbilitiesViewset,
                    ReferancesViewset
                    )

router = DefaultRouter()
router.register(r'profile', ProfileViewset, basename="Get Profile Info")
router.register(r'contact', ContactViewset, basename="Get Profile Contact")
router.register(r'experiences', ExperiencesViewset, basename="Get Profile Experiences")
router.register(r'project-categories', ProjectCategoriesViewset, basename="Get Project Categories")
router.register(r'projects', ProjectViewset, basename="Get Profile Projects")
router.register(r'abilities', AbilitiesViewset, basename="Get Profile Abilities")
router.register(r'referances', ReferancesViewset, basename="Get Profile referances")



urlpatterns = [
    path('/v1/', include(router.urls))
]