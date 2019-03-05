from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newUser/', views.newUser, name="newUser"),
    path('gamePage/', views.gameUser, name="gamePage"),
    path('gameEntry/', views.gameEntry, name="gameEntry"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]