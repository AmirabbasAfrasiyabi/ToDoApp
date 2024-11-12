from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView
from django.shortcuts import redirect
from .models import Task  

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class CustomLoginViews(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreateView(CreateView):
    model = Task
    fields= '__all__'
    success_url = reverse_lazy('tasks')
    

class TaskUpdateView(UpdateView):
    model = Task
    fields= '__all__'
    success_url = reverse_lazy('tasks')
    

class TaskDeleteView(DeleteView):
    model = Task
    fields= '__all__'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')