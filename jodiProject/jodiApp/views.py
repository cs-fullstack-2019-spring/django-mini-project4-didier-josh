from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserLoginForm, UserLoginModel, GameForm, GameModel
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        userLog = UserLoginModel.objects.get(username=request.user)
        addGame = GameModel.objects.filter(gameForeignkey=userLog)
        return render(request, 'jodiApp/index.html', {'addGame': addGame})
    else:
        return render(request, 'jodiApp/index.html')


# lets a user create a new account
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


# allows a game to be entered
def gameEntry(request):
    newGame = GameForm(request.POST or None)
    print(request.POST)
    if newGame.is_valid():
        print("save")
        userLog = UserLoginModel.objects.get(username=request.user)
        GameModel.objects.create(name=request.POST["name"], developer=request.POST["developer"],
                                 dateMade=request.POST["dateMade"], ageLimit=request.POST["ageLimit"],
                                 gameForeignkey=userLog)
        return redirect('index')
    return render(request, 'jodiApp/gameEntry.html', {"newGame": newGame})


# edit game
def edit(request, ID):
    edit_game = get_object_or_404(GameModel, pk=ID)
    gameToEdit = GameForm(request.POST or None, instance=edit_game)
    if gameToEdit.is_valid():
        gameToEdit.save()
        return redirect('index')

    return render(request, 'jodiApp/gameEntry.html', {'newGame': gameToEdit})


# delete game
def delete(request, ID):
    deleted_game = get_object_or_404(GameModel, pk=ID)
    if request.method == 'POST':
        deleted_game.delete()
        return redirect('index')

    return render(request, 'jodiApp/delete.html', {"deleted_game": deleted_game})
