from django import forms
from .models import UserLoginModel, GameModel



class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginModel
        exclude = ["dateAccountCreated", "userTableForeignKey"]

    def clean_password2(self):
        password1Data = self.cleaned_data.get("password1")
        password2Data = self.cleaned_data.get("password2")
        print(password2Data)
        print(password1Data)
        if str(password1Data) != str(password2Data):
            raise forms.ValidationError("Does not Match")
        return password1Data


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ["gameForeignkey"]

    def clean_dateMade(self):
        dateMadeData = self.cleaned_data["dateMade"]

        if dateMadeData == None:
            raise forms.ValidationError("Must Enter Date")
        return dateMadeData

    def clean_ageLimit(self):
        ageLimitData = self.clean_ageLimit["ageLimit"]

        if ageLimitData < 10:
            raise forms.ValidationError("You're too young for this game!")
        return ageLimitData
