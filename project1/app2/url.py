from django.urls import path
from . import views

urlpatterns = [
    path('taskhome/',views.taskhome),
    path('taskabout/',views.taskabout),
]