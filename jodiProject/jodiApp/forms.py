from django import forms
from .models import UserLoginModel, GameModel


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginModel
        exclude = ["dateAccountCreated", "userTableForeignKey"]


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ["gameForeignkey"]

    def clean_dateMade(self):
        dateMadeData = self.cleaned_data["dateMade"]

        if dateMadeData == None:
            raise forms.ValidationError("Input date")

    def clean_ageLimit(self):
        ageLimitData = self.clean_ageLimit["ageLimit"]

        if ageLimitData < 10:
            raise forms.ValidationError("You're too young for this game!")
