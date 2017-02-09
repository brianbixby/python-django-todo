from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Todo

# Create your views here.
def index(request):
    if request.method == "GET":
        context = {
            "todos": Todo.objects.all()
        }
        return render(request, 'todoapp/index.html', context)
    elif request.method == "POST":
        new_todo = Todo()
        new_todo.text = request.POST["text"]
        new_todo.save()
        # redirect name defined in urls
        return redirect('index')

def signup(request):
    context = {"error": False}
    if request.method == "GET":
        return render(request, 'todoapp/signup.html', context)
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            if user is not None:
                return login(request)
        except:
            context["error"] = f"User {username} already exists"
            return render(request, 'todoapp/signup', context)

def login(request):
    if request.method == "GET":
        return render(request, 'todoapp/login.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = auth.authenticate(username=username, password=password, email=email)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def secret(request):
    context = {"error": False}
    if request.user.is_authenticated:
        return render(request, 'todoapp/secret.html')
    else:
        context["error"] = "Not authenticated"
        return render(request, 'todoapp/signup.html', context)
