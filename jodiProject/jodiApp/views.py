from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserLoginForm, UserLoginModel, GameForm, GameModel
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    addGame = GameModel.objects.all()
    return render(request, 'jodiApp/index.html', {'addGame': addGame})


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
    return render(request, 'jodiApp/gameEntry.html', {"newGame": newGame})


def gameUser(request):
    newGame = GameModel.objects.filter(gameForeignKey=request.user)
    context = {
        "games": newGame
    }
    return render(request, 'jodiApp/gamePage.html', context)


def delete(request, ID):
    deleted_game = get_object_or_404(GameModel, pk=ID)
    if request.method == 'POST':
        deleted_game.delete()
        return redirect('index')

    return render(request, 'jodiApp/delete.html', {"deleted_game": deleted_game})
