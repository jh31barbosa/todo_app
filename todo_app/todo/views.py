from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="signin-user")
def home(request):
    todos = Todo.objects.all().filter(user=request.user)
    if request.method == "GET":
        return render(request, "home.html", {"todos": todos})
    if request.method == "POST":
        todo = request.POST["task"].strip()
        todo = Todo.objects.create(title=todo, user=request.user)
        todo.save()
        return redirect("home")
    return render(request, "home.html", {"todos": todos})


@login_required(login_url="signin-user")
def edit_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo_form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        todo_form = TodoUpdateForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
            return redirect("home")
    # if request.POST["task"] == "1"

    return render(request, "edit.html", {"todo_form": todo_form, "todo": todo})


@login_required(login_url="signin-user")
def deleteTodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("home")


# user Authentication


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
