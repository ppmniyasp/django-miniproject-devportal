from django.urls import path
from . import views

urlpatterns = [
    path('',views.display_Projects, name="projects"),
    path('add-project/',views.addProject, name="add-project"),
    path('view-project/<str:pk>',views.viewProject, name="view-project"),
    path('edit-project/<str:pk>',views.editProject, name="edit-project"),
    path('delete-project/<str:pk>',views.deleteProject, name="delete-project"),
]