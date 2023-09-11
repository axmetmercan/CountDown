from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Create a ForeignKey relationship with User
    name = models.CharField(max_length=100, default="", null=False, blank=False)
    surname = models.CharField(max_length=100, default="Ahmet", null=False, blank=False)
    title = models.CharField(max_length=100, default=None)
    picture = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        full_name = self.name +" " + self.surname
        return full_name
    class Meta:
            verbose_name = "Profile"
            verbose_name_plural = "Profiles"



class Contact(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_contacts", default=None)
    title = models.CharField(max_length=100, default=None)
    value = models.CharField(max_length=100, default=None)
    icon_class = models.CharField(max_length=100, default="", blank=False, null=False)
   
    def __str__(self):
        
        return self.title
    class Meta:
        verbose_name = "Contacnt"
        verbose_name_plural = "Contacts"

class WorkExperinces(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_works")
    category = models.ForeignKey(
        'ProjectCategories', on_delete=models.CASCADE, related_name="related_category")
    company_title = models.CharField(max_length=100)
    company_website = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    referance = models.ForeignKey(
        'Referances', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        
        return self.company_title
    
    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"

class ProjectCategories(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='profile_project_categories', null=False,blank=False)
    title = models.CharField(max_length=100, default=None)
    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
    

class Projects(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_projects", default=None)
    title = models.CharField(max_length=100, null=False,blank=False)
    description = models.TextField(max_length=255, null=False,blank=False, default=None)
    referance_link = models.CharField(max_length=200, null=False,blank=False,default=None)
    project_picture = models.ImageField(verbose_name="Project Image", default=None, null=True,blank=True)
    referance = models.ForeignKey(
        'Referances', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    
class Abilities(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_abilities",default=None)
    degree = models.IntegerField(validators=[MinValueValidator(1, message="Min value should be 1 atleast"),
                                             MaxValueValidator(100, message="Max value should be 100 most" )],default=1)
    title = models.CharField(max_length=100, verbose_name="Pl", default=None)

    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = "Ability"
        verbose_name_plural = "Abilities"
    
class Referances(models.Model):
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name="profile_referances",default=None)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    def __str__(self):
        
        return self.name
    class Meta:
        verbose_name = "Reference"
        verbose_name_plural = "Referances"
    