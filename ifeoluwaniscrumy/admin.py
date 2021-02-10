from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)


