from rest_framework.serializers import ModelSerializer
from .models import Profile, Contact, WorkExperinces, ProjectCategories, Projects, Abilities, Referances


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ExperinceSerializer(ModelSerializer):
    class Meta:
        model = WorkExperinces
        fields = "__all__"


class ProjectCategoriesSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategories
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class AbilitiesSerializer(ModelSerializer):
    class Meta:
        model = Abilities
        fields = "__all__"

class ReferancesSerializer(ModelSerializer):
    class Meta:
        model = Referances
        fields = "__all__"