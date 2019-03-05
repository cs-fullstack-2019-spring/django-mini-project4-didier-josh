from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newUser/', views.newUser, name="newUser"),
    path('gameUser/', views.gameUser, name="gameUser"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]