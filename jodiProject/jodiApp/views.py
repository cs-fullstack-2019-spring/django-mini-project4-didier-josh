from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserLoginModel, GameForm, GameModel
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'jodiApp/index.html')


def newUser(request):
    newLogin = UserLoginForm(request.POST or None)
    print(request.POST)
    if newLogin.is_valid():
        User.objects.create_user(request.POST["username"], "", request.POST["password2"])
        print("save")
        newLogin.save()
        return redirect('index')

    context = {
        "newLogin": newLogin
    }

    return render(request, 'jodiApp/newUser.html', context)



def gameEntry(request):
    newGame = GameForm(request.POST or None)
    print(request.POST)
    if newGame.is_valid():
        print("save")
        newGame.save()
        return redirect('index')

    context = {
        "newGame": newGame
    }
    return render(request, 'jodiApp/gamePage.html', context)

def gameUser(request):
    return render(request, 'jodiApp/gamePage.html')

