from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description', 'complete'] 
    success_url = reverse_lazy('tasks')

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    fields= '__all__'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')