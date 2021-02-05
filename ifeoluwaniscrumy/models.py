from django.db import models
from django.contrib.auth.models import User
from django.db.models import PROTECT

# Create your models here.

 
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=200)


class ScrumyGoal(models.Model):
    goal_status = models.ForeignKey(GoalStatus, on_delete=PROTECT)
    user = models.ForeignKey(User, related_name="ifeoluwani", null=True, on_delete=models.SET_NULL)
    goal_name = models.CharField(max_length=200)
    goal_id = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)


class ScrumyHistory(models.Model):
    goal = models.ForeignKey(ScrumyGoal, null=True, on_delete=models.SET_NULL)
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_fro = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.CharField(max_length=200)

