from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import *

# Create your views here.


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goal)


def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.filter(goal_id=goal_id)
    return HttpResponse(goal)


def add_goal(request):
    random_num = random.randint(1000, 9999)

    if GoalStatus.objects.get(goal_id=random_num):
        print('goal_id exists')

    else:
        first = ScrumyGoals.objects.create(goal_name = 'Keep learning Django', goal_id= random_num , created_by= 'louis', moved_by='louis', owner= 'louis', goal_status= GoalStatus.objects.get(status_name = 'Weekly Goal'), user=User.objects.get(username = 'louis'))
        first.save()
    
    return HttpResponse (first)


def home(request):
    goals = ScrumyGoals.objects.filter(goal_name = 'Keep learning Django')
    output = ', '.join([goal.goal_name for goal in goals])
    return HttpResponse(output)


