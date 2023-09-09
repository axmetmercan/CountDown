from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import ProfileSerializer, AbilitiesSerializer,ReferancesSerializer,ProjectSerializer, ProjectCategoriesSerializer, ContactSerializer, ExperinceSerializer
from .models import Profile, Contact, WorkExperinces, ProjectCategories, Projects, Abilities, Referances
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset =Profile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ContactViewset(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class ExperiencesViewset(viewsets.ModelViewSet):
    serializer_class = ExperinceSerializer
    queryset = WorkExperinces.objects.all()

class ProjectCategoriesViewset(viewsets.ModelViewSet):
    serializer_class =ProjectCategoriesSerializer
    queryset = ProjectCategories.objects.all()

class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()


class AbilitiesViewset(viewsets.ModelViewSet):
    serializer_class = AbilitiesSerializer
    queryset = Projects.objects.all()

    
class ReferancesViewset(viewsets.ModelViewSet):
    serializer_class = ReferancesSerializer
    queryset = Projects.objects.all()

    