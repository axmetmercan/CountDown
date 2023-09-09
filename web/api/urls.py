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
router.register(r'Profile', ProfileViewset, basename="Get Profile Info")
router.register(r'Contact', ContactViewset, basename="Get Profile Contact")
router.register(r'Experiences', ExperiencesViewset, basename="Get Profile Experiences")
router.register(r'Project-categories', ProjectCategoriesViewset, basename="Get Project Categories")
router.register(r'Projects', ProjectViewset, basename="Get Profile Projects")
router.register(r'Abilities', AbilitiesViewset, basename="Get Profile Abilities")
router.register(r'Referances', ReferancesViewset, basename="Get Profile referances")



urlpatterns = [
    path('/v1/', include(router.urls))
]