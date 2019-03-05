from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newUser/', views.newUser, name="newUser"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]