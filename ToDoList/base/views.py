from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task  
class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

    