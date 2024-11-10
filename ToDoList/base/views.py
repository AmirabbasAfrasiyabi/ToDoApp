from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task  
class taskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task'
