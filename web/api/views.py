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
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class ExperiencesViewset(viewsets.ModelViewSet):
    serializer_class = ExperinceSerializer
    queryset = WorkExperinces.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectCategoriesViewset(viewsets.ModelViewSet):
    serializer_class =ProjectCategoriesSerializer
    queryset = ProjectCategories.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class AbilitiesViewset(viewsets.ModelViewSet):
    serializer_class = AbilitiesSerializer
    queryset = Abilities.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    
class ReferancesViewset(viewsets.ModelViewSet):
    serializer_class = ReferancesSerializer
    queryset = Referances.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    