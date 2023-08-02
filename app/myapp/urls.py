from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='todo_list/', view=views.todos, name='todo_list')
]
