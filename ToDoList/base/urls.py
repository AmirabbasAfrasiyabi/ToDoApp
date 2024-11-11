
from django.urls import path
from .views import TaskList , TaskDetailView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task'),
    
]

