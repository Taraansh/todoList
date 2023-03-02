from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDescription=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Task.objects.all()
    # for item in allTasks:
    #     print(item.taskTitle)
    #     print(item.taskDescription)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)