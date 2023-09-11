from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Profile, Contact, WorkExperinces, ProjectCategories, Projects, Abilities, Referances


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    profile = StringRelatedField(read_only=True)
    class Meta:
        model = Contact
        fields = "__all__"


class ExperinceSerializer(ModelSerializer):
    profile = StringRelatedField(read_only=True)
    category = StringRelatedField(read_only=True)
    class Meta:
        model = WorkExperinces
        fields = "__all__"


class ProjectCategoriesSerializer(ModelSerializer):
    profile = StringRelatedField(read_only=True)

    class Meta:
        model = ProjectCategories
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    profile = StringRelatedField(read_only=True)
    class Meta:
        model = Projects
        fields = "__all__"


class AbilitiesSerializer(ModelSerializer):
    profile = StringRelatedField(read_only=True)

    class Meta:
        model = Abilities
        fields = "__all__"

class ReferancesSerializer(ModelSerializer):
    profile = StringRelatedField(read_only=True)

    class Meta:
        model = Referances
        fields = "__all__"