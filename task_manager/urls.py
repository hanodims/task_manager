"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', TokenObtainPairView.as_view(), name="login"),
    #path('register/', views.Register.as_view(), name="register"),
    
    path('create/', views.CreateBoard.as_view(), name="board-create"),
    path('<int:board_id>/delboard/', views.DeleteBoard.as_view(), name="delete-board"),
    path('', views.ListBoard.as_view(), name="board-list"),
    path('list/', views.UserListBoard.as_view(), name="user-board-list"),

    path('<int:board_id>/createtask/', views.CreateTask.as_view(), name="create-task"),
    path('<int:task_id>/hidetask/', views.HideTask.as_view(), name="hide-task"),
    path('<int:task_id>/deltask/', views.DeleteTask.as_view(), name="delete-task"),

    path('<int:board_id>/all/', views.ListBoardTask.as_view(), name="board-task"),

]
