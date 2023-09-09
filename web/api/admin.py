from django.contrib import admin
from .models import (Profile, 
                    Contact,
                    WorkExperinces,
                    ProjectCategories,
                    Projects,
                    Abilities,
                    Referances
                    )
# Register your models here.
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(WorkExperinces)
admin.site.register(ProjectCategories)
admin.site.register(Projects)
admin.site.register(Abilities)
admin.site.register(Referances)