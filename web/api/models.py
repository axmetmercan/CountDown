from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default=None)
    picture = models.ImageField(null=True, blank=True)


class Contact(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_contacts", default=None)
    title = models.CharField(max_length=100, default=None)
    value = models.CharField(max_length=100, default=None)


class WorkExperinces(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_works")
    category = models.ForeignKey(
        'ProjectCategories', on_delete=models.CASCADE, related_name="related_category")
    company_title = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    referance = models.ForeignKey(
        'Referances', on_delete=models.SET_NULL, null=True)


class ProjectCategories(models.Model):
    title = models.CharField(max_length=100, default=None)


class Projects(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_projects", default=None)
    title = models.CharField(max_length=100, null=False,blank=False)
    description = models.TextField(max_length=255, null=False,blank=False, default=None)
    referance_link = models.CharField(max_length=200, null=False,blank=False,default=None)
    project_picture = models.ImageField(verbose_name="Project Image", default=None)
    referance = models.ForeignKey(
        'Referances', on_delete=models.SET_NULL, null=True, blank=True)


class Abilities(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_abilities",default=None)
    degree = models.IntegerField(validators=[MinValueValidator(1, message="Min value should be 1 atleast"),
                                             MaxValueValidator(100, message="Max value should be 100 most" )],default=1)
    title = models.CharField(max_length=100, verbose_name="Pl", default=None)


class Referances(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
