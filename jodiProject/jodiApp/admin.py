from django.contrib import admin
from .models import UserLoginModel, GameModel

# Register your models here.
admin.site.register(UserLoginModel)
admin.site.register(GameModel)