from django.urls import path
from .views import (
    register, user_login, user_logout, 
    task_list, task_detail, task_create, task_edit, task_delete
)
from .views import custom_logout

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    path("", task_list, name="task_list"),
    path("<int:task_id>/", task_detail, name="task_detail"),
    path("create/", task_create, name="task_create"),
    path("<int:task_id>/edit/", task_edit, name="task_edit"),
    path("<int:task_id>/delete/", task_delete, name="task_delete"),
    path('logout/', custom_logout, name='logout'),
]
