from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newUser/', views.newUser, name="newUser"),
    path('gamePage/', views.gamePage, name="gamePage"),
    path('gamePage/delete/<int:ID>/', views.delete, name="delete"),
    path('gamePage/edit/<int:ID>/', views.edit, name="edit"),
    path('gameEntry/', views.gameEntry, name="gameEntry"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
