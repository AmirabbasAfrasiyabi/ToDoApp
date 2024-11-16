
from django.urls import path
from .views import TaskList , TaskDetailView , TaskCreateView , TaskUpdateView , TaskDeleteView , CustomLoginViews , CustomLogoutView , RegisterPage , TaskReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginViews.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    
]

