from django.db import models
from django.contrib.auth.models import User

# Create your models here.

 
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name="ifeoluwani", null=True, on_delete=models.SET_NULL)
    goal_name = models.CharField(max_length=200)
    goal_id = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    goal = models.ForeignKey(ScrumyGoals, null=True, on_delete=models.SET_NULL)
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.CharField(max_length=200)

    def __str__(self):
        return self.created_by

