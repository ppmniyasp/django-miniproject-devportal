from django.shortcuts import render,redirect
from .models import Projects
from django.contrib import messages
from . forms import addProjectForm, ReviewForm
from . utils import searchProjects

# Create your views here.

def display_Projects(request):
    projects,search_query = searchProjects(request)

    context = {'projects':projects,'search_query':search_query}
    return render(request,'projects/display_projects.html',context)

def viewProject(request,pk):
    project = Projects.objects.get(id = pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user
        review.project = project
        form.save()

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('view-project',pk = project.id)

    context = {'project':project, 'form':form}
    return render(request,'projects/view_project.html',context)


def addProject(request):
    form = addProjectForm()
    if request.method == 'POST':
        form = addProjectForm(request.POST,request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/add_project.html',context)

def editProject(request,pk):
    project = Projects.objects.get(id = pk)
    form = addProjectForm(instance=project)
    if request.method == 'POST':
        form = addProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/add_project.html',context)


def deleteProject(request,pk):
    project = Projects.objects.get(id = pk)
    project.delete()
    return redirect('projects')
