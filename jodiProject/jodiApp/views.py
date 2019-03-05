from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserLoginModel, GameForm, GameModel


# Create your views here.
def index(request):
    return render(request, 'jodiApp/index.html')

def newUser(request):
    newLogin = UserLoginForm(request.POST or None)
    print (request.POST)
    if newLogin.is_valid():
        print("save")
        newLogin.save()
        return redirect('index')
    context = {
        "newLogin": newLogin
    }

    return render(request, 'jodiApp/newUser.html', context)
